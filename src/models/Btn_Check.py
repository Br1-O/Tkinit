import tkinter as tk
from src.interfaces.Iwidget import Widget

class Btn_check(Widget):

    def set(self):

        self._checked = self._kwargs.get("var", tk.IntVar(value=0))

        self._instance = tk.Checkbutton(
            self._window.instance,
            text=self._text,
            bg=self._bg_color,
            fg=self._font_color,
            font=(self._font_family, self._font_size),
            justify=self._justify,
            relief=self._relief,
            borderwidth=self._borderwidth,
            cursor=self._cursor,
            activebackground=self._activebackground,
            activeforeground=self._activeforeground,
            variable=self._checked,
            command=self._command,
            anchor=self._anchor,
            state=self._state,
            highlightthickness=self._highlightthickness,
            highlightbackground=self._highlightbackground,
            highlightcolor=self._highlightcolor,
            takefocus=self._takefocus,
            selectcolor=self._kwargs.get('selectcolor', None)
        )

        if self._default:
            self._instance.bind("<Return>", lambda event: self._command())

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Checkbutton widget with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === General Options ===
            **text** (str): The label shown next to the check button. Default: "".
            **bg_color** (str): Background color of the widget. Default: "#FFFFFF".
            **font_color** (str): Text color. Default: "#000000".
            **font_family** (str): Font family used for the text. Default: "Arial".
            **font_size** (int): Font size in points. Default: 12.
            **state** (str): Widget state ("normal", "disabled"). Default: "normal".
            **cursor** (str): Cursor style when hovering over the widget. Default: None.
            **justify** (str): Justification for multi-line text ("left", "center", "right"). Default: "left".
            **anchor** (str): Positioning of text inside the widget ("n", "e", "w", "center", etc.). Default: "w".
            **relief** (str): Border style ("flat", "raised", "sunken", "groove", "ridge"). Default: "flat".
            **borderwidth** (int): Thickness of the border. Default: 1.
            **takefocus** (bool | int): Determines whether the widget can take focus with Tab. Default: True.
            **command** (callable): Function to call when the checkbutton is toggled. Default: None.
            **var** (tk.IntVar): Variable tracking the state (checked/unchecked). Default: tk.IntVar(0).
            **selectcolor** (str): Color shown when the checkbox is selected. Default: system default.
            **activebackground** (str): Background color when the widget is active. Default: system default.
            **activeforeground** (str): Foreground (text) color when the widget is active. Default: system default.
            **highlightthickness** (int): Thickness of the focus highlight border. Default: 0.
            **highlightbackground** (str): Color of the focus highlight when the widget doesn't have focus. Default: system default.
            **highlightcolor** (str): Color of the focus highlight when the widget has focus. Default: system default.
            **default** (bool): If True, binds the <Return> key to trigger the command. Default: False.

        === Positioning Options ===
            **display** (str): Layout manager to use. Options: "pack", "grid", "place". Default: "pack".

        --- pack ---
            **side** (str): Side to pack against ("top", "bottom", "left", "right"). Default: "top".
            **fill** (str): How to fill extra space ("x", "y", "both", None). Default: None.
            **expand** (bool): Whether to expand and fill extra space. Default: False.
            **margin_x** (int): Horizontal external padding (padx). Default: 0.
            **margin_y** (int): Vertical external padding (pady). Default: 0.
            **padding_x** (int): Horizontal internal padding (ipadx). Default: 0.
            **padding_y** (int): Vertical internal padding (ipady). Default: 0.

        --- grid ---
            **row** (int): Row index in the grid. Default: 0.
            **column** (int): Column index in the grid. Default: 0.
            **rowspan** (int): Number of rows the widget spans. Default: 1.
            **columnspan** (int): Number of columns the widget spans. Default: 1.
            **sticky** (str): Alignment within the cell ("n", "s", "e", "w", or combination). Default: "".
            **margin_x** (int): Horizontal padding (padx). Default: 0.
            **margin_y** (int): Vertical padding (pady). Default: 0.
            **padding_x** (int): Horizontal internal padding (ipadx). Default: 0.
            **padding_y** (int): Vertical internal padding (ipady). Default: 0.

        --- place ---
            **x** (int): Absolute X coordinate. Default: 0.
            **y** (int): Absolute Y coordinate. Default: 0.
            **relx** (float): Relative X position (0.0 to 1.0). Default: 0.0.
            **rely** (float): Relative Y position (0.0 to 1.0). Default: 0.0.
            **relwidth** (float): Relative width (0.0 to 1.0). Default: None.
            **relheight** (float): Relative height (0.0 to 1.0). Default: None.
            **width** (int): Absolute width in pixels. Default: None.
            **height** (int): Absolute height in pixels. Default: None.
            **anchor** (str): Anchor point for widget positioning. Default: None.

        Returns:
            Checkbutton: An instance of the Checkbutton widget initialized and placed according to the parameters.
        """
        widget = super().create(window, **kwargs)
        return widget

