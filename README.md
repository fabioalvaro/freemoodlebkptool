# freemoodlebkptool
Moodle Backup Tool

This is a command line tool to increase the time to backup and restore applications wrote on Moodle.

# 1 requirements of the Tool

* python

* Mysql Server

* Root Database (to extract and restore the databases)


# 2)Install
git clone https://github.com/fabioalvaro/freemoodlebkptool.git ~/opt/moodlebkptool

2)Create the link on system

$ cd /usr/local/bin

$ ln -s ~/opt/moodlebkptool/moodlerestoretool.py moodlerestoretool

# 3 Configuration Before use


1)define a environment variable
$ export PT_DESTINO=/home/fabioalvaro/python_aulas/freemoodlebkptool/destino_backups


# 4 Examples of use of the Tool:
    #to Create a Full Backup of Moodle Instalation
    freemoodlebkptool /var/production_www/application01 myApp01
    
    #to Restore a Backup created
    freemoodlerestoretool myApp01.mdlbkp.tar  /var/www/homemaranha /datamoodle/homemaranha 127.0.0.1 root mypassword homemaranha_db 
