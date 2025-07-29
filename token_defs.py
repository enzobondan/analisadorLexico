# Palavras-chave reservadas da linguagem
KEYWORDS = {
    "if", "else", "while", "return", "int", "float", "string", "sqrt"
}

# Lista de especificações dos tokens com suas expressões regulares
TOKEN_SPECS = [
    # Números malformados — casos inválidos que precisam ser detectados como erro léxico
    ('NUM_MALFORMADO', r'\d+\.\.|(?<!\d)\.\d+|\d+\.(?!\d)'),  # Exemplos: 3..14, .12, 10.

    # Literais numéricos válidos
    ('NUM_FLOAT',      r'\d+\.\d+'),  # Números de ponto flutuante válidos (ex: 3.14)
    ('NUM_INT',        r'\d+'),       # Números inteiros (ex: 42)

    # Literais de string
    ('STRING',          r'"[^"\n]*"'),   # String válida com aspas duplas (ex: "texto")
    ('STRING_SINGLE',   r"'[^'\n]*'"),   # String válida com aspas simples (ex: 'texto')
    ('STRING_UNCLOSED', r'"[^"\n]*'),    # String com aspas duplas sem fechamento

    # Identificadores (nomes de variáveis, funções, etc.)
    ('ID',             r'[a-zA-Z_][a-zA-Z_0-9]*'),

    # Comentários
    ('COMMENT_MULTI',  r'/\*.*?\*/'),    # Comentário de múltiplas linhas (ex: /* ... */)
    ('COMMENT_SINGLE', r'//[^\n]*'),     # Comentário de uma linha (ex: // ...)

    # Operadores compostos (dois ou mais caracteres)
    ('PLUS_ASSIGN',    r'\+='),          # Operador +=
    ('MINUS_ASSIGN',   r'-='),           # Operador -=
    ('POWER',          r'\*\*'),         # Potência **
    ('EQ',             r'=='),           # Igualdade ==
    ('NEQ',            r'!='),           # Diferente !=
    ('LEQ',            r'<='),           # Menor ou igual <=
    ('GEQ',            r'>='),           # Maior ou igual >=

    # Operadores simples (um caractere)
    ('ASSIGN',         r'='),            # Atribuição =
    ('PLUS',           r'\+'),           # Soma +
    ('MINUS',          r'-'),            # Subtração -
    ('MULT',           r'\*'),           # Multiplicação *
    ('DIV',            r'/'),            # Divisão /
    ('LT',             r'<'),            # Menor <
    ('GT',             r'>'),            # Maior >
    ('NOT',            r'!'),            # Negação lógica !

    # Delimitadores (separadores de elementos da linguagem)
    ('DELIM',          r'[;,{}()\[\]\.]'),  # ; , { } ( ) [ ] .

    # Caracteres de controle e ignorados
    ('NEWLINE',        r'\n'),           # Quebra de linha
    ('SKIP',           r'[ \t]+'),       # Espaços e tabulações (ignorados)

    # Qualquer caractere não reconhecido pelos padrões anteriores
    ('MISMATCH',       r'.'),            # Para identificar erros léxicos genéricos
]
