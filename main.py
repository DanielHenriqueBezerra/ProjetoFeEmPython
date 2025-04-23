# Importa a função que criamos no arquivo leitor.py

from utils.leitor import ler_texto

def mostrar_menu():
    print("Bem-vindo ao Projeto Fé em Python 🙏✨")
    print("1. Proteção")
    print("2. Gratidão")
    print("3. Família")
    escolha = input("Digite o número da sua escolha: ")
    return escolha

escolha = mostrar_menu()

if escolha == "1":
    tema = "protecao"
elif escolha == "2":
    tema = "gratidao"
elif escolha == "3":
    tema = "familia"
else:
    print("Escolha inválida.😢")
    exit()

# Monta os caminhos dos arquivos

caminho_oracao = f"oracoes/{tema}.txt"
caminho_versiculo = f"versiculo/{tema}.txt"

# Lê os conteúdos usando a função que criamos

conteudo_oracao = ler_texto(caminho_oracao)
conteudo_versiculo = ler_texto(caminho_versiculo)

# Mostra os resultados
print("\n🙏 Oração:")
print(conteudo_oracao)

print("\n📖 Versículo:")
print(conteudo_versiculo)
