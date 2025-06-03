import tkinter as tk
from src.interfaces.Iwidget import Widget

class Menu(Widget):

    def set(self):
        self._instance = tk.Menu(
            self._window,
            tearoff=self._tearoff,
            bg=self._bg_color,
            fg=self._font_color,
            font=(self._font_family, self._font_size),
            cursor=self._cursor,
            postcommand=self._postcommand
        )

    @classmethod
    def create(cls, window, **kwargs):
        """
        Creates an instance of the Menu widget with the specified options.

        Parameters:
            **window** (tk.Tk | tk.Toplevel): The parent window.

        === General Options ===
            **tearoff** (bool): Whether the menu can be torn off into a separate window. Default: True.
            **bg_color** (str): Background color. Default: "#FFFFFF".
            **font_color** (str): Text color. Default: "#000000".
            **font_family** (str): Font family used. Default: "Arial".
            **font_size** (int): Font size in points. Default: 12.
            **cursor** (str): Cursor style when hovering over menu items. Default: None.
            **postcommand** (callable): A function that is called right before the menu is shown. Default: None.

        Note:
            The Menu widget does not support geometry management like pack, grid, or place. It must be attached
            to another widget such as a Menubutton or used as a toplevel menu via `window.config(menu=menu_instance)`.

        Returns:
            **Menu**: An instance of the Menu widget.
        """
        super().create(window, **kwargs)