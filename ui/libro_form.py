import flet as ft

def libro_form():
    
    
    
    
    
    
    mensaje = ft.Text (
        "",
        color = ft.Colors.GREEN
    )
    
    return ft.Container (
        padding = 30,
        content = ft.Column (
            controls = [
                ft.Text (
                    "Registrar libro",
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),
                
                ft.Text (
                    "Capture los datos básicos del libro",
                    size = 14,
                    color = ft.Colors.BLUE_GREY_600
                ),
                
                titulo_input,
                autor_input,
                isbn_input,
                
                ft.ElevatedButton (
                    "Registrar libr",
                    icon = ft-Icons.SAVE,
                    
                )
            ]
        )
    )