import tkinter as tk
from src.interfaces.Iwidget import Widget

class Label(Widget):

    def set(self):
        self._instance = tk.Label(
            self._window,
            text=self._text,
            bg=self._bg_color,
            fg=self._font_color,
            font=(self._font_family, self._font_size),
            justify=self._justify,
            anchor=self._anchor,
            state=self._state,
            cursor=self._cursor,
            relief=self._relief,
            borderwidth=self._borderwidth,
            wraplength=self._wraplength,
            takefocus=self._takefocus
        )

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Label widget with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === General Options ===
            **text** (str): The text displayed in the label. Default: "".
            **bg_color** (str): Background color. Default: "#FFFFFF".
            **font_color** (str): Text color. Default: "#000000".
            **font_family** (str): Font family used. Default: "Arial".
            **font_size** (int): Font size in points. Default: 12.
            **state** (str): Widget state ("normal", "disabled"). Default: None.
            **cursor** (str): Cursor style on hover. Default: None.
            **justify** (str): Text justification ("left", "center", "right"). Default: None.
            **anchor** (str): Anchor position for content inside the label (e.g., "n", "e", "center"). Default: None.
            **relief** (str): Border style ("flat", "sunken", "raised", etc.). Default: None.
            **borderwidth** (int): Border width in pixels. Default: None.
            **wraplength** (int): Maximum line width in pixels before wrapping text. Default: None.
            **takefocus** (bool | int): Whether the widget can take focus. Default: None.

        === Positioning Options ===
            **display** (str): Layout manager to use. Options: "pack", "grid", "place". Default: "pack".

        --- pack ---
            **side** (str): Side to pack against ("top", "bottom", "left", "right"). Default: "top".
            **fill** (str): How to fill extra space ("x", "y", "both", None). Default: None.
            **expand** (bool): Whether to expand and fill any extra space. Default: False.
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
            **Label**: An instance of the Label widget initialized and placed according to the parameters.
        """
        return super().create(window, **kwargs)
