import tkinter as tk
from src.tk.interfaces.Itk_widget import IWidget

class Window(IWidget):
    """
    Methods:
        create --- creates a new window
        get_instance --- gets reference to use as param in widgets
        run --- runs the window (execute after including all widgets of a window)
    """
    _instance = None
    _title = "Nueva ventana"
    _bg_color = "#FFF"
    _geometry = ""
    _is_resizable = ""

    #Constructor
    def __init__(self, width = 800, height = 800, title = "Nueva Ventana", bg_color = "#FFF", is_resizableX = False, is_resizableY = False):
        self.geometry = (width, height)
        self.is_resizable = (is_resizableX, is_resizableY)
        self._title = title
        self._bg_color = bg_color
        
    #Geometry property
    @property
    def geometry(self):
        return self._geometry
    
    #is_resizable property
    @property
    def is_resizable(self):
        return self._is_resizable
    
    @property
    def instance(self):
        """
            Returns the tk instance of the window for widgets
        """
        return self._instance
    
    @geometry.setter
    def geometry(self, value):
        self._geometry = f"{value[0]}x{value[1]}"

    @is_resizable.setter
    def is_resizable(self, value):
        self._is_resizable = value
    
    #sets the properties for the window
    def set(self):
        self._instance = tk.Tk()
        self._instance.title(self._title)
        self._instance.geometry(self._geometry)
        self._instance.configure(bg=self._bg_color)
        self._instance.resizable(*self._is_resizable)
    
    #Method to create window
    @classmethod
    def create(cls, **kwargs):
        """
        Params:
            width (int) ---- DEF="800".
            height (str) ---- DEF="800".
            title (str) ---- DEF="Nueva ventana".
            bg_color (str) ---- DEF="#FFF".
            is_resizableX (bool) ---- DEF=False.
            is_resizableY (bool) ---- DEF=False.
        """
        window = cls(**kwargs)
        window.set()
        return window
    
    #executes mainloop
    def run(self):
        """
            Executes main loop of the window
        """
        (self._instance).mainloop()
        return True

    