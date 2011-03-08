"""
Unit parsing and conversion tool
"""


length_dict = {'meters':1.0,'m':1.0,
        'centimeters':1e-2,'cm':1e-2,
        'millimeters':1e-3,'mm':1e-3,
        'kilometers':1e3,'km':1e3,
        }

frequency_dict = {'Hz':1.0,
        'kHz':1e3,
        'MHz':1e6,
        'GHz':1e9,
        'THz':1e12,
        }

velocity_dict = {'meters/second':1.0,'m/s':1.0,
        'kilometers/s':1e3,'km/s':1e3,'kms':1e3,
        'centimeters/s':1e-2,'cm/s':1e-2,'cms':1e-2,
        }

speedoflight = 2.99792458e8 # m/s
