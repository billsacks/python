"""
Functions and class for helping to define a color scheme
"""

from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import sRGBColor, LabColor
from collections import OrderedDict

def diff_cie2000(hex1, hex2):
    """
    Returns delta_e_cie2000 of two colors expressed as hex values

    hex1 and hex2 should be strings of the form '#123456'
    """
    lab1 = convert_color(sRGBColor.new_from_rgb_hex(hex1), LabColor)
    lab2 = convert_color(sRGBColor.new_from_rgb_hex(hex2), LabColor)
    return delta_e_cie2000(lab1, lab2)

class ColorScheme:

    def __init__(self, background_hex, default_hex):
        """
        Initialize a ColorScheme object with a given background and default text color

        background_hex and default_hex should be strings of the form '#123456'
        """
        self._colors = OrderedDict()
        self._colors['background'] = background_hex
        self._colors['default'] = default_hex

    def copy(self):
        """
        Usage: colors2 = colors.copy()

        Copies the colors without sharing a reference to the underlying dictionary
        """
        other = ColorScheme(background_hex = self._colors['background'],
                            default_hex = self._colors['default'])
        other._colors = self._colors.copy()
        return other

    def print_colors(self):
        for color in self._colors:
            print("{}: {}".format(color, self._colors[color]))

    def set_color(self, color, hex_value):
        """
        Add or change a color with the given name
        
        hex_value should be a string of the form '#123456'
        """
        self._colors[color] = hex_value

    def get_color(self, color):
        return self._colors[color]

    def contrasts(self, color, against=None):
        """
        Print color differences of the given named color against other colors
        
        If against is 'None' then print contrasts against all others. Otherwise, against
        should be a list of color names against which we print contrasts. (It's important
        that this be a list, even if it is just a list of size 1.)
        """
        if against is None:
            against = []
            for one_color in self._colors:
                if one_color != color:
                    against.append(one_color)

        self.test_hex(self._colors[color], against=against)

    def test_hex(self, color_hex, against=None):
        """
        Print color differences of the given hex value against other colors

        If against is 'None' then print contrasts against all others. Otherwise, against
        should be a list of color names against which we print contrasts. (It's important
        that this be a list, even if it is just a list of size 1.)
        """
        if against is None:
            against = self._colors.keys()

        for one_color in against:
            print("{}: {}".format(one_color,
                                  diff_cie2000(color_hex, self._colors[one_color])))

    
