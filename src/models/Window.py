import tkinter as tk
from src.interfaces.Iwindow import IWindow

class Window(IWindow):
    """
    Methods:
        create --- creates a new window
        get_instance --- gets reference to use as param in widgets
        run --- runs the window (execute after including all widgets of a window)
    """
    
    #sets the properties for the window
    def set(self):
        self._instance = tk.Tk()
        self._instance.title(self._title)
        self._instance.geometry(self._geometry)
        self._instance.configure(bg=self._bg_color, menu = self._menu)
        self._instance.resizable(*self._is_resizable)    