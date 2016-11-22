#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
import time
import sys

# zipa(diretorio_a_Ser_compactado, nome_do_backup )
def f_zipa(a,file_name):
    global PT_DESTINO
    print (" aaa " +a  )
    print (" bbb " +file_name  )
   # raise Exception('Para MAno!!! '+a + "  "+ file_name)
    #zip -r9 /home/fabioalvaro/temp/banana.zip  /home/fabioalvaro/android-studio
    #comando='zip -r9 /home/fabioalvaro/temp/'+file_name+'.zip  /home/fabioalvaro/android-studio'
    #comando='zip -r -j /home/fabioalvaro/temp/'+file_name+'.zip  '+ a
    print PT_DESTINO
    comando='sudo zip -r '+ PT_DESTINO +'/'+file_name+'.zip  '+ a
     
    print (comando)
    os.system(comando)    
    print  file_name+".zip  "+" Backup realizado! "

def get_valor_da_linha( texto ):
   # print "Texto na Funcao: "+ texto
    str_base = texto;
    str_agulha = "=";

    posicao = str_base.find(str_agulha)
    tamanho = len(texto)-2
   # print "Posicao " + str(posicao)
   # print "Tamanho " , len(texto)
   # print "Texto Recuperado " + texto.find(texto, posicao,10)
    v3 = texto[16:7]
   # print "pedacao: (" + v3	+")"
   # print "pedaco :",texto[posicao+1:tamanho]
    retorno =texto[posicao+1:tamanho]
    return retorno

def get_moodleData( config_file ):
    arq = open(config_file, 'r')
    print arq
    texto = arq.readlines()
    for linha in texto :	
        v1 = two = linha[0:14]
	    #print (v1)
        if v1=="$CFG->dataroot" :
            print("sim igual !!!!!")
            v2 = get_valor_da_linha(linha)
            print "Valor "+v2
            #v3 = v2.replace("'", "")
            removed = v2.replace("'", "")
            removed = removed.strip()
           # removed = "      "+removed+"       "
           # print removed.strip()
          #  newstr = v2.replace("M", " ")
           # print (removed)
    arq.close()
    return  removed 


def printme( str ):
   "This prints a passed string into this function"
   print str
   return    

#limpa a tela

os.system("clear")

os.system("pause")

#veio parametro 1?
#param1 = sys.argv[0]

#rint sys.argv[0]
#print sys.argv[1]#
#print sys.argv[2]

if len(sys.argv) >= 3:
    param1 = sys.argv[0]
    param2 = sys.argv[1]
    param3 = sys.argv[2]
else:
	print "Error:"
	print "voce precisa informar algum parametro, parametros nao informados"
	print " Syntax ler2.py diretorio_app cmd1 Nome_Amigavel_do_Backup"
	exit()
	

#LER DESTINO NA VARIAVEL DE AMBIENTE
PT_DESTINO = os.environ.get('PT_DESTINO')


if PT_DESTINO is None:
    print "ERRO: A VARIAVEL DESTINO GLOBAL  PT_DESTINO NAO FOI DEFINIDA!";
    print "USE $ export PT_DESTINO=/PATH/DOS/BACKUPS";
    print "E TENTE NOVAMENTE";
    print "====================="
    exit()



#print "Conteudo da Variavel PATH " + PT_DESTINO
#exit()

#pega variaveis
dir_alvo =param2



is_dir =os.path.isdir(dir_alvo)
exist_dir =os.path.exists(dir_alvo)

print ("MOODLE APPLICATION DOWNLOAD")
print ("")
print ("========================================")
#print ("SCRIPT        ["+ param1)
print ("APP DIRETORIO    ["+ param2+"]")
print ("NOME DOS BACKUPS ["+ param3+"]")
print ("PASTA DESTINO DO SHELL ["+ PT_DESTINO+"]")



#diretorio valido?

#is_dir = print(os.path.isdir(dir_alvo))
#exist_dir = print(os.path.exists(dir_alvo))



#valida o diretorio
if not is_dir:
    print "Erro: Diretorio invalido!!!"
    exit()

#existe um arquivo de configuracao dentro?
exist_config_file =os.path.exists(dir_alvo+'/config.php')
if not exist_config_file:
    print "Erro: Esse Diretorio nao tem configuracao moodle verifique!!!"
    exit()

    #nome do diretorio
dir_name_limpo = os.path.basename(dir_alvo)
#print "Nome do Diretorio "+dir_name_limpo
print "DIRETORIO NOME [ "+dir_name_limpo+"]"

#prefix_tool = 'graduacao_'
prefix_tool = param3+'_'



#prefix_tool = dir_name_limpo+'_'
dir_nome_zip = dir_name_limpo

#config File
config_file =dir_alvo+'/config.php'




#arq = open('/home/fabioalvaro/python_aulas/config.php', 'r')




#Qual o Moodle Data?
dir_moodle_data =  get_moodleData(config_file)
print "MOODLE DATADIR [" + dir_moodle_data+ "]"
print "DIRETORIO NOME ["+dir_name_limpo+"]"


#diretorio é valido?
is_dir_moddata =os.path.isdir(dir_moodle_data)
if not is_dir_moddata:
    print "Erro: Diretorio Moodle Data invalido!!!"
    exit()

#Resumo



ans=True
while ans:
    print ""
    print ""
    print ""
    print (""" Deseja executar o Backup da Aplicacao Moodle acima? (y/N)	""")
    ans=raw_input("Escolha: ") 
    if ans=="y" or ans=="Y":   
        print("\n Student Added")
        ans=False
    elif ans !="":
      print("\n Opcao Invalida!")
    elif ans =="":
      print("\n Saiu sem fazer nada")
      exit()        

print 'passou...'



#print "Maravilha senta o pau Arnaldo!"
#exit()
#Agora ja era.... senta o pau!!!



#faz backup do app
f_zipa(dir_alvo,prefix_tool+dir_nome_zip+"_app")


#faz backup do Moodle Data

#print dir_moodle_data,prefix_tool+dir_nome_zip+"_md"


f_zipa(dir_moodle_data,prefix_tool+dir_nome_zip+"_md")

print "Fim do Processo"
exit()
#copia pasta
# /home/fabioalvaro/android-studio

#barra de Progresso 
toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")




   # Now you can call printme function
#printme("I'm first call to user defined function!")
#printme("Again second call to the same function")
