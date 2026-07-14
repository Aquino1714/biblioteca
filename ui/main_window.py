import flet as ft

def main_window(page: ft.Page):
    page.Title = "Biblioteca Universitaria"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.WHITE

    # Ejemplo de witget
    titulo = ft.Text("Sistema de Biblioteca Universitaria",
        size = 24,
        weight = ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Selecciona una opcion del menu",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    # Widget de contenido
    contenido = ft.Container (
        content = ft.Column (
            controls = [
                titulo,
                subtitulo
            ],
            spacing = 10
        ),
        padding = 30,
        expand = True,
        bgcolor = ft.Colors.WHITE
    )

    manu_lateral = ft.Container (
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_100,
        padding = 20,
        content = ft.Column (
            controls = [
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.BLUE_GREY_600
                ),
                ft.Text (
                    "Sistema de gestión",
                    size = 12,
                    color = ft.Colors.BLUE_GREY_100
                ),
                
                ft.Divider (color = ft.Colors.BLUE_GREY_700),
                
                ft.ElevatedButton (
                    "libros",
                    icon = ft.Icons.BOOK,
                    width = 180,
                ),
                ft.ElevatedButton (
                    "usuarios",
                    icon = ft.Icons.PERSON_OUTLINE,
                    width = 180,
                ),
                ft.ElevatedButton (
                    "prestamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180,
                ),
                ft.ElevatedButton (
                    "devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180,
                ),
            ],
            spacing = 15
        )
    )

    # Agregar los widgets al contenedor principal
    layout = ft.Row (
        controls = [
            manu_lateral,
            contenido
        ],
        expand = True
    )

    page.add(layout)