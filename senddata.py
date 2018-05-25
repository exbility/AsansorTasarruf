import ftplib
from ftplib import FTP

session = ftplib.FTP('IP_ADRESI','FTP_USERNAME','FTP_PASSWORD')
session.cwd('/public_html')
file = open('kayitlar.txt','rb')                  # file to send
session.storbinary('STOR kayitlar.txt', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
