from src.models import *

def main():

    def value(var_name):
        print(Btn_Radio.get_value(var_name))

    mainWindow = Window.create(
        width= 1200, 
        height= 1000, 
        title= "Nueva", 
        bg_color= "#F0F0F0", 
        is_resizableX= True, 
        is_resizableY= True
    )
    frame = Frame.create(
        window= mainWindow,
        bg_color = "#AAAAAA",
        cursor = "hand2",
        borderwidth = 2,
        relief = "raised",
        display = "place",
        relx = 0.5,
        rely = 0.5
    )

    radio = Btn_Radio.create(
        window= frame,
        text="patata",
        command=lambda: value("frutas"),
        bg_color="#eee",
        font_color="#333",
        font_size=14,
        display="grid",
        row=2,
        column = 1,
        value = "patata",
        var = "frutas"
    )
    radio2 = Btn_Radio.create(
        window= frame,
        text="papa",
        command=lambda: value("frutas"),
        bg_color="#eee",
        font_color="#333",
        font_size=14,
        display="grid",
        row=3,
        column = 1,
        value = "papa",
        var = "frutas"
    )
    radio7 = Btn_Radio.create(
        window= frame,
        text="lechuga",
        command=lambda: value("verduras"),
        bg_color="#eee",
        font_color="#333",
        font_size=14,
        display="grid",
        row=8,
        column = 1,
        value = "lechuga",
        var = "verduras"
    )
    radio8 = Btn_Radio.create(
        window= frame,
        text="batata",
        command=lambda: value("verduras"),
        bg_color="#eee",
        font_color="#333",
        font_size=14,
        display="grid",
        row=9,
        column = 1,
        value = "batata",
        var = "verduras"
    )
    check = Btn_check.create(
        window= frame,
        text="Aceptar términos",
        command=lambda: value(),
        bg_color="#eee",
        font_color="#333",
        font_size=14,
        display="grid",
        row=0,
        column = 1,
    )

    mainWindow.run()

if __name__ == "__main__":
    main()