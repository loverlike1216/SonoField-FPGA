import math
from .transducer import Transducer

SHAPES = {2: (1, 1), 8: (2, 2), 16: (2, 4), 32: (4, 4), 72: (6, 6), 128: (8, 8)}


def opposing_arrays(total=72, pitch=0.018, gap=0.160, shape="planar", radius=0.180,
                    diameter=0.016, frequency=40000.0):
    """Meters. gap is on-axis face spacing. Cap rims extend toward the central workspace.

    IDs retain physical upper/lower mapping: upper RTL 0..63, lower RTL 64..127.
    No compact renumbering of lower channels for smaller arrays.
    """
    if total not in SHAPES or pitch < diameter or gap <= 0 or shape not in ("planar", "concave"):
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
