import time, os, sys
os.system("clear")
print("If you have generated a banner file using generator.py or your banner is between 30th 35th line of file, you can use this.")
time.sleep(2)
path= input("\nEnter file name or path > ")
try:
    with open(path, 'r') as f3:
        lines = f3.readlines()
        with open(path, 'w') as f:
            lines [29] = "'\'\'+green+'\'\'"+ lines[29]
            lines [30] = "'\'\'+red+'\'\'"+ lines[30]
            lines [31] = "'\'\'+cyan+'\'\'"+ lines[31]
            lines [32] = "'\'\'+yellow+'\'\'"+ lines[32]
            lines [33] = "'\'\'+blue+'\'\'"+ lines[33]
            lines [34] = "'\'\'+purple+'\'\'"+ lines[34]
            lines [35] = "'\'\'+green+'\'\'"+ lines[35]
            f.writelines(lines)
            print("\nColor added successfully!")    
except:
    print("File not found.")