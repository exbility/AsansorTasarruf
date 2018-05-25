import ftplib
from ftplib import FTP

session = ftplib.FTP('178.159.36.70','necrols','W!?XdH@OUz_.')
session.cwd('/public_html')
file = open('kayitlar.txt','rb')                  # file to send
session.storbinary('STOR kayitlar.txt', file)     # send the file
file.close()                                    # close file and FTP
session.quit()