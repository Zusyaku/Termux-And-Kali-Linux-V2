#Open source
#Asal luh chat gueh Aldi Sad mulu 🙂
#!/bin/bash
echo
echo -e "\033[1;97m  _    _ _______ __  __ _       "
echo -e " | |  | |__   __|  \/  | |      "
echo -e " | |__| |  | |  | \  / | |      "
echo -e " |  __  |  | |  | |\/| | |      "
echo -e " | |  | |  | |  | |  | | |____  "
echo -e " |_|  |_|  |_|  |_|  |_|______| "
echo
echo -e " Creator : Aldi Bachtiar Rifai"
echo
echo -e " [!] Contoh : Script ngga usah ada tulisa (.html) "
read -p ' [!] Nama file   : ' nama
echo
echo -e " [!] Buat Upload foto/lagu"
echo -e " [!] link :  https://top4top.io/"
echo
read -p ' [!] Judul       : ' judul
read -p ' [!] Link Gambar : ' gambar
read -p ' [!] Hacker by   : ' hack
read -p ' [!] Pesan       : ' pes
read -p ' [!] Thanks to   : ' tank
read -p ' [!] Link lagu   : ' lagu
cd $HOME
cat <<LOGIN>$nama.html
<!DOCTYPE html>
<html>
<head>
	<title>$judul</title>
<meta name='description' content='[ Your Site Not Safe]'> <meta name='keywords' content='[ERROR THE SYSTEM]'>
	<link href='https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap' rel='stylesheet'>
	<link href='https://fonts.googleapis.com/css2?family=Metal+Mania&display=swap' rel='stylesheet'>
	<link href='https://fonts.googleapis.com/css2?family=Indie+Flower&family=Metal+Mania&display=swap' rel='stylesheet'>
	<link href='https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap' rel='stylesheet'> 
	<script language=JavaScript> message='White Cyber Illusion';function clickIE4(){if (event.button==2){alert(message);return false;}}function clickNS4(e){if (document.layers||document.getElementById&&!document.all){if (e.which==2||e.which==3){alert(message);return false;}}}if (document.layers){document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS4;}else if (document.all&&!document.getElementById){document.onmousedown=clickIE4;}document.oncontextmenu=new Function('alert(message);return false')// --></script> 
	<style type='text/css'>
		body{
			background:url(https://f.top4top.io/p_1577h5txv0.gif);
		}
		.shining {
		font-size: 25px;
		font-family: Gloria Hallelujah;
		  text-align:center;
		  text-transform:uppercase;
		  letter-spacing:5px;
		  background:linear-gradient(90deg, #000,#f5f5f5,#000);
		  -webkit-background-clip:text;
		  -webkit-text-fill-color:transparent;
		  background-repeat:no-repeat;
		  background-size:80%;
		  position:relative;
		  animation:shine 6s ease-in-out infinite;
}
.shining h1{
		font-size: 50px;
}
@keyframes shine {
  from {
    background-position-x:-500%;
  }
  to {
    background-position-x:500%;
  }
}
p{
	font-size: 15px;
	font-family: Indie Flower;
	color: white;
}
	</style>
</head>
<body>
	<center>
		<br>
		<br>
		<br>
		<br>
		<br>
		<br>
		<br>
<img src='$gambar'width='450' height='400'>
	
	<div class='shining'>
<h1 color='red'>Hacked by $hack</h1>
	</div>
<!--
.ahgcrewstyle {
        color: #F00;
}
/.ahg {
        color: #0F0;
}
#message font strong {
        font-family: Tahoma, Geneva, sans-serif;
        font-size: 18px;
}
.gre {
        color: #9F3;
        font-size: 36px;
}
#message font {
        font-size: 16px;
}
-->
</style>
</head><body alink='gray' bgcolor='black' vlink='gray' link='gray' text='gray'>
<p></p><center>
<center></center>
<script type='text/javascript'>
TypingText = function(element, interval, cursor, finishedCallback) {
  if((typeof document.getElementById == 'undefined') || (typeof element.innerHTML == 'undefined')) {
    this.running = true;
    return;
  }
  this.element = element;
  this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });
  this.interval = (typeof interval == 'undefined' ? 100 : interval);
  this.origText = this.element.innerHTML;
  this.unparsedOrigText = this.origText;
  this.cursor = (cursor ? cursor : '');
  this.currentText = '';
  this.currentChar = 0;
  this.element.typingText = this;
  if(this.element.id == '') this.element.id = 'typingtext' + TypingText.currentIndex++;
  TypingText.all.push(this);
  this.running = false;
  this.inTag = false;
  this.tagBuffer = '';
  this.inHTMLEntity = false;
  this.HTMLEntityBuffer = '';
}
TypingText.all = new Array();
TypingText.currentIndex = 0;
TypingText.runAll = function() {
  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();
}
TypingText.prototype.run = function() {
 if(this.running) return;
 if(typeof this.origText == 'undefined') {
   setTimeout('document.getElementById('' + this.element.id + '').typingText.run()', this.interval);
   return;
 }
 if(this.currentText == '') this.element.innerHTML = '';
 if(this.currentChar < this.origText.length) {
   if(this.origText.charAt(this.currentChar) == '<' && !this.inTag) {
     this.tagBuffer = '<';
     this.inTag = true;
     this.currentChar++;
     this.run();
     return;
   } else if(this.origText.charAt(this.currentChar) == '>' && this.inTag) {
     this.tagBuffer += '>';
      this.inTag = false;
      this.currentText += this.tagBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inTag) {
      this.tagBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == '&' && !this.inHTMLEntity) {
     this.HTMLEntityBuffer = '&';
      this.inHTMLEntity = true;
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == ';' && this.inHTMLEntity) {
     this.HTMLEntityBuffer += ';';
      this.inHTMLEntity = false;
      this.currentText += this.HTMLEntityBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inHTMLEntity) {
      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else {
      this.currentText += this.origText.charAt(this.currentChar);
    }
    this.element.innerHTML = this.currentText;
    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == 'function' ? this.cursor(this.currentText) : this.cursor) : '');
   this.currentChar++;
   setTimeout('document.getElementById('' + this.element.id + '').typingText.run()', this.interval);
 } else {
        this.currentText = '';
        this.currentChar = 0;
       this.running = false;
       this.finishedCallback();
 }
}
</script>
<center>
  <b class='Gre'>From Newbie To Mastah</b>
  <br>
  <font>
</font><p id='message'><font> <strong><br> $pes <br>
 <br>
  </strong><br>
<br>
We Are  <span class='ahgcrewstyle'><strong><strong> Legion </strong></strong></span><strong> </strong> <br>
</font></p>
<p align='center'><em></em> <b><font size='10'><span class='ahgcrewstyle'></span></font></b></p>
<p><font><br></font></p>
 <br>
 <p align='center'><font color='red' size='5' face='Times New Roman'> </font><br><br><br><br><br><br></p>
<body>
	<br>
        <marquee direction='right' ><font face='Courier' color='red' size='5'>[] $tank []</font></marquee>
	<br>
	
	

	<iframe width='200' height='100' scrolling='no' frameborder='no' allow='autoplay' src='$lagu'></iframe>
	</center>
</body>
</html>
<script>(function(d, s, id) {
 var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = '//connect.facebook.net/en_US/all.js#xfbml=1&appId=384191914936497';
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
<p align='center'><font size='+8' face='Times New Roman'><font color='green'><font color='white'>  <font color='red'> </font></font></font></font></p>
<script>alert{} PROGRAMER BY ./randiXploit{}</script>
<p align='center'> <img > </p>
  <script type='text/javascript'>
new TypingText(document.getElementById('message'), 50, function(i){ var ar = new Array('\\', '|', '/', '-'); return ' ' + ar[i.length % ar.length]; });
//Type out examples:
TypingText.runAll();
  </script>
</font></p>
<center></center>
<br>
</br>
</body></html>
<!-- aghaze larzeshe safhe-->
<meta http-equiv='Content-Language' content='en-us'>
<SCRIPT language=JavaScript>
<!-- Begin
function shake(n) {
if (parent.moveBy) {
for (i = 10; i > 0; i--) {
for (j = n; j > 0; j--) {
parent.moveBy(-i,0);
parent.moveBy(0,-i);
parent.moveBy(-i,0);
parent.moveBy(0,i);
parent.moveBy(i,0);
parent.moveBy(0,-i);
parent.moveBy(-i,0);
parent.moveBy(0,i);
parent.moveBy(i,0);
parent.moveBy(0,-i);
parent.moveBy(-i,0);
parent.moveBy(0,-i);
parent.moveBy(i,0);
parent.moveBy(0,i);
parent.moveBy(i,0);
parent.moveBy(0,i);
        }
     }
  }
}
//  End -->
<!--
shake(1);
//-->
</SCRIPT>
<!-- p align='center'><font size='7' color='#FF0000'>chi?</font></p> -->
<!--payan--></SCRIPT>
</body>
</html>
</body>
</html>
<P align=center></P>
<body bgcolor='#333366' background='' text='#FFFFFF' link='#0066CC' vlink='#999999' alink='#993300' style=''><style>
body {
    padding:0;
    margin:0;
    background-image:;
    background-repeat: no-repeat;
    background-position:top;
background-color: black;
color: white;
font: normal 110% courier;
margin-top: 5px;
margin-left: 5px;
padding: 0;
margin-right: 5px;
}
td{font-family: verdana; font-size: 20pt; color: green}
a{font-family: verdana; font-size: 30pt; color: silver}
</style>
<center><img src=''></center>
<style>
#navbar-iframe {
display: none;
<style>
</div>
<style>
.animasi {
  color: #EBE3AA;
  font-family:sans-serif;
  font-weight:lighter;
  font-size: 2em;
  white-space: nowrap;
  overflow: hidden;
  width: 30em;
  animation: keyframes 5s steps(500) infinite;
}
@keyframes keyframes{
 
  from{ width: 0px;}
 
}
</style>
 
<link href='http://fonts.googleapis.com/css?family=Bevan' rel='stylesheet' type='text/css'>
</head>
</body>
</DOCTYPE>
<div class='animasi'>
LOGIN
cp -f $nama.html /sdcard
echo
echo -e " [✓] Nama Sc $nama.html | Tersimpan di sdcard"
