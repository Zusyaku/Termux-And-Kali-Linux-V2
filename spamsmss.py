import requests,os,sys,time
from time import sleep
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def baner():
    clear()
    print(f"""
  {p}╔═╗┌─┐┌─┐┌┬┐  {c}┌─┐┌┬┐┌─┐
  {p}╚═╗├─┘├─┤│││  {c}└─┐│││└─┐
  {p}╚═╝┴  ┴ ┴┴ ┴  {c}└─┘┴ ┴└─┘{p}{g}
https://ainxbot-id.herokuapp.com
{ab}--------------------------------{d}""")
def cblg():
    lg=input(f"{pr}Coba lagi? ({d}{c}y{d}/{c}n{p}) : {c}")
    if lg == "y" or lg == "Y":
       sleep(10)
       os.system("python run.py")
    elif lg == "n" or lg == "N":
       sys.exit(f"{er}Bye bro jangan lupa kasih bintang github saya:)")
    else:
       print(f"{er}Ngetik yang bener coeg")
       cblg()

def spam(nomor):
    req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
    if "terkirim" in req:
       print(f"{dn}Spam ke {c}{nomor} berhasil")
    else:
       print(f"{er}Spam ke {c}{nomor} gagal")
if __name__=="__main__":
    baner()
    nomor=input(f"{er}Put your number,example : {c}8xxx {p}tanpa 0/62\n{er}Limit : 3x\n{pr}{ab} >>> {c}")
    spam(nomor)
    cblg()
