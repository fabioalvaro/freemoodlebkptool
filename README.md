# freemoodlebkptool
Moodle Backup Tool

This is a command line tool to increase the time to backup and restore applications wrote on Moodle.



1)Install
git clone https://github.com/fabioalvaro/freemoodlebkptool.git ~/opt/moodlebkptool

2)Create the link on system

$ cd /usr/local/bin

$ ln -s ~/opt/moodlebkptool/moodlerestoretool.py moodlerestoretool



# Example of use of the Tool:
    
    #to Restore a Backup created
    freemoodlerestoretool myApp01.mdlbkp.tar  /var/www/homemaranha /datamoodle/homemaranha 127.0.0.1 root mypassword homemaranha_db 
