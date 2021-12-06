import pytube,pyfiglet,os

print('Loading Downloads')

os.system('pip3 install pytube')
os.system('pkg install python3')
os.system('clear')

name = pyfiglet.figlet_format('YtDownload')
print(name)
print('Page   : Omen Latip\nGithub    : https://github.com/Latip176\nYoutube   : Omen Craft\n')
link = input('Link Videonya ➡ ')
print('Loading 3 Menitan...')

judul = pytube.YouTube(link).title
print('\nJudul Videonya: '+judul)

pytube.YouTube(link).streams.get_highest_resolution().download('/storage/emulated/0/download')
print('\nSucces Cek Folder Download Anda!\n')