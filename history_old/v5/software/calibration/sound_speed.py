"""Cramer zero-frequency humid-air approximation; assumptions explicit at call site."""
import math


def sound_speed(temperature_c, humidity_percent, pressure_pa, co2_ppm=420):
    t, rh, p, xc = temperature_c, humidity_percent, pressure_pa, co2_ppm*1e-6
    if not (0 <= t <= 30 and 0 <= rh <= 100 and 76000 <= p <= 102000 and 0 <= xc <= .01):
        raise ValueError('Outside documented Cramer approximation domain')
    tk = t + 273.15
    psv = math.exp(1.2811805e-5*tk*tk - .019509874*tk + 34.04926034 - 6353.6311/tk)
    xw = rh*.01*(1.00062 + 3.14e-8*p + 5.6e-7*t*t)*psv/p
    if xw > .06: raise ValueError('Water mole fraction exceeds approximation domain')
    return (331.5024 + .603055*t - .000528*t*t
            + (51.471935 + .1495874*t - .000782*t*t)*xw
            + (-1.82e-7 + 3.73e-8*t - 2.93e-10*t*t)*p
            + (-85.20931 - .228525*t + 5.91e-5*t*t)*xc
            - 2.835149*xw*xw - 2.15e-13*p*p + 29.179762*xc*xc + .000486*xw*p*xc)
