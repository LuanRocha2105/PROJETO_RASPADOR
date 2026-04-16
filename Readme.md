# Raspador de Cifras

Ferramenta de linha de comando que busca cifras no [Cifra Club](https://www.cifraclub.com.br/) e gera um PDF formatado com acordes destacados em azul.

# Funcionalidades

 Busca cifras diretamente no Cifra Club via raspagem de dados


# Requisitos

 Dependências listadas em `requirements.txt`


# Instalação


- Clone o repositório

git clone https://github.com/seu-usuario/raspador-cifras.git
cd raspador-cifras

- (Recomendado) Crie um ambiente virtual

python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

- Instale as dependências
pip install -r requirements.txt


# Como usar

python raspador_cifra.py


O programa solicitará o nome do artista e da música:

```
Digite o nome do artista (ex: Legião Urbana): Legião Urbana
Digite o nome da música  (ex: Tempo Perdido): Tempo Perdido

Caminho gerado: legiao-urbana/tempo-perdido
Acessando: https://www.cifraclub.com.br/legiao-urbana/tempo-perdido/

Música : Tempo Perdido
Artista: Legião Urbana

CIFRA:
...

PDF gerado com sucesso: legiao-urbana_tempo-perdido.pdf
```

O arquivo PDF será salvo no diretório atual com o nome no formato `artista_musica.pdf`.



# Bibliotecas utilizadas

| Biblioteca       | Uso                              |
|------------------|----------------------------------|
| `requests`       | Requisições HTTP                 |
| `beautifulsoup4` | Parsing e extração do HTML       |
| `reportlab`      | Geração do PDF                   |
| `lxml`           | Parser HTML alternativo (rápido) |