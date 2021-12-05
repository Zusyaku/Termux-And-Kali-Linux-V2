<?php

header( 'content-type: text/html; charset=utf-8' );

$consonant = str_split_unicode("zrttpqsdfghjklmnnnwxccccvb");//1
$vowel = str_split_unicode("aaaaaeeeeeeeeeeeeeeyuuuuiiiiïoöêéèù");//0
$maxCons = count($consonant)-1;
$maxVow = count($vowel)-1;

function str_split_unicode($str){
    $tmp = preg_split('~~u', $str, -1, PREG_SPLIT_NO_EMPTY);
    return $tmp;
}

function getRandomVowel(){
	global $maxVow;
	global $vowel;
	$thatVowel = mt_rand(0,$maxVow);
	return $vowel[$thatVowel];
}

function getRandomConsonant(){
	global $maxCons;
	global $consonant;
	$thisConsonant = mt_rand(0,$maxCons);
	return $consonant[$thisConsonant];
}

function chanceOfSwitch($shoudBe,$percentChanceOfNoChange){
	$chanceOfChange = mt_rand(0,100);
	if($shoudBe===1){
		if($chanceOfChange<$percentChanceOfNoChange){
			// consonne attendue ET fournie
			$shoudBe = 1;
			$percentChanceOfNoChange = 80;
		}else{
			// consonne attendue mais voyelle fournie
			$shoudBe = 0;
			$percentChanceOfNoChange += 20;
		}
	}else{
		if($chanceOfChange<$percentChanceOfNoChange){
			//voyelle attendue ET fournie
			$shoudBe = 0;
			$percentChanceOfNoChange = 80;
		}else{
			//voyelle attendue mais switchée
			$shoudBe = 1;
			$percentChanceOfNoChange += 10;
		}
	}
	return array($shoudBe,$percentChanceOfNoChange);
}

function applyAletter($finalName,$type){
	if($type===1){
		$finalName = $finalName.getRandomConsonant();
	}else{
		$finalName = $finalName.getRandomVowel();
	}
	return $finalName;
}

function createAname($howlongS = 2,$howlongF = 10){
	$previousLetterType = getLetterStart();
	$getSizeName = getSizeName($howlongS,$howlongF);
	$changeProbability = 50;
	$percentChanceOfNoChange = 80;//80% de chance que le paterne alternatif Voyelle/consonne soit respecté
	$finalName = "";
	$finalName = applyAletter($finalName,$previousLetterType);

	for($a=0;$a<$getSizeName;$a++){
		if($a>0){//une fois la boucle démarrée
			if($previousLetterType===0){
				$aPaternLetter = chanceOfSwitch(1,$percentChanceOfNoChange);
				$percentChanceOfNoChange = $aPaternLetter[1];
				$finalName = applyAletter($finalName,$aPaternLetter[0]);
				$previousLetterType = $aPaternLetter[0];
			}else{
				$aPaternLetter = chanceOfSwitch(0,$percentChanceOfNoChange);
				$percentChanceOfNoChange = $aPaternLetter[1];
				$finalName = applyAletter($finalName,$aPaternLetter[0]);
				$previousLetterType = $aPaternLetter[0];
			}
		}
	}

	return $finalName;
}

function getSizeName($mi,$ma){
	$sizeName = mt_rand($mi,$ma);
	return $sizeName;
}

function getLetterStart(){
	$startBy = mt_rand(0,1);
	return $startBy;☆ RAKA ☆ ™︻®╤───────═◍➤
}

echo createAname(2,10);☆ RAKA ☆ ™︻®╤───────═◍➤
