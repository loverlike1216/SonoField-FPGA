import math
from .transducer import Transducer

SHAPES = {2: (1, 1), 8: (2, 2), 16: (2, 4), 32: (4, 4), 72: (6, 6), 128: (8, 8)}


def opposing_arrays(total=128, pitch=0.012, gap=0.100, shape="planar", radius=0.180,
                    diameter=0.010, frequency=40000.0):
    """Meters, positions are RADIATING SURFACE CENTERS, origin at array-pair center.

    Planar faces lie at z=+/-gap/2. PCB coordinates require a separate mounting model.
    Curved research alternatives: gap is on-axis face spacing; cap rims extend inward.

    IDs retain physical upper/lower mapping: upper RTL 0..63, lower RTL 64..127.
    No compact renumbering of lower channels for smaller arrays.
    """
    if (not all(math.isfinite(v) for v in (pitch,gap,radius,diameter,frequency)) or
        total not in SHAPES or pitch < diameter or diameter <= 0 or gap <= 0 or
        frequency <= 0 or shape not in ("planar", "concave")):
        raise ValueError("Invalid geometry, unsupported emitter count, or intersecting pitch")
    rows, cols = SHAPES[total]
    elements = []
    for side, sign, base in (("UPPER", 1, 0), ("LOWER", -1, 64)):
        for row in range(rows):
            for col in range(cols):
                x, y = (col - (cols-1)/2)*pitch, (row-(rows-1)/2)*pitch
                r2 = x*x+y*y
                if shape == "concave":
                    if radius <= math.sqrt(r2):
                        raise ValueError("Cap radius too small")
                    depth = math.sqrt(radius*radius-r2)
                    sag = radius-depth
                    z = sign*(gap/2-sag)
                    if sign*z < diameter/2:
                        raise ValueError("Opposing cap clearance too small")
                    normal = (-x/radius, -y/radius, -sign*depth/radius)
                else:
                    z, normal = sign*gap/2, (0.0, 0.0, -float(sign))
                index = row*cols+col
                elements.append(Transducer(f"{side}_TX_{index:02d}", base+index, (x,y,z), normal,
                                          diameter=diameter, frequency=frequency))
    return elements


def planar_profile(config, gap_m=None):
    """Build the user-selected adjustable planar assembly, rejecting out-of-travel gaps.

    Generic opposing_arrays remains available for explicitly labeled research alternatives.
    """
    geometry=dict(config["geometry"])
    gap=geometry["gap"] if gap_m is None else float(gap_m)
    limits=config["gap_range_m"]
    if (config.get("coordinate_reference") != "RADIATING_SURFACE_CENTER" or
        geometry["shape"] != "planar" or not math.isfinite(gap) or
        not limits[0] <= gap <= limits[1]):
        raise ValueError("Planar radiating-face profile requires a gap inside its documented travel range")
    geometry["gap"]=gap
    return opposing_arrays(**geometry)


def coordinate_rows(elements):
    """Millimeter export, both boards in one global frame (not mirrored fabrication views)."""
    return [{"CHANNEL_ID":e.channel_id,"rtl_channel":e.rtl_channel,
             "x_mm":round(e.position[0]*1000,9),"y_mm":round(e.position[1]*1000,9),
             "z_mm":round(e.position[2]*1000,9),"normal_x":e.normal[0],
             "normal_y":e.normal[1],"normal_z":e.normal[2],
             "coordinate_reference":"RADIATING_SURFACE_CENTER"} for e in elements]
