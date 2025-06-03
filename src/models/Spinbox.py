import tkinter as tk
from src.interfaces.Iwidget import Widget

class Spinbox(Widget):

    def set(self):
        self._instance = tk.Spinbox(
            self._window,
            from_=self._from_,
            to=self._to,
            increment=self._increment,
            format=self._format,
            font=(self._font_family, self._font_size),
            relief=self._relief,
            borderwidth=self._borderwidth,
            state=self._state,
            cursor=self._cursor,
            takefocus=self._takefocus,
            command=self._command
        )

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Spinbox widget with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === General Options ===
            **from_** (float | int): Starting value. Required.
            **to** (float | int): Ending value. Required.
            **increment** (float): Step value. Default: 1.
            **format** (str): Format string for display. Example: "%.2f". Default: None.
            **font_family** (str): Font family used. Default: "Arial".
            **font_size** (int): Font size in points. Default: 12.
            **state** (str): Widget state ("normal", "readonly", "disabled"). Default: "normal".
            **cursor** (str): Cursor style on hover. Default: None.
            **relief** (str): Border style ("flat", "raised", "sunken", etc.). Default: "sunken".
            **borderwidth** (int): Border thickness in pixels. Default: 2.
            **takefocus** (bool | int): Whether the widget can take focus via Tab. Default: True.
            **command** (callable): Function to call when the value is changed. Default: None.

        === Positioning Options ===
            **display** (str): Layout manager to use. Options: "pack", "grid", "place". Default: "pack".

        --- pack ---
            **side** (str): Side to pack against ("top", "bottom", "left", "right"). Default: "top".
            **fill** (str): How to fill extra space ("x", "y", "both", None). Default: None.
            **expand** (bool): Whether to expand and fill extra space. Default: False.
            **margin_x** (int): Horizontal margin (external padding). Default: 0.
            **margin_y** (int): Vertical margin (external padding). Default: 0.
            **padding_x** (int): Horizontal internal padding. Default: 0.
            **padding_y** (int): Vertical internal padding. Default: 0.

        --- grid ---
            **row** (int): Row index in the grid. Default: 0.
            **column** (int): Column index in the grid. Default: 0.
            **rowspan** (int): Number of rows the widget spans. Default: 1.
            **columnspan** (int): Number of columns the widget spans. Default: 1.
            **sticky** (str): Alignment within the cell ("n", "s", "e", "w", or combination). Default: None.
            **margin_x** (int): Horizontal margin. Default: 0.
            **margin_y** (int): Vertical margin. Default: 0.
            **padding_x** (int): Horizontal internal padding. Default: 0.
            **padding_y** (int): Vertical internal padding. Default: 0.

        --- place ---
            **x** (int): Absolute X coordinate. Default: 0.
            **y** (int): Absolute Y coordinate. Default: 0.
            **relx** (float): Relative X position (0.0 to 1.0). Default: 0.0.
            **rely** (float): Relative Y position (0.0 to 1.0). Default: 0.0.
            **relwidth** (float): Relative width (0.0 to 1.0). Default: None.
            **relheight** (float): Relative height (0.0 to 1.0). Default: None.
            **width** (int): Absolute width in pixels. Default: None.
            **height** (int): Absolute height in pixels. Default: None.
            **anchor** (str): Reference anchor point. Default: None.

        Returns:
            **Spinbox**: An instance of the Spinbox widget initialized and placed according to the parameters.
        """
        widget = super().create(window, **kwargs)
        return widget