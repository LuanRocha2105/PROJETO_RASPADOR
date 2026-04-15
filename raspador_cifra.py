import requests
from bs4 import BeautifulSoup
import unicodedata

BASE_URL = "https://www.cifraclub.com.br/"

def buscar_cifra(caminho):
    url = BASE_URL + caminho + "/"
    print(f"\nAcessando: {url}")

    resposta = requests.get(url)

    # Verificar se a página existe
    if resposta.status_code != 200:
        print(f"Erro ao acessar a página. Status: {resposta.status_code}")
        return

    soup = BeautifulSoup(resposta.text, "html.parser")
    
    titulo_tag  = soup.find("div", class_="g-1 g-fix cifra").find("h1") if soup.find("div", class_="g-1 g-fix cifra") else None 
    artista_tag = soup.find("h2").find("a")
 
    titulo  = titulo_tag.get_text(strip=True)  if titulo_tag  else "Título desconhecido"
    artista = artista_tag.get_text(strip=True) if artista_tag else "Artista desconhecido"

    print(f"Música : {titulo}")
    print(f"Artista: {artista}")
    print("\nCIFRA:\n")

    cifra_tag = soup.find("pre")
    linhas_cifra = []
    linha_atual  = ""
    tipo_atual   = "letra"

    for elemento in cifra_tag.children:
        if isinstance(elemento, str):
            partes = elemento.split("\n")
            for i, parte in enumerate(partes):
                linha_atual += parte
                if i < len(partes) - 1:
                    linhas_cifra.append({"tipo": tipo_atual, "texto": linha_atual})
                    print(linha_atual)
                    linha_atual = ""
                    tipo_atual  = "letra"
        elif elemento.name == "b":
            linha_atual += elemento.get_text()
            tipo_atual = "acorde"
 
    if linha_atual:
        linhas_cifra.append({"tipo": tipo_atual, "texto": linha_atual})
        print(linha_atual)
 
    print()


    


caminho = input("Digite o caminho da música (ex: jorge-ben-jor/take-it-easy): ")
buscar_cifra(caminho)
