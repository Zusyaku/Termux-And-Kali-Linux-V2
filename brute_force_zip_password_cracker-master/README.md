# Cracking passwords made (stupidly) simple
Brute force zip files.

## NOTE
Since the rockyou.txt is approx. 133 MB, which is over Github's 25 MB file upload limit. You can download 'rockyou.txt' [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).

## Installation
- [zipfile2](https://pypi.org/project/zipfile2/): `pip install zipfile2`
- [tqdm](https://pypi.org/project/tqdm/): `pip install tqdm`

## Usage
1.fill out the path to the rockyou.txt file on line 5.\
2.fill out the path to the password protected zip file on line 6.

## Running the program
1.`cd PATH TO THE FOLDER WHERE THE PROGRAM IS STORED.py`\
2.`python brute_force_zip_1.py`
