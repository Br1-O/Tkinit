import tkinter as tk
from src.tk.interfaces.Itk_widget import IWidget

class Label(IWidget):
    
    _instance = ""
    _window = None
    _text = "1"
    _bg_color = "#FFF"
    _font_color = "#FFF"
    _font_family = ""
    _font_size = 14
    _font = ""
    _row = 0
    _column = 0
    _rowspan = 1
    _columnspan = 1
    _margin_x = 1
    _margin_y = 1
    _padding_x = 1
    _padding_y = 1
    _sticky = "w"

    #Constructor
    def __init__(    
        self,
        window,
        text="",
        bg_color="#FFF",
        font_color="#000",
        font_family="Arial",
        font_size=14,
        row=0,
        column=0,
        rowspan=1,
        columnspan=1,
        margin_x=1,
        margin_y=1,
        padding_x=1,
        padding_y=1,
        sticky="w",):
        self._window = window
        self._text = text
        self._bg_color = bg_color
        self._font_color = font_color
        self._font_family = font_family
        self._font_size = font_size
        self._row = row
        self._column = column
        self._rowspan = rowspan
        self._columnspan = columnspan
        self._margin_x = margin_x
        self._margin_y = margin_y
        self._padding_x = padding_x
        self._padding_y = padding_y
        self._sticky = sticky

    #Geometry property
    @property
    def font(self):
        return self._font
    
    @font.setter
    def font(self, value):
        self._font = value

    #Method to get the tk instance of the widget
    @property
    def instance(self):
        return self._instance
    
    #sets the properties for the label
    def set(self):
        self._instance = tk.Label(
            self._window.instance,
            text=self._text,
            bg=self._bg_color,
            fg=self._font_color,
            font=(self._font_family, self._font_size)
        )

    #places the label in the window
    def place_grid(self):
        (self._instance).grid(row = self._row, column = self._column, rowspan = self._rowspan, columnspan= self._columnspan, padx = self._margin_x, pady = self._margin_y, ipadx = self._padding_x, ipady = self._padding_y, sticky = self._sticky)
    
    #Method to create window
    @classmethod
    def create(cls, **kwargs):
        """
        Params:
            window (Window)
            text (str) ---- DEF="Label".
            bg_color (str) ---- DEF="#FFF".
            font_color (str) ---- DEF="#000".
            font_family (str) ---- DEF="Arial".
            font_size (int) ---- DEF=12.
            row (int) ---- DEF=0.
            column (int) ---- DEF=0.
            rowspan (int) ---- DEF=1.
            columnspan (int) ---- DEF=1.
            margin_x (int) ---- DEF=1.
            margin_y (int) ---- DEF=1.
            padding_x (int) ---- DEF=1.
            padding_y (int) ---- DEF=1.
            sticky (str) ---- DEF=w.
            ...
        """
        label = cls(**kwargs)
        label.set()
        label.place_grid()
        return label