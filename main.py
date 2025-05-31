# Importação das bibliotecas necessárias

import os
import shutil

# Definição do caminho da pasta que será organizada

caminho_base = os.path.join(os.getcwd(), "data")

# Mapeamento das extensões para categorias de arquivos
# Este dicionário define quais extensões pertencem a quais categorias
# As chaves são os nomes das pastas e os valores são listas de extensões

extensoes = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".doc"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Apresentações": [".ppt", ".pptx"],
    "Áudios": [".mp3", ".wav", ".ogg"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Executáveis": [".exe", ".msi"],
}

# Função auxiliar que encontra a categoria correspondente a uma extensão
# A função percorre o dicionário e retorna a categoria (nome da pasta)
# correspondente à extensão do arquivo. Se não encontrar, retorna 'Outros'.

def encontrar_categoria(extensao):
    for categoria, lista_extensoes in extensoes.items():
        if extensao.lower() in lista_extensoes:
            return categoria
    return "Outros"

# Listagem de arquivos no diretório base
# Este bloco lista todos os arquivos da pasta base, ignorando pastas

for nome_arquivo in os.listdir(caminho_base):
    caminho_completo = os.path.join(caminho_base, nome_arquivo)

    if os.path.isfile(caminho_completo):
        _, extensao = os.path.splitext(nome_arquivo)

        categoria = encontrar_categoria(extensao)

        pasta_destino = os.path.join(caminho_base, categoria)

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        destino_final = os.path.join(pasta_destino, nome_arquivo)

        shutil.move(caminho_completo, destino_final)

        print(f"Movido: {nome_arquivo} → {categoria}")
