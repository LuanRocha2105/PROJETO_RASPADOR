import requests
from bs4 import BeautifulSoup

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

    titulo = soup.find("div", class_="g-1 g-fix cifra").find("h1")
    artista = soup.find("h2").find("a") 
    
    if titulo:
        print(f"Música : {titulo.get_text(strip=True)}")
    else:
        print("Título não encontrado.")
    
    if artista:
        print(f"Artista: {artista.get_text(strip=True)}")
    else:
        print("Artista não encontrado.")

    print("\nCIFRA:\n")   

    cifra_tag = soup.find("pre")

    for elemento in cifra_tag.children:
        # Elemento de texto puro = letra da música
        if isinstance(elemento, str):
            print(elemento, end="")
        # Tag <b> = acorde
        elif elemento.name == "b":
            print(elemento.get_text(), end="")
 
    print()



    


caminho = input("Digite o caminho da música (ex: jorge-ben-jor/take-it-easy): ")
buscar_cifra(caminho)
