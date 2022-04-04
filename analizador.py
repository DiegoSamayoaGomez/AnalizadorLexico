from sly import Lexer

class BasicLexer(Lexer):
    
    #Conjunto de tokens reconocidos
    tokens = { NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    
    #Determinar que cadena se ignorará para marcar final de cada cadena
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    #Expresiones regulares reconocidas para cada token
    IF = r'SI'
    THEN = r'ENTONCES'
    ELSE = r'SINO'
    FOR = r'CICLO'
    FUN = r'DECF'
    TO = r'HACIA'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*' 
    STRING = r'\".*?\"'
    EQEQ = r'=='

#Especificar rango de números aceptados
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

#Especificar capacidad de realizar comentarios
    @_(r'#.*')
    def COMMENT(self, t):
        pass

#Especificar salto de linea
    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

#Especificar manejo de errores
    def error(self, t):
        self.index += 1
        return  t