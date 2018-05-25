import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import ftplib
from ftplib import FTP
import requests
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


ledpinler = [11,12,13,15,16]
led1=11
led2=12
led3=13
led4=15
led5=16
buton1=29
buton2=31
buton3=33
buton4=35
buton5=27
sonbasilan=1 #varsayilan kat
oncekibasilan=1 #varsayilan kat
kayitet=0

#url = "https://necrols.co/get_istatistik.php?saat=9"
url = "https://necrols.co/get_istatistik.php?saat={suankisaat}".format(suankisaat=strftime("%H", gmtime()))
r = requests.get(url)
if r.status_code == 200:
    sonbasilan=int(r.text)
    oncekibasilan=int(r.text)
else:
    bosluk()

#oprint(url)
#print("sonbasilan:{}".format(sonbasilan))
 
def blink(pin):
    print("led yandi..")
    GPIO.output(pin, True)
    time.sleep(0.1)
    return

def ledstatus(pin,onoff):
    if onoff == True:
        GPIO.output(pin, True)
    else:
        GPIO.output(pin, False)
        
    return

def bosluk():
    return

def kapat(haricpin):
    
    for i in range(0,len(ledpinler)):
        if haricpin == ledpinler[i]:
            #GPIO.output(i, False)
            bosluk()
        else:
            GPIO.output(ledpinler[i], False)
            #print i
    return


 
try:
    while True:
        
        butonOku1 = GPIO.input(29)
        butonOku2 = GPIO.input(31)
        butonOku3 = GPIO.input(33)
        butonOku4 = GPIO.input(35)
        butonOku5 = GPIO.input(37)
        
        
        
        ilkmi=0
        
        # BUTON KONTROLLERI
        
        if butonOku1 == True:
            oncekibasilan = sonbasilan
            sonbasilan = 1
            ilkmi=1
        elif butonOku2 == True:
            oncekibasilan = sonbasilan
            sonbasilan = 2
            ilkmi=1
        elif butonOku3 == True:
            oncekibasilan = sonbasilan
            sonbasilan = 3
            ilkmi=1
        elif butonOku4 == True:
            oncekibasilan = sonbasilan
            sonbasilan = 4
            ilkmi=1
        elif butonOku5 == True:
            oncekibasilan = sonbasilan
            sonbasilan = 5
            ilkmi=1
        else:
            bosluk()
        
        oncekikayitet = kayitet
        kayitet = "{0} {1} {2}\n".format(strftime("%H", gmtime()),oncekibasilan,sonbasilan)
        
        if oncekikayitet != kayitet and ilkmi==1 and oncekibasilan != sonbasilan:
            kayit = open("kayitlar.txt","a")
            kayit.write(kayitet)
            print("KAYIT YAPILDI {0}".format(kayitet))
        else:
            bosluk()
        
        print(oncekibasilan)
        print("aan\n")
        print(sonbasilan)
        # SON BASILAN
        
        
        if sonbasilan == 1:
            ledstatus(led1,1)
            kapat(led1)
        elif sonbasilan == 2:
            ledstatus(led2,1)
            kapat(led2)
        elif sonbasilan == 3:
            ledstatus(led3,1)
            kapat(led3)
        elif sonbasilan == 4:
            ledstatus(led4,1)
            kapat(led4)
        elif sonbasilan == 5:
            ledstatus(led5,1)
            kapat(led5)
        else:
            bosluk()
            
        time.sleep(0.4)
except KeyboardInterrupt:
    print ("Cikis yapildi. GPIOlar temizlendi..")
    GPIO.cleanup()