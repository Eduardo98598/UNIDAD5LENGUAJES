import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin

precedence = (
	('right','ID','CALL','BEGIN','IF','WHILE'),
	('right','PROCEDURE'),
	('right','VAR'),
	('right', 'ASSIGN'),
	('right','UPDATE'),
	('left','NE'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','ODD'),
	('left','LPARENT','RPARENT'),
	)

def p_program(p):
	'''program : block'''
	print "ANALISIS DEL PROGRAMA"
	#p[0] = program(p[1],"program")

def p_block(p):
	'''block : constDecl varDecl procDecl statement'''
	print "BLOQUE"

def p_constDecl(p):
	'''constDecl : CONST constAssignmentList SEMMICOLOM'''
	#p[0] = constDecl(p[2])
	print "CONSTANTE"

def p_constDeclEmpty(p):
	'''constDecl : empty'''
	#p[0] = Null()
	print "CONSTANTEDESC"

def p_constAssignmentList1(p):
	'''constAssignmentList : ID ASSIGN NUMBER'''
	print "INTANCIADECONSTANTE"

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMMA ID ASSIGN NUMBER'''
	print "INSTANCIADEMULTCONSTANTES"

def p_varDecl1(p):
	'''varDecl : VAR identList SEMMICOLOM'''
	print "INSTANCIADEVARIABLE"

def p_varDeclEmpty(p):
	'''varDecl : empty'''
	print "VARIABLENULO"

def p_identList1(p):
	'''identList : ID'''
	print "IDENTIFICADOR"

def p_identList2(p):
	'''identList : identList COMMA ID'''
	print "MULTIDENTIFICADOR"

def p_procDecl1(p):
	'''procDecl : procDecl PROCEDURE ID SEMMICOLOM block SEMMICOLOM'''
	print "INSTANCIADEMETODO"

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	print "METODOINDEF"

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	print "IDENTIFICADORACTUALIZADO"

def p_statement2(p):
	'''statement : CALL ID'''
	print "LLAMADAIDENTIFICADOR"

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	print "INICIOFINAL"

def p_statement4(p):
	'''statement : IF condition THEN statement'''
	print "CONDICION"

def p_statement5(p):
	'''statement : WHILE condition DO statement'''
	print "ESTRUCTURADO"

def p_statementEmpty(p):
	'''statement : empty'''
	print "IDENTIFICADORNULO"

def p_statementList1(p):
	'''statementList : statement'''
	print "LISTADEIDENTIFICADORES"

def p_statementList2(p):
	'''statementList : statementList SEMMICOLOM statement'''
	print "IDENTICADORESANIDADO"

def p_condition1(p):
	'''condition : ODD expression'''
	print "ODD"

def p_condition2(p):
	'''condition : expression relation expression'''
	print "RELACION"

def p_relation1(p):
	'''relation : ASSIGN'''
	print "RELASIGNACION"

def p_relation2(p):
	'''relation : NE'''
	print "RELDIF"

def p_relation3(p):
	'''relation : LT'''
	print "RELMENOR"

def p_relation4(p):
	'''relation : GT'''
	print "RELMAYOR"

def p_relation5(p):
	'''relation : LTE'''
	print "RELMENORIGUAL"

def p_relation6(p):
	'''relation : GTE'''
	print "RELMAYORIGUAL"

def p_expression1(p):
	'''expression : term'''
	print "EXPRESIONES"

def p_expression2(p):
	'''expression : addingOperator term'''
	print "OTROSOPERADORES"

def p_expression3(p):
	'''expression : expression addingOperator term'''
	print "EXPRESIONCONOPERADOR"

def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	print "SUMA"

def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	print "RESTA"

def p_term1(p):
	'''term : factor'''
	print "FACTOR"

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print "TERMINOCONFACTOR"

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	print "MULTIPLICACION"

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	print "DIVISION"

def p_factor1(p):
	'''factor : ID'''
	print "IDENTIFICADORDELFACTOR"

def p_factor2(p):
	'''factor : NUMBER'''
	print "NUMERO"

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''
	print "PARENTESISIZQ"

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print "Error: La sintaxis no es correcta ", p
	print "Error en la linea "+str(p.lineno)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta == False:
		numArchivo = raw_input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

	return files[int(numArchivo)-1]

directorio = 'C:/Users/carl-/OneDrive/Compilador_PL0/analizadorV2/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print result






