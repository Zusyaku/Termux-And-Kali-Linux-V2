import tkinter as tk, subprocess, os, socket
from tkinter import filedialog
root= tk.Tk()
root.title("Local HTTP Server")
canvas1 = tk.Canvas(root, width = 400, height = 400)
canvas1.pack()
canvas1.create_text(200,70, text="Enter port no\n(Current:8000)")
entry1 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry1)
folder_selected = os.path.dirname(__file__)
def getFolderPath():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    canvas1.create_text(200, 190, text=folder_selected+"\n")   
def startftp ():
    port=entry1.get()
    os.chdir(folder_selected)
    subprocess.call("python -m http.server "+port)
canvas1.create_text(230, 130, text="Select Shared folder\n(Current-"+folder_selected+")")
getfolder = tk.Button(text="Select", command=getFolderPath)
canvas1.create_window(200, 160, window=getfolder)
start = tk.Button(text='Start FTP', command=startftp)
canvas1.create_window(200, 220, window=start)
canvas1.create_text(200, 330, text="Close cmd window after complete!")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(10)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    if (ip.find("192") != -1):
        canvas1.create_text(200, 250, text="Your local IP is:\n"+ip)
    if (ip.find("172") != -1):
        canvas1.create_text(200, 250, text="Your local IP is:\n"+ip)
except:
    canvas1.create_text(200, 250, text="Link Unavailable")
s.close()
canvas1.create_text(200, 300, text="Add \"http://\" before and \"port\" after your IP.")
root.mainloop()