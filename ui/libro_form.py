import flet as ft

def libro_form(regresar):
    titulo_input = ft.TextField(
        label = "Titulo del libro:",
        width = 400
    )
    
    autor_input = ft.TextField(
        label = "Autor del libro:",
        width = 400
    )
    
    isbn_input = ft.TextField (
        label = "ISBN del libro:",
        width = 400
    )
    
    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN,
    )

    def guardar_libro(e):
        titulo = titulo_input.value
        autor = autor_input.value
        isbn = isbn_input.value
        
        if not titulo == "" or autor == "" or  isbn == "":
            mensaje.value = "Por favor, complete todos los campos."
            mensaje.color = ft.Colors.RED
        else:
            mensaje.value = f"Libro '{titulo}' listo para insertar"
            print(f"Titulo: {titulo}, Autor: {autor}, ISBN: {isbn}")
            mensaje.color = ft.Colors.GREEN
            
            # Limpiar los campos después de guardar
            titulo_input.value = ""
            autor_input.value = ""
            isbn_input.value = ""
        
        e.page.update()

    return ft.Container (
        padding = 30,
        content = ft.Column (
            controls = [
                ft.Text (
                    "Registrar nuevo libro",
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),
                
                ft.Text (
                    "Captura los datos básicos del libro",
                    size = 24,
                    color = ft.Colors.BLUE_GREY_600
                ),
                
                titulo_input,
                autor_input,
                isbn_input,
                
                ft.Row (
                        controls = [
                            ft.ElevatedButton (
                                "Registrar libro",
                                icon = ft.Icons.SAVE,
                                on_click = guardar_libro
                            ),
                            ft.OutlinedButton (
                                "Regresar",
                                icon = ft.Icons.ARROW_BACK,
                                on_click = lambda e: regresar()
                            )
                        ]
                    ),
                
                

                mensaje
            ],
            spacing = 15
        )
    )