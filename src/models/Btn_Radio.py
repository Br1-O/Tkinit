import tkinter as tk
from src.interfaces.Iwidget import Widget

class Btn_Radio(Widget):

    #Dictionary with name and reference for all the variables associated with radio btns
    _variables = {}

    def check_existing_variables(self):
        cls = self.__class__
        self._var = self._kwargs.get("var", None)
        if self._var:
            not_found = True
            for var_name in cls._variables.keys():
                if self._var == var_name:
                    self._var = cls._variables[var_name]
                    not_found = False
            if not_found:
                new_var = tk.StringVar(value= self._var)
                cls._variables[self._var] = new_var
                self._var = new_var

    @classmethod
    def get_value(cls, var_name):
        result = None
        if var_name:
            for var in cls._variables.keys():
                if var_name == var:
                    result = (cls._variables[var_name]).get()
        return result
            

    def set(self):

        self.check_existing_variables()

        self._instance = tk.Radiobutton(
            self._window.instance,
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
            takefocus=self._takefocus,
            variable=self._var,
            value = self._value,
            command=self._command,
        )
        
        if self._default:
            self._instance.bind("<Return>", lambda event: self._command())

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Radiobutton widget with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === General Options ===
            **text** (str): The label shown next to the radio button. Default: "".
            **bg_color** (str): Background color. Default: "#FFFFFF".
            **font_color** (str): Text color. Default: "#000000".
            **font_family** (str): Font family used. Default: "Arial".
            **font_size** (int): Font size in points. Default: 12.
            **state** (str): Widget state ("normal", "disabled"). Default: None.
            **cursor** (str): Cursor style on hover. Default: None.
            **justify** (str): Justification for multi-line text ("left", "center", "right"). Default: None.
            **anchor** (str): Anchor position inside the widget ("n", "e", "center", etc.). Default: None.
            **relief** (str): Border style ("flat", "raised", "sunken", etc.). Default: None.
            **borderwidth** (int): Border thickness in pixels. Default: None.
            **takefocus** (bool | int): Whether the widget can take focus via Tab. Default: None.
            **command** (callable): Function to call when the radiobutton is selected. Default: None.

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
            **Radiobutton**: An instance of the Radiobutton widget initialized and placed according to the parameters.
        """
        widget = super().create(window, **kwargs)
        return widget