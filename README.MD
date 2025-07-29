# Analisador Léxico para Linguagem Fictícia DNSFU

## Visão Geral

Este projeto implementa um analisador léxico para uma linguagem fictícia chamada **DNSFU**. O analisador é capaz de identificar tokens básicos como palavras-chave, identificadores, números inteiros e de ponto flutuante, strings, operadores, delimitadores e comentários, além de detectar erros léxicos como caracteres inválidos, números malformados e strings não fechadas.

O analisador lê arquivos com extensão `.dnsfu` do diretório atual, permite ao usuário escolher qual arquivo deseja analisar, exibe os tokens reconhecidos e possíveis erros léxicos, e exporta os tokens para um arquivo JSON.

---

## Estrutura do Projeto

- **main.py**: Interface principal para o usuário, gerencia a leitura dos arquivos, execução do lexer e exportação dos tokens.
- **lexer.py**: Implementação do analisador léxico usando expressões regulares para identificar os tokens.
- **token_defs.py**: Definição das expressões regulares para os tokens e lista de palavras-chave da linguagem.

---

## Definição dos Tokens

A lista de tokens (em `token_defs.py`) inclui:

- **Palavras-chave**: `if`, `else`, `while`, `return`, `int`, `float`, `string`, `sqrt`.
- **Números**:
  - Inteiros (`NUM_INT`)
  - Ponto flutuante válidos (`NUM_FLOAT`)
  - Números malformados detectados e sinalizados como erro (`NUM_MALFORMADO`).
- **Strings**:
  - Com aspas duplas e simples.
  - Strings não fechadas são identificadas e reportadas como erro.
- **Identificadores**: nomes válidos de variáveis e funções.
- **Comentários**:
  - Linha única (`// comentário`)
  - Múltiplas linhas (`/* comentário */`)
- **Operadores**:
  - Simples: `+`, `-`, `*`, `/`, `=`, `<`, `>`, `!`
  - Compostos: `+=`, `-=`, `**`, `==`, `!=`, `<=`, `>=`
- **Delimitadores**: `;`, `,`, `{`, `}`, `(`, `)`, `[`, `]`, `.`
- **Ignorados**: espaços, tabulações e quebras de linha.

---

## Como Usar

1. Coloque arquivos `.dnsfu` com o código da linguagem fictícia no mesmo diretório do projeto.

2. Execute o programa principal:

```bash
python main.py
```
