clear 
echo "Remember use this script as a root user!"
rm /usr/bin/freemoodlebkptool 
rm /usr/bin/freemoodlerestoretool
ln -s /opt/freemoodlebkptool/freemoodlebkptool.py /usr/bin/freemoodlebkptool
ln -s /opt/freemoodlebkptool/freemoodlerestoretool.py /usr/bin/freemoodlerestoretool
echo "The tool freemoodlebkptool was installed"
