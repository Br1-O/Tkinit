import tkinter as tk
from src.interfaces.Iwidget import Widget

class Menubutton(Widget):
    
    def set(self):
        self._instance = tk.Menubutton(
            self._window,
            text=self._text,
            bg=self._bg_color,
            fg=self._font_color,
            font=(self._font_family, self._font_size),
            menu=self._menu,
            relief=self._relief,
            borderwidth=self._borderwidth,
            cursor=self._cursor,
            state=self._state
        )

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Menubutton widget with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === General Options ===
            **text** (str): The text displayed on the Menubutton. Default: "".
            **bg_color** (str): Background color. Default: "#FFFFFF".
            **font_color** (str): Text color. Default: "#000000".
            **font_family** (str): Font family used. Default: "Arial".
            **font_size** (int): Font size in points. Default: 12.
            **state** (str): Widget state ("normal", "disabled"). Default: None.
            **cursor** (str): Cursor style on hover. Default: None.
            **relief** (str): Border style ("flat", "raised", "sunken", etc.). Default: None.
            **borderwidth** (int): Border thickness in pixels. Default: None.
            **menu** (tk.Menu): Menu to associate with this Menubutton. Default: None.

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
            **Menubutton**: An instance of the Menubutton widget initialized and placed according to the parameters.
        """
        widget = super().create(window, **kwargs)
        return widget