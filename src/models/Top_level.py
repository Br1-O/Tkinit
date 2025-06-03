import tkinter as tk
from src.interfaces.Iwidget import Widget

class Toplevel(Widget):

    def set(self):
        self._instance = tk.Toplevel(self._window)
        if self._title:
            self._instance.title(self._title)
        if self._iconbitmap:
            self._instance.iconbitmap(self._iconbitmap)
        self._instance.configure(
            bg=self._bg_color,
            cursor=self._cursor
        )
        self._instance.resizable(*self._resizable)
        self._instance.minsize(*self._minsize)
        self._instance.maxsize(*self._maxsize)

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Toplevel window with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === General Options ===
            **title** (str): The window title shown in the title bar. Default: "".
            **iconbitmap** (str): Path to the icon bitmap file for the window. Default: None.
            **bg_color** (str): Background color of the window. Default: "#FFFFFF".
            **cursor** (str): Cursor style when hovering over the window. Default: None.
            **resizable** (tuple[bool, bool]): Allow window resizing in (width, height). Default: (True, True).
            **minsize** (tuple[int, int]): Minimum window size as (width, height). Default: (1, 1).
            **maxsize** (tuple[int, int]): Maximum window size as (width, height). Default: (max int, max int).

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
            **Toplevel**: An instance of the Toplevel window initialized and placed according to the parameters.
        """
        widget = super().create(window, **kwargs)
        return widget