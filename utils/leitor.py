#Aqui ira conter uma função simples para ler o conteudo do arquivo .txt

#Objetivo: Ler o conteúdo de um arquivo de texto (oração ou versículo) e devolver esse texto para ser mostrado na tela.
#------------------------------

# Função para ler o conteúdo de um arquivo de texto
def ler_texto(caminho_arquivo):
    try:
        with open(caminho_arquivo,"r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileExistsError:
        return "Arquivo não encontrado.🙁"
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"