<p align="center">
<img src="https://img.shields.io/badge/Python-3.9-brightgreen.svg?style=plastic">
<img src="https://img.shields.io/badge/OSINT-red.svg?style=plastic">

<p align="center">
    <a href="https://twitter.com/muhsobrimaulan1"><b>Twitter</b></a>
    <span> - </span>
    <a href="https://discord.gg/muhammadsobrimaulana"><b>Discord</b></a>
    <span> - </span>
    <a href="https://sobri3195.github.io/"><b>Pegasus Blog</b></a>
</p>

---

**Pegalou** adalah alat **OSINT** yang dibuat dengan python untuk menemukan profil berdasarkan nama pengguna. Nama pengguna yang diperiksa lebih dari 350 website dalam beberapa detik. Teknik ini untuk bisa mendapatkan hasil dengan lebih cepat sambil mempertahankan jumlah positifi palsu yang rendah.

Jika anda menyukai script ini, silahkan berikan **star** pada proyek ini :D

If you find any errors or false positives or if you want to suggest more websites feel free to open an issue.

## Features

* **Fast**, lookup can complete **under 20 seconds**
* Over **350** platforms are included
* Batch processing
    * Usernames can be provided from commandline
    * List of usernames can be provided from a file
* Results are automatically saved in txt file
* JSON and CSV file formats [Coming Soon]
* Proxy support [Coming Soon]
* Tor support [Coming Soon]

## Installation

```bash
git clone https://github.com/sobri3195/pegalou.git
cd pegalou
pip3 install -r requirements.txt
```

## Usage

```bash
python3 pegalou.py -h
usage: pegalou.py [-h] [-u U] [-d D [D ...]] [-f F] [-l L] [-t T] [-v]

pegalou - Find social media profiles on the web | v1.0.0

optional arguments:
  -h, --help    show this help message and exit
  -u U          Specify username
  -d D [D ...]  Specify DNS Servers [Default : 1.1.1.1]
  -f F          Specify a file containing username list
  -l L          Specify multiple comma separated usernames
  -t T          Specify timeout [Default : 20]
  -v            Prints version

# Single username
python3 pegalou.py -u username

# Multiple *comma* separated usernames
python3 pegalou.py -l "user1, user2"

# Username list in a file
python3 pegalou.py -f users.txt
```

## Usage
* Modified by dr. Muhammad Sobri Maulana, S.Kom, CEH, OSCP, OSCE