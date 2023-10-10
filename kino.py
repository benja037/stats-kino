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
numeros2 = soup.find_all(
    "span", class_="badge rounded-pill bg-warning text-dark")
for elemento in numeros2:
    numerito = elemento.get_text()
    numeros.append(numerito)
print(numeros2)
resultados_kino = numeros[0:14]
resultados_rekino = numeros[14:28]
resultados_chanchito = numeros[28:42]
resultados_combo = numeros[42:56]
resultados_chaojefe1 = numeros[56:70]
resultados_chaojefe2 = numeros[70:84]
resultados_chaojefe3 = numeros[84:98]


print(numeros)
print("==========================================================")


def main(page: ft.Page):
    page.add(ft.Text("Hola Flet"))
    page.add(ft.Text(numeros))
    page.add(ft.Text("Resultados Kino"))
    page.add(ft.Text(resultados_kino))
    page.add(ft.Text("Resultados Rekino"))
    page.add(ft.Text(resultados_rekino))
    page.add(ft.Text("Resultados chanchito"))
    page.add(ft.Text(resultados_chanchito))
    page.add(ft.Text("Resultados Combo Marraqueta"))
    page.add(ft.Text(resultados_combo))
    page.add(ft.Text("Resultados Chao Jefe 1 millon"))
    page.add(ft.Text(resultados_chaojefe1))
    page.add(ft.Text("Resultados Chao Jefe 2 millones"))
    page.add(ft.Text(resultados_chaojefe2))
    page.add(ft.Text("Resultados Chao Jefe 3 millones"))
    page.add(ft.Text(resultados_chaojefe3))


ft.app(main, view=ft.WEB_BROWSER)
