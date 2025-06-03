import tkinter as tk
from src.interfaces.Iwidget import Widget

class Scrollbar(Widget):

    def set(self):
        self._instance = tk.Scrollbar(
            self._window,
            orient=self._orient,
            command=self._command,
            relief=self._relief,
            borderwidth=self._borderwidth,
            cursor=self._cursor
        )

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Scrollbar widget with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === Scrollbar Options ===
            **orient** (str): Orientation of the scrollbar ("horizontal" or "vertical"). Default: "vertical".
            **command** (callable): Function to call when the scrollbar is moved.
            **relief** (str): Border style ("flat", "raised", "sunken", etc.). Default: "sunken".
            **borderwidth** (int): Border thickness in pixels. Default: 2.
            **cursor** (str): Cursor style when hovering over the scrollbar.

        === Positioning Options ===
            **display** (str): Layout manager to use. Options: "pack", "grid", "place". Default: "pack".

        --- pack ---
            **side** (str): Side to pack against ("top", "bottom", "left", "right"). Default: "right".
            **fill** (str): How to fill extra space ("x", "y", "both", None). Default: "y".
            **expand** (bool): Whether to expand and fill extra space. Default: False.
            **margin_x** (int): External padding on X axis. Default: 0.
            **margin_y** (int): External padding on Y axis. Default: 0.
            **padding_x** (int): Internal padding on X axis. Default: 0.
            **padding_y** (int): Internal padding on Y axis. Default: 0.

        --- grid ---
            **row** (int): Row index. Default: 0.
            **column** (int): Column index. Default: 0.
            **rowspan** (int): Row span. Default: 1.
            **columnspan** (int): Column span. Default: 1.
            **sticky** (str): Cell alignment. Default: None.
            **margin_x** (int): External padding on X axis. Default: 0.
            **margin_y** (int): External padding on Y axis. Default: 0.
            **padding_x** (int): Internal padding on X axis. Default: 0.
            **padding_y** (int): Internal padding on Y axis. Default: 0.

        --- place ---
            **x** (int): Absolute X position. Default: 0.
            **y** (int): Absolute Y position. Default: 0.
            **relx** (float): Relative X (0.0 to 1.0). Default: 0.0.
            **rely** (float): Relative Y (0.0 to 1.0). Default: 0.0.
            **relwidth** (float): Relative width. Default: None.
            **relheight** (float): Relative height. Default: None.
            **width** (int): Absolute width in pixels. Default: None.
            **height** (int): Absolute height in pixels. Default: None.
            **anchor** (str): Anchor reference point. Default: None.

        Returns:
            Scrollbar: An instance of the Scrollbar widget initialized and placed according to the parameters.
        """
        super().create(window, **kwargs)