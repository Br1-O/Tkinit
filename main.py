from src.tk.models.tk_window import Window
from src.tk.models.tk_label import Label

def main():
    mainWindow = Window.create(
        width= 1200, 
        height= 1000, 
        title= "Nueva", 
        bg_color= "#F0F0F0", 
        is_resizableX= True, 
        is_resizableY= True
    )
    label = Label.create(
        window= mainWindow,
        text= "Hola mundo",
        bg_color= "#333",
        font_color= "#FFF",
        font_size= 15,
        row= 1,
        rowspan= 2,
        column= 0,
        columnspan= 2,
        sticky="w"
    )
    print(mainWindow.geometry)

    mainWindow.run()

if __name__ == "__main__":
    main()