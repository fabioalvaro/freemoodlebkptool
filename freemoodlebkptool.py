#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
import time
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''





# compress the file

def f_zipa(a,file_name):
    global PT_DESTINO
    comando='tar -zcvf '+ PT_DESTINO +'/'+file_name+'.tar.gz -C ' + a+' .'
    os.system(comando)    
    print file_name+".zip  "+" Backup realizado! "

def get_valor_da_linha( texto ):
    str_base = texto;
    str_agulha = "=";
    posicao = str_base.find(str_agulha)
    tamanho = len(texto)-2
    retorno =texto[posicao+1:tamanho]
    return retorno

def get_moodleData( config_file ):
    arq = open(config_file, 'r')
   # print arq
    texto = arq.readlines()
    for linha in texto :	
        v1 = two = linha[0:14]
	    #print (v1)
        if v1=="$CFG->dataroot" :
            v2 = get_valor_da_linha(linha)
            removed = v2.replace("'", "")
            removed = removed.strip()
    arq.close()
    return removed


#Get Valor From config moodle
def get_valor_config(file,size,text_needle):
    myretorno ="0"
    arq = open(file, 'r')
    texto = arq.readlines()
    removed = "" 
    for linha in texto :	
        v1 = two = linha[0:12]      
        if v1==text_needle :           
            v2 = get_valor_da_linha(linha)          
            removed = v2.replace("'", "")
            removed = removed.strip()
            myretorno = removed
    arq.close()    
    return myretorno


#MYSQL INFORMATION GET 
# host,db,use,pass
def get_mysql_parametros( config_file ):
    my_array = [1, 'rebecca', 'allard','pass']    
    
    v_dbhost = get_valor_config(config_file,12,'$CFG->dbhost')    
    my_array[0]=v_dbhost
    
    v_dbname = get_valor_config(config_file,12,'$CFG->dbname')    
    my_array[1]=v_dbname      
           
    v_dbuser = get_valor_config(config_file,12,'$CFG->dbuser')    
    my_array[2]=v_dbuser  
    
    v_dbpass = get_valor_config(config_file,12,'$CFG->dbpass')
    my_array[3]=v_dbpass

    return my_array
#MYSQL INFORMATION GET


#BACKUP DO MYSQL
def backup_mysql(DB_HOST,DB_NAME,DB_USER,DB_PASS,SET_BACKUP_FILE_NAME):
    stat=0
    comando = 'mysqldump -vh'+DB_HOST+' -u'+DB_USER+' -p'+DB_PASS+' '+DB_NAME+' | gzip -9 -c  > '+SET_BACKUP_FILE_NAME+".gz"
    print (comando)
    os.system(comando)
    return stat


#Clean the screen
os.system("clear")


#arrive the param 1?

if len(sys.argv) >= 3:
    param1 = sys.argv[0]
    param2 = sys.argv[1]
    param3 = sys.argv[2]
else:
	print "Error:"
    print "You must to inform any param! Error parameter not valid."

    print ""
	exit()
	

#Read the Environment Variable
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


#Procura os parametros do Mysql
print "MYSQL SETTINGS"
mysql_parametros =  get_mysql_parametros(config_file)
print " host    " +mysql_parametros[0]+ bcolors.OKGREEN + "  SUCCESS" + bcolors.ENDC
print " db_name " +mysql_parametros[1]+ bcolors.OKGREEN + "  SUCCESS" + bcolors.ENDC
print " user    " +mysql_parametros[2]+ bcolors.OKGREEN + "  SUCCESS" + bcolors.ENDC
print " pass    " +mysql_parametros[3]+ bcolors.OKGREEN + "  SUCCESS" + bcolors.ENDC






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

    print (""" Did you want to run the Backup as showned above? (y/N)	""")
    ans=raw_input("Escolha: ") 
    if ans=="y" or ans=="Y":   
        print("\n Yes lets go...")
        ans=False
    elif ans !="":
      print("\n invalid option!")
    elif ans =="":
      print("\n exit, without to do nothing")
      exit()        



#faz backup do app
f_zipa(dir_alvo,prefix_tool+dir_nome_zip+"_app")


#faz backup do Moodle Data

f_zipa(dir_moodle_data,prefix_tool+dir_nome_zip+"_md")

#MYSQL Processo

print(bcolors.OKGREEN + "SUCCESS" + bcolors.ENDC)
destino_backup_file=PT_DESTINO+'/'+prefix_tool+dir_name_limpo+'.sql'


#realiza o backup
backup_mysql(mysql_parametros[0],mysql_parametros[1],mysql_parametros[2],mysql_parametros[3],destino_backup_file)



print "End of Process"
exit()


