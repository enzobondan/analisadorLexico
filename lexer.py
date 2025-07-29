import re
from token_defs import TOKEN_SPECS, KEYWORDS

class LexicalError(Exception):
    # Exceção customizada para erros léxicos que inclui número da linha
    def __init__(self, message, line_number):
        super().__init__(f"Linha {line_number}: {message}")

class Lexer:
    def __init__(self):
        # Compila uma única regex unificada para todos os tipos de tokens, usando grupos nomeados
        self.token_regex = re.compile(
            '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECS),
            re.DOTALL
        )

    def tokenize(self, code: str):
        pos = 0              # Posição atual no código fonte
        line = 1             # Número da linha atual para rastreamento de erros
        tokens = []          # Lista para armazenar tokens reconhecidos
        erros = []           # Lista para armazenar mensagens de erro léxico

        lines = code.splitlines()  # Quebra o código em linhas para mensagens de erro e posicionamento
        current_line_start = 0     # Índice de início da linha atual no texto completo

        while pos < len(code):
            match = self.token_regex.match(code, pos)  # Tenta casar um token a partir da posição atual
            if not match:
                # Nenhum token reconhecido na posição atual - caractere inválido
                line_text = lines[line - 1] if line - 1 < len(lines) else ""
                col = pos - current_line_start
                char = code[pos]

                erro = (
                    f"Linha {line}: Caractere inválido: {char!r}\n"
                    f"{line_text}\n"
                    f"{' ' * col}^"
                )
                erros.append(erro)
                pos += 1  # Avança um caractere para continuar a análise
                continue

            kind = match.lastgroup  # Nome do grupo regex que casou (tipo do token)
            lexeme = match.group(kind)  # Texto capturado para o token

            if kind == "STRING_UNCLOSED":
                # Trata string sem fechamento, erro léxico específico
                col = match.start() - current_line_start
                erro = (
                    f"Linha {line}: String malformada (não fechada)\n"
                    f"{lines[line - 1]}\n"
                    f"{' ' * col}^"
                )
                erros.append(erro)
                pos = match.end()
                continue

            if kind == "NUM_MALFORMADO":
                # Trata número de ponto flutuante mal formado
                col = match.start() - current_line_start
                erro = (
                    f"Linha {line}: Número de ponto flutuante malformado\n"
                    f"{lines[line - 1]}\n"
                    f"{' ' * col}^"
                )
                erros.append(erro)
                pos = match.end()
                continue

            elif kind == "NEWLINE":
                # Nova linha detectada — incrementa contador de linha e atualiza posição da linha
                line += 1
                current_line_start = match.end()
            elif kind == "SKIP" or kind == "COMMENT_SINGLE":
                # Espaços, tabs e comentários de linha única são ignorados (não geram tokens)
                pass
            elif kind == "COMMENT_MULTI":
                # Comentários multi-linha podem conter quebras de linha, atualiza contador de linhas
                line += lexeme.count('\n')
            elif kind == "MISMATCH":
                # Qualquer caractere não reconhecido é erro léxico genérico
                col = match.start() - current_line_start
                line_text = lines[line - 1] if line - 1 < len(lines) else ""

                erro = (
                    f"Linha {line}: Caractere inválido: {lexeme!r}\n"
                    f"{line_text}\n"
                    f"{' ' * col}^"
                )
                erros.append(erro)
                pos = match.end()
                continue
            else:
                # Caso especial: se o token for identificador e estiver entre as palavras-chave, ajusta tipo
                if kind == "ID" and lexeme in KEYWORDS:
                    kind = "KEYWORD"
                # Armazena o token reconhecido (linha, tipo, lexema)
                tokens.append((line, kind, lexeme))

            pos = match.end()  # Avança a posição para continuar a análise

        return tokens, erros
