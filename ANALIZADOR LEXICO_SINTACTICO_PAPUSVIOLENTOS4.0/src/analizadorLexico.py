import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST',
		'VAR','PROCEDURE','OUT','IN','ELSE','RETURN','THIS','EXTENDS','NEW','LENGTH',
		'INT','TRUE','BOOLEAN','FALSE','CONTINUE','NULL','CASE',
		'CATCH','BREAK','DELETE','DEBUGGER','FINALLY','FOR','FUNCTION','INSTANCEOF','LET',
		'SWITCH','THROW','TRY','TYPEOF','VOID','CON','SCRIPT'
		]

tokens = reservadas+[#'VARIABLE','INTEGER','SUM','MIN','MULT','DIVIDE','ODD','ASIGNACION','DIFERENTE','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL','PARENTESISIZQ', 'PARENTESISDER','COMA','PUNTOCOMA','DOT','UPDATE',
		'ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT', 'RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE','CAND','COR','IGUALIGUAL','DIFERENTEJAVA','LLAVEIZQ','LLAVEDER','CORCHIZQ','CORCHDER',
		'ADMIRACION','GUION','MOD','DOSPUNTOS','COMSIMDER','COMSIMIZQ','COMDOBDER','COMDOIZQ','DOUBLE','COMENTARIO',
		'COMMIT','APERFIN', 'APERINI','COMILLADOBLEDER','COMILLASIMPLEDER','STRING']

#tokens = tokens+reservadas

# reservadas = {
	# 'begin':'BEGIN',
	# 'end':'END',
	# 'if':'IF',
	# 'then':'THEN',
	# 'while':'WHILE',
	# 'do':'DO',
	# 'call':'CALL',
	# 'const':'CONST',
	# 'int':'VAR',
	# 'procedure':'PROCEDURE',
	# 'out':'OUT',
	# 'in':'IN',
	# 'else':'ELSE'
# }

#tokens = tokens+list(reservadas.values())

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='
t_CAND='&&'
t_COR=r'\|\|'
t_IGUALIGUAL=r'=='
t_DIFERENTEJAVA='!='
t_LLAVEIZQ = '\{'
t_LLAVEDER = '\}'
t_CORCHIZQ = '\['
t_CORCHDER = r'\]'
t_ADMIRACION = '!'
t_GUION = '-'
t_MOD  = '%'
t_DOSPUNTOS = r':'
t_COMSIMDER = r'\''
t_COMSIMIZQ = r'\''
t_COMDOBDER = r'\"'
t_COMDOIZQ = r'\"'
t_DOUBLE= r'\d*[.,]?\d+'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMENTARIO(t):
	r'\#.*'
	pass
def t_COMMIT(t):
	r'(<!--)[a-zA-Z_]*( )*[\w]*'
	return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t
def t_COMILLADOBLEDER(t):

	r'"([\x20-\x7E]|\t|\r)*"'
	t.value = str(t.value)
	return t
def t_COMILLASIMPLEDER(t):

	r"'([\x20-\x7E]|\t|\r)*'"
	t.value = str(t.value)
	return t

def t_error(t):
	#print " CARACTERES NO RECONOCIDOS'%s'" % t.value[0]
	t.lexer.skip(1)

# def buscarFicheros(directorio):
# 	ficheros = []
# 	numArchivo = ''
# 	respuesta = False
# 	cont = 1

# 	for base, dirs, files in os.walk(directorio):
# 		ficheros.append(files)

# 	for file in files:
# 		print str(cont)+". "+file
# 		cont = cont+1

# 	while respuesta == False:
# 		numArchivo = raw_input('\nNumero del test: ')
# 		for file in files:
# 			if file == files[int(numArchivo)-1]:
# 				respuesta = True
# 				break

# 	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

# 	return files[int(numArchivo)-1]

# directorio = '/Users/sebas/Documents/Compiladores/pl0/analizador version 1/test/'
# archivo = buscarFicheros(directorio)
# test = directorio+archivo
# fp = codecs.open(test,"r","utf-8")
# cadena = fp.read()
# fp.close()

analizador = lex.lex()

#analizador.input(cadena)

# while True:
# 	tok = analizador.token()
# 	if not tok : break
# 	print tok



