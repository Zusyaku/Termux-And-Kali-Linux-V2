# vsco-dl
> Download all of the images and videos from a VSCO user

<p align="center">
<a href="https://asciinema.org/a/196264">
<img src="https://asciinema.org/a/196264.png" width="595px" height="auto">
</a>
</p>

## :floppy_disk: Installation

```bash
# clone the repo
$ git clone https://github.com/sdushantha/vsco-dl.git

# or download the raw Python file
$ curl https://raw.githubusercontent.com/sdushantha/vsco-dl/master/vsco-dl.py --output vsco-dl.py

# install the requirements
$ pip3 install requests colorama

# run the program using Python 3
$ python3 vsco-dl.py ...
```

## :hammer: Usage
```
usage: vsco-dl.py [-h] [--content CONTENT] username pages

Download all of the images and videos from a VSCO user

positional arguments:
  username           Username of VSCO user
  pages              Number of pages the user has

optional arguments:
  -h, --help         show this help message and exit
  --content CONTENT  Option to download only videos (video) or photos (photo)

```

## :scroll: License
MIT License

Copyright (c) 2018 Siddharth Dushantha
