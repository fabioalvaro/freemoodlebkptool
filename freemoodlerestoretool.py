#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
import time
import sys
import ntpath
import glob


version_app="1.0"
fake_prog_arquivo=1

print ""
print '========================='
print "MOODLE RESTORE TOOL 1.0"
print '========================='

def process_dbinfo():
    global c_localhost
    global c_user
    global c_pass
    print "==================================================================="
    print "MYSQL Connection"
    print "localhost:    " + c_localhost
    print "user:         " + c_user
    print "pass:         " + c_pass
    print "==================================================================="
    print ""
    print "WARNING! All Data will be erased on target showned above... Are you sure?"

def restore_database():
    global c_localhost
    global c_user
    global c_pass
    global TMP_FOLDER
    global p_db_name
    print TMP_FOLDER

    #defl
    #EXTRAPATH = "/data/backups"
    EXTRAPATH = ""
    comando = 'gunzip -d '+TMP_FOLDER+EXTRAPATH+'/*sql.gz'
    os.system(comando)
    print comando





    c_dbname = p_db_name.strip()

    #c_scriptname='colegioanchieta_colegioanchieta.sql'



    sql1 = 'DROP DATABASE IF EXISTS '+c_dbname
    comando = "mysql -u"+c_user+" -p"+c_pass+" -e "+sql1
    print comando
    os.system(comando)
    print "passou 3"
    print comando
    comando = 'mysql -u'+c_user+' -p'+c_pass+' -e "CREATE DATABASE IF NOT EXISTS '+c_dbname+'"'
    os.system(comando)



    #retrieve the file sql

    for file in os.listdir(TMP_FOLDER+EXTRAPATH):
        if file.endswith(".sql"):
            print(file)
            arquivo_sql=str(file)



   # arquivo_sql = os.system(comando)
    #print comando

    comando = 'mysql -h' + c_localhost + ' -u' + c_user + ' -p' + c_pass + ' ' + c_dbname + ' -v < '+TMP_FOLDER+EXTRAPATH+'/'+arquivo_sql
    print "SQL to Restore: "+comando
    #print "mysql -h127.0.0.1 -uroot -ptoor ze_do_caroco -v < /usr/tmp/asd/data/backups/*.sql"
    
    os.system(comando)
    #os.system("mysql -h127.0.0.1 -uroot -ptoor ze_do_caroco -v < /usr/tmp/asd/data/backups/*.sql")


    print 'Database '+c_dbname+' restored'





def ungroup(file_name):
    TMP_FOLDER_MD=TMP_FOLDER+"/md"
    TMP_FOLDER_APP = TMP_FOLDER + "/app"
    os.system("rm -rf "+TMP_FOLDER)
    os.system("mkdir -p "+TMP_FOLDER)
    #tar -xvf unico.tar
    comando = 'tar -xvf '+file_name +" -C "+TMP_FOLDER
    print "TEMP FOLDER "+TMP_FOLDER
    print (comando)


    os.system(comando)
    #extract folders
    os.system("rm -rf " + TMP_FOLDER+"/app")
    os.system("mkdir -p " + TMP_FOLDER+"/app")
    os.system("rm -rf " + TMP_FOLDER+"/md")
    os.system("mkdir -p " + TMP_FOLDER+"/md")

    # tar -zxvf compactada.tar.gz -C caminho/da/pasta/
    # mdlbkp.tar
    EXTRAPATH="/data/backups"
    EXTRAPATH = ""
    comando_app = 'tar -zxvf ' + TMP_FOLDER+EXTRAPATH + "/*_app.tar.gz -C " + TMP_FOLDER_APP
    os.system(comando_app)


    comando_md = 'tar -zxvf ' + TMP_FOLDER+EXTRAPATH + "/*_md.tar.gz -C " + TMP_FOLDER_MD
    print "LOG:"+ comando_md

    os.system(comando_md)

    global TMP_MD
    TMP_MD=TMP_FOLDER_MD

    global TMP_APP
    TMP_APP=TMP_FOLDER_APP

    print  file_name + ".zip  " + " Backup realizado! "




TMP_FOLDER='/usr/tmp/asd'
TMP_MD=''
TMP_APP=''
c_localhost=""
c_user =""
c_pass=""
p_db_host = ""
p_db_user = ""
p_db_pass = ""
p_db_name = ""

if len(sys.argv) >= 4:
    param1 = sys.argv[0]
    p_nomebackup = sys.argv[1]
    #recupera o nome do arquivo
    ntpath.basename(p_nomebackup)
    head, tail = ntpath.split(p_nomebackup)
    p_filename_backup=tail

    p_filename_backup_without_ext = os.path.splitext(p_filename_backup)[0]
    p_filename_backup_without_ext = os.path.splitext(p_filename_backup_without_ext)[0]


    p_nomebackup = sys.argv[1]
    p_pastadestino = sys.argv[2]
    p_pastadestino_moodleData = sys.argv[3]

    #check the database parameters
    if len(sys.argv) > 4:
        p_db_host = sys.argv[4]
        p_db_user = sys.argv[5]
        p_db_pass = sys.argv[6]
        # print p_db_host
        # print p_db_user
        # print p_db_pass
        c_localhost = p_db_host
        c_user = p_db_user
        c_pass = p_db_pass
        if len(sys.argv) >= 8:
           p_db_name = sys.argv[7]

  #  print "OK parece tudo certo!"




else:
    if not p_db_host:
        print "Database not defined!"
    if not p_db_user:
        print "Database User not defined!"
    if not p_db_host:
        print "Database Password not defined!"



    print "Ops! Error:"
    print "There are missing parameters! please complete the information as showed bellow"
    print ""
    print " Syntax:  freemoodlerestoretool  backup_name.mdlbkp.tar /home/foo/www/myAppRestoredTest1 /home/foo/MoodleDataRestoredTest1 "
    print " Syntax:  freemoodlerestoretool  backup_name.mdlbkp.tar /home/foo/www/myAppRestored [databasehost] [database] [password]"
    print ""
    print "Try Again! ;)"
    print ""
    print ""
    print ""
    exit()


#test
FOLDER_DESTINY=p_pastadestino
FOLDER_DESTINY_MD=p_pastadestino_moodleData
#remove last slash from directories
s=p_pastadestino_moodleData
if s.endswith('/'):
    s = s[:-1]
FOLDER_DESTINY_MD=s

#remove last slash from directories
s=p_pastadestino
if s.endswith('/'):
    s = s[:-1]
FOLDER_DESTINY=s




FD=FOLDER_DESTINY
FDM=FOLDER_DESTINY_MD


#print p_filename_backup
#print tail
#print(p_filename_backup_without_ext)
os.system("clear")
print "==================================================================="
print "MOODLE BACKUP TOOL - RESTORE MODE - " + version_app
print "==================================================================="
print "Backup Moodle Filename:                  " + p_filename_backup
print "Destination www Folder:                  " + FD
print "Destination Moodle Data Folder:          " + FDM
print ""
if c_localhost != "":
    process_dbinfo()
print ""
print ""

#coonfirm with user before run It is irreversible
#Resumo
ans=True
while ans:
    print ("Are you sure to run the Moodle Restore Tool? The modifications cannot be restore automatically (y/N)")
    ans=raw_input("Choose: ")
    if ans=="y" or ans=="Y":
        print("\n Confirmedy")
        ans=False
    elif ans !="":
      print("\n Opcao Invalida!")
    elif ans =="":
      print("\n nothing changed.")
      exit()

print 'approved co continue...      ;)'


#Rodar os processos


#print "Nome da Base: "+ p_db_name + "argumentos "+ str(len(sys.argv))
#exit()



#desagrupar backup
print "LOG 1: " + TMP_APP
print " "
ungroup(p_nomebackup)





APP_NAME_DESTINY=p_filename_backup_without_ext
# Move App Folder

print "LOG 2: " + TMP_APP
print " "
#diretorio existe?
    #apaga
os.system("rm -rf "+FD)

print FD
    #cria
#exit()
os.system("mkdir -p "+FD)
#copia
comando_app = 'cp -avr ' + TMP_APP + "/* " + FD


# /home/fabioalvaro/public_html/patorestaurado/patoverde_lfgonline
print "LOG: " + comando_app
os.system(comando_app)


#mover moodle data
print "LOG 3: " + TMP_MD
os.system("rm -rf "+FDM)
os.system("mkdir -p "+FDM)

comando_md = 'cp -avr ' + TMP_MD + "/* " + FDM
print "LOG: " + comando_md

os.system(comando_md)

#Restore the database
restore_database()
print ""
print ""
print ""
print ""
print "======================================================="
print "MOODLE BACKUP TOOL - RESTORE MODE - " + version_app
print "NOTICE"
print "======================================================="

#Final REcomendations
print "Change the configurations in your file config.php to reflect the new "
print "folder locations that could be diferent of the original source of backup!!!"
print "Change the file => "+FD+"/config.php"
print ""
print "C$CFG->dbhost    = '"+p_db_host+"';"
print "C$CFG->dbname    = '"+p_db_name+"';"
print "C$CFG->dbuser    = '"+p_db_user+"';"
print "C$CFG->dbpass    = '***************************';"
print ""
print "C$CFG->dirroot   = '"+FD+"';"
print "C$CFG->dataroot  = '"+FDM+"';"
print " "
print " "

print "**** Without theconfigurations above the moodle instalation will not work properly, please verifiy! "




print "End of Process"
exit()
#Restore Mysql









