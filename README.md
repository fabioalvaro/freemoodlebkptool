# freemoodlebkptool
Moodle Backup Tool

This is a command line tool to increase the time to backup and restore applications wrote on Moodle.

# 1 requirements of the Tool

* python

* Mysql Server

* Root Database (to extract and restore the databases)


# 2)Install

#Globally

git clone https://github.com/fabioalvaro/freemoodlebkptool.git ~/opt/moodlebkptool

2)Create the link on system

$ cd /usr/local/bin

$ ln -s ~/opt/moodlebkptool/moodlerestoretool.py moodlerestoretool

    # Installation on system scope
    $ sudo git clone https://github.com/fabioalvaro/freemoodlebkptool.git /opt/freemoodlebkptool

    
#Locally

How to Install Locally on your default user:

1)Download the zip version
    cd ~
    wget https://github.com/slackwarecps/freemoodlebkptool/archive/master.zip
    

2)Unzip the package
    unzip master 
3)Create a simbolic link to binary

    rm ~/bin/freemoodlebkptool

    rm ~/bin/freemoodlerestoretool

    ln -s freemoodlebkptool-master/freemoodlebkptool.py  ~/bin/freemoodlebkptool

    ln -s freemoodlebkptool-master/freemoodlerestoretool.py  ~/bin/freemoodlerestoretool 


4)use it!
    $ freemoodlebkptool
    OR
    $ freemoodlerestoretool
    
    
# 3 Configuration Before use


1)define a environment variable
$ export PT_DESTINO=/home/fabioalvaro/python_aulas/freemoodlebkptool/destino_backups


# 4 Examples of use of the Tool:
    #to Create a Full Backup of Moodle Instalation
    freemoodlebkptool /var/production_www/application01 myApp01
    
    #to Restore a Backup created
    freemoodlerestoretool myApp01.mdlbkp.tar  /var/www/homemaranha /datamoodle/homemaranha 127.0.0.1 root mypassword homemaranha_db 
