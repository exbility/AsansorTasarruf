# AsansorTasarruf

Asansörlerin tasarruf edebilmesi için akıllı hareket sistemi. 

Raspberry Pi 3 , Python ve PHP kullanılarak yapılmıştır.

Çalışma Videosu Link : https://youtu.be/-qaW-gWuOJQ

Gereksinimler :
- 1
- 2

Devre kurulumu yapıldıktan sonra Python ve PHP kodları yazılır.

buton.py dosyası hakkında :
```
-Ana programımızdır

-Butonları kontrol eder

-Request ile veri çeker
```

senddata.py dosyası hakkında :
```
-FTP kullanarak uzak sunucuya dosya göndeririz.
```

Çalışması için Raspberry Pi 3 içinde yapılması gerekenler : 

Dosylaarın bir klasöre atılması gereklidir.

Crontab eklenmesi gerekir. Crontab kodumuz saatte bir uzak sunucuya FTP ile kayitlar.txt dosyasını göndermektedir.

Crontab eklemek için console ekranında "crontab -e" kodu çalıştırılır ve en alt satıra "0 * * * * python /home/pi/buton.oy" yazılması gerekir.

Not: Tırnak işaretleri yok ve /home/pi/ kısmı hangi klasöre attıysanız ona göre değiştiriniz.
