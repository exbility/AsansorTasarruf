<?php

$saat = (int)$_GET["saat"];
$dosya = fopen('kayitlar.txt', 'r');
$icerik = fread($dosya, filesize('kayitlar.txt'));
fclose($dosya);

$bol = explode("\n",$icerik);

$dizi = array();
foreach ($bol as $islem)
{
	$bol2 = explode(" ",$islem);
	if($saat == $bol2[0])
	{
		$dizi[] = $bol2[1];
	}
}
sort($dizi);
$dizi = array_count_values ( $dizi );
$final=1;
$key = array_search(max($dizi), $dizi);
$final=["suankikat"=>$key];

//print_r(json_encode($final));
//print_r($dizi);
echo $key;

/* Random olusturma
for ($i=1;$i<25;$i++)
{
	for($j=1;$j<40;$j++)
	{
		$salla1 = rand(1,5);
		$salla2 = rand(1,5);
		if($salla1 != $salla2)echo $i." ".$salla1." ".$salla2."\n";
		
	}
}
*/
?>