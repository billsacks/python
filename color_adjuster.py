"""
Class for adjusting rgb colors
"""

from colormath.color_objects import sRGBColor

class ColorAdjuster:

    def __init__(self, r_adjust, g_adjust, b_adjust):
        """Initialize a ColorAdjuster object that will adjust r, g, b by the given amounts
        """
        self._r_adjust = r_adjust
        self._g_adjust = g_adjust
        self._b_adjust = b_adjust

    def adjust_hex(self, orig_hex):
        """Given an original hex value, return the adjusted value"""

        orig_color = sRGBColor.new_from_rgb_hex(orig_hex)
        r = orig_color.rgb_r
        g = orig_color.rgb_g
        b = orig_color.rgb_b

        new_color = sRGBColor(rgb_r = r*self._r_adjust,
                              rgb_g = g*self._g_adjust,
                              rgb_b = b*self._b_adjust)

        return new_color.get_rgb_hex()
