"""
Class for adjusting rgb colors
"""

from colormath.color_objects import sRGBColor
import numpy as np

class ColorAdjuster:

    def __init__(self, r_adjust, g_adjust, b_adjust):
        """Initialize a ColorAdjuster object that will adjust r, g, b by the given amounts
        """
        self._adjust = np.array([r_adjust, g_adjust, b_adjust])

    def adjust_hex(self, orig_hex):
        """Given an original hex value, return the adjusted value

        If the adjusted value would have r, g, or b exceeding 1 (i.e., 255), raises an
        exception.
        """

        orig_color = sRGBColor.new_from_rgb_hex(orig_hex)

        orig_rgb = np.array(orig_color.get_value_tuple())
        new_rgb = orig_rgb * self._adjust

        max_rgb = np.max(new_rgb)
        if max_rgb > 1:
            raise RuntimeError("Adjusted rgb has a value exceeding 1")

        new_color = sRGBColor(rgb_r = new_rgb[0],
                              rgb_g = new_rgb[1],
                              rgb_b = new_rgb[2])

        return new_color.get_rgb_hex()
