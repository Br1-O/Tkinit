from abc import ABC, abstractmethod

class Widget(ABC):
    def __init__(self, window, **kwargs):
        self._window = window
        self._kwargs = kwargs
        self._instance = None

        # Propiedades comunes
        self._text = kwargs.get('text', '')
        self._bg_color = kwargs.get('bg_color', '#FFFFFF')
        self._font_color = kwargs.get('font_color', '#000000')
        self._font_family = kwargs.get('font_family', 'Arial')
        self._font_size = kwargs.get('font_size', 12)
        self._width = kwargs.get('width', None)
        self._height = kwargs.get('height', None)  # puede ser píxeles o filas (según widget)
        self._cursor = kwargs.get('cursor', None)
        self._relief = kwargs.get('relief', None)
        self._borderwidth = kwargs.get('borderwidth', None)
        self._state = kwargs.get('state', None)
        self._takefocus = kwargs.get('takefocus', None)
        self._highlightthickness = kwargs.get('highlightthickness', None)
        self._highlightbackground = kwargs.get('highlightbackground', None)
        self._highlightcolor = kwargs.get('highlightcolor', None)

        # Propiedades de posicionamiento
        self._display = kwargs.get('display', 'pack')
        self._side = kwargs.get('side', 'top')
        self._fill = kwargs.get('fill', None)
        self._expand = kwargs.get('expand', False)
        self._x = kwargs.get('x', 0)
        self._y = kwargs.get('y', 0)
        self._relx = kwargs.get('relx', 0.0)
        self._rely = kwargs.get('rely', 0.0)
        self._relwidth = kwargs.get('relwidth', None)
        self._relheight = kwargs.get('relheight', None)
        self._anchor = kwargs.get('anchor', None)
        self._row = kwargs.get('row', 0)
        self._column = kwargs.get('column', 0)
        self._rowspan = kwargs.get('rowspan', 1)
        self._columnspan = kwargs.get('columnspan', 1)
        self._sticky = kwargs.get('sticky', None)
        self._margin_x = kwargs.get('margin_x', 0)
        self._margin_y = kwargs.get('margin_y', 0)
        self._padding_x = kwargs.get('padding_x', 0)
        self._padding_y = kwargs.get('padding_y', 0)

        # Propiedades específicas
        self._justify = kwargs.get('justify', None)
        self._wraplength = kwargs.get('wraplength', None)
        self._underline = kwargs.get('underline', None)
        self._image = kwargs.get('image', None)
        self._compound = kwargs.get('compound', None)
        self._show = kwargs.get('show', None)
        self._insertbackground = kwargs.get('insertbackground', None)
        self._selectbackground = kwargs.get('selectbackground', None)
        self._selectforeground = kwargs.get('selectforeground', None)
        self._from_ = kwargs.get('from_', 0)
        self._to = kwargs.get('to', 100)
        self._orient = kwargs.get('orient', 'horizontal')
        self._length = kwargs.get('length', 100)
        self._tickinterval = kwargs.get('tickinterval', None)
        self._resolution = kwargs.get('resolution', 1)
        self._increment = kwargs.get('increment', 1)
        self._format = kwargs.get('format', None)
        self._wrap = kwargs.get('wrap', False)
        self._command = kwargs.get('command', None)
        self._menu = kwargs.get('menu', None)
        self._tearoff = kwargs.get('tearoff', True)
        self._postcommand = kwargs.get('postcommand', None)
        self._scrollregion = kwargs.get('scrollregion', None)
        self._xscrollcommand = kwargs.get('xscrollcommand', None)
        self._yscrollcommand = kwargs.get('yscrollcommand', None)
        self._selectmode = kwargs.get('selectmode', 'browse')
        self._activestyle = kwargs.get('activestyle', 'dotbox')
        self._exportselection = kwargs.get('exportselection', True)
        self._title = kwargs.get('title', None)
        self._iconbitmap = kwargs.get('iconbitmap', None)
        self._resizable = kwargs.get('resizable', (True, True))
        self._minsize = kwargs.get('minsize', (0, 0))
        self._maxsize = kwargs.get('maxsize', (0, 0))
        self._var = kwargs.get('variable', None)
        self._value = kwargs.get('value', None)

        # Nuevas propiedades añadidas
        # Para Entry: validación
        self._validate = kwargs.get('validate', None)  # e.g. 'focus', 'key', 'all'
        self._validatecommand = kwargs.get('validatecommand', None)
        self._invalidcommand = kwargs.get('invalidcommand', None)

        # Eventos bindables: dict {event:str : handler:callable}
        self._bindings = kwargs.get('bindings', {})

        # Colores activos para botones o widgets interactivos
        self._activebackground = kwargs.get('activebackground', None)
        self._activeforeground = kwargs.get('activeforeground', None)

        # Altura para widgets que lo interpretan como filas visibles (Listbox, Text)
        self._visible_height = kwargs.get('visible_height', None)

        # Propiedades para Scale
        self._sliderlength = kwargs.get('sliderlength', None)
        self._showvalue = kwargs.get('showvalue', True)

        # Para Button: si es default (responde a Enter)
        self._default = kwargs.get('default', False)

        # Tooltip (no nativo, queda para implementar aparte)
        self._tooltip = kwargs.get('tooltip', None)

    @abstractmethod
    def set(cls):
        pass

    def place_in(self):
        if self._display == "grid":
            self._instance.grid(
                row=self._row,
                column=self._column,
                rowspan=self._rowspan,
                columnspan=self._columnspan,
                padx=self._margin_x,
                pady=self._margin_y,
                ipadx=self._padding_x,
                ipady=self._padding_y,
                sticky=self._sticky
            )
        elif self._display == "place":
            self._instance.place(
                x=self._x,
                y=self._y,
                width=self._width,
                height=self._height,
                relx=self._relx,
                rely=self._rely,
                relwidth=self._relwidth,
                relheight=self._relheight,
                anchor=self._anchor
            )
        else:
            self._instance.pack(
                side=self._side,
                fill=self._fill,
                expand=self._expand,
                padx=self._margin_x,
                pady=self._margin_y,
                ipadx=self._padding_x,
                ipady=self._padding_y
            )
        # Aplicar bindings si existen
        for event, handler in self._bindings.items():
            self._instance.bind(event, handler)

    @classmethod
    def create(cls, window, **kwargs):
        """
        Params:
            window (Window)
            text (str) ---- DEF="Label".
            bg_color (str) ---- DEF="#FFF".
            font_color (str) ---- DEF="#000".
            font_family (str) ---- DEF="Arial".
            font_size (int) ---- DEF=14.
            state (str) ---- DEF="normal".
            cursor (str) ---- DEF="arrow".
            justify (str) ---- DEF="left".
            anchor (str) ---- DEF="nw".
            command (callable | None) ---- DEF=None. (for buttons)
            relief (str) ---- DEF="flat".
            borderwidth (int) ---- DEF=0.
            wraplength (int) ---- DEF=0.
            takefocus (int | bool) ---- DEF=1.

            //////////////////////////////////
            DISPLAY OPTIONS
            display (str) ---- DEF="pack". (Values: "pack", "grid", "place")
            //////////////////////////////////

            (FOR DISPLAY = "grid")
            row (int) ---- DEF=0.
            column (int) ---- DEF=0.
            rowspan (int) ---- DEF=1.
            columnspan (int) ---- DEF=1.
            sticky (str) ---- DEF="w".
            margin_x (int) ---- DEF=1.
            margin_y (int) ---- DEF=1.
            padding_x (int) ---- DEF=1.
            padding_y (int) ---- DEF=1.

            //////////////////////////////////
            (FOR DISPLAY = "place")
            x (int) ---- DEF=0.
            y (int) ---- DEF=0.
            width (int) ---- DEF=1.
            height (int) ---- DEF=1.
            relx (float) ---- DEF=0.5.
            rely (float) ---- DEF=0.5.
            relwidth (float) ---- DEF=0.5.
            relheight (float) ---- DEF=0.5.
            anchor (str) ---- DEF="nw".

            //////////////////////////////////
            (FOR DISPLAY = "pack")
            side (str) ---- DEF="top".
            fill (str) ---- DEF="x".
            expand (bool) ---- DEF=True.
            margin_x (int) ---- DEF=1.
            margin_y (int) ---- DEF=1.
            padding_x (int) ---- DEF=1.
            padding_y (int) ---- DEF=1.

            //////////////////////////////////
            VALIDATION (for Entry widgets)
            validate (str | None) ---- DEF=None. Options: "focus", "key", "all".
            validatecommand (callable | None) ---- DEF=None. Function to validate input.
            invalidcommand (callable | None) ---- DEF=None. Called when validation fails.

            //////////////////////////////////
            EVENTS
            bindings (dict) ---- DEF={}. Dict of event-string keys and handler functions as values, e.g. {"<Button-1>": handler}.

            //////////////////////////////////
            INTERACTIVE COLORS (for buttons and similar)
            activebackground (str | None) ---- DEF=None. Background color when active.
            activeforeground (str | None) ---- DEF=None. Foreground color when active.

            //////////////////////////////////
            WIDGET SPECIFIC
            visible_height (int | None) ---- DEF=None. Number of visible rows (for Listbox, Text).
            sliderlength (int | None) ---- DEF=None. Length of the slider (for Scale).
            showvalue (bool) ---- DEF=True. Whether to show the value label (for Scale).
            default (bool) ---- DEF=False. If True, button acts as default button (Enter key).

            //////////////////////////////////
            TOOLTIP
            tooltip (str | None) ---- DEF=None. Text to show on tooltip (implementation required).
        """
        widget = cls(window, **kwargs)
        widget.set()
        widget.place_in()
        return widget