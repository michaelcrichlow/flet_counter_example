import flet as ft
from flet import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Flet Counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"

    text_number = ft.TextField(
        value="10", text_align=ft.TextAlign.RIGHT, width=100)

    def increment(e: ControlEvent):
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    def decrement(e: ControlEvent):
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def restore_default_value(e: ControlEvent):
        text_number.value = "0"
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=decrement),
            text_number,
            ft.IconButton(ft.icons.ADD, on_click=increment)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.TextButton(text="RESET", on_click=restore_default_value)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
