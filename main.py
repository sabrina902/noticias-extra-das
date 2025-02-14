import flet as ft
from banco import criar_tabela, carregar_noticias_do_banco
from extrator import buscar_e_salvar_noticias

def main(page: ft.Page):
    page.title = "Notícias Extraídas"
    page.theme_mode = "light"
    page.padding = 20
    page.window.width = 400
    page.window_height = 830

    titulo = ft.Text("Últimas Notícias", size=24, weight="bold")
    lista_noticias = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)

    def atualizar_noticias(_=None):
        buscar_e_salvar_noticias()
        noticias = carregar_noticias_do_banco()

        lista_noticias.controls.clear()
        for noticia, data in noticias:
            lista_noticias.controls.append(ft.Text(f"{noticia} - {data.strftime('%d/%m/%Y %H:%M')}"))

        page.update()

    btn_atualizar = ft.ElevatedButton("Atualizar Notícias", on_click=atualizar_noticias)
    page.add(titulo, btn_atualizar, lista_noticias)
    atualizar_noticias()

if __name__ == "__main__":
    criar_tabela()
    ft.app(target=main)
