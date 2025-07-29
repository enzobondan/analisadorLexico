import os
import json
from lexer import Lexer, LexicalError

def listar_arquivos_dnsfu():
    # Lista todos os arquivos com extensão .dnsfu no diretório atual
    return [f for f in os.listdir('.') if f.endswith('.dnsfu')]

def exibir_menu(arquivos):
    # Exibe um menu numerado com os arquivos encontrados para o usuário escolher
    print("Arquivos encontrados:")
    for idx, nome in enumerate(arquivos):
        print(f"{idx + 1}. {nome}")
    print()

def selecionar_arquivo(arquivos):
    # Recebe do usuário a escolha do arquivo, garantindo que a entrada seja válida
    while True:
        try:
            escolha = int(input("Selecione o número do arquivo a ser analisado: "))
            if 1 <= escolha <= len(arquivos):
                return arquivos[escolha - 1]
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas o número correspondente.")

def exportar_tokens(tokens, arquivo_base):
    # Exporta a lista de tokens para um arquivo JSON com indentação para melhor leitura
    with open(arquivo_base + '.json', 'w', encoding='utf-8') as jf:
        json.dump(tokens, jf, ensure_ascii=False, indent=2)

def main():
    # Função principal do programa que orquestra o fluxo do analisador léxico

    arquivos = listar_arquivos_dnsfu()

    if not arquivos:
        print("Nenhum arquivo .dnsfu encontrado no diretório atual.")
        return

    exibir_menu(arquivos)
    selecionado = selecionar_arquivo(arquivos)

    try:
        with open(selecionado, encoding="utf-8") as f:
            source = f.read()

        if not source.strip():
            print("O arquivo está vazio. Nada a analisar.")
            return

        lexer = Lexer()
        tokens, erros = lexer.tokenize(source)

        # Exibe os tokens encontrados formatados por linha, tipo e lexema
        print("\nTOKENS RECONHECIDOS:\n")
        for linha, tipo, lexema in tokens:
            print(f"Linha {linha:<3} | {tipo:<12} => {lexema}")

        # Exibe possíveis erros léxicos encontrados
        if erros:
            print("\nERROS LÉXICOS ENCONTRADOS:\n")
            for erro in erros:
                print(erro)
        else:
            print("\nNenhum erro léxico encontrado.")

        base_nome = os.path.splitext(selecionado)[0]
        exportar_tokens(tokens, base_nome)

        print(f"\nTokens exportados para: {base_nome}.json")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{selecionado}' não encontrado.")
    except LexicalError as e:
        print(f"Erro léxico: {e}")

if __name__ == "__main__":
    main()
