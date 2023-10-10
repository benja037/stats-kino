import flet as ft
from bs4 import BeautifulSoup
import requests


r = requests.get('https://chileresultados.com/kino/ultimosorteo')
print("==========================================================")
print(r.status_code)
print("==========================================================")
print(r.headers['content-type'])
print("==========================================================")
print(r.encoding)
print("==========================================================")
texto = r.text
print(texto)
print("==========================================================")
numeros = []
soup = BeautifulSoup(texto, "lxml")
filas_html = soup.find_all("ul", class_="lstPe")
for fila_html in filas_html:
    lista_li = fila_html.find_all("li")
    for numero_li in lista_li:
        numero = numero_li.find("span", class_="bola").get_text()
        numeros.append(numero)


print(numeros)
print("==========================================================")


def main(page: ft.Page):
    page.add(ft.Text("Hola Flet"))
    page.add(ft.Text(numeros))


ft.app(main, view=ft.WEB_BROWSER)
