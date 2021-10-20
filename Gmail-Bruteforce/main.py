from Core.gmailBrute import login 
from Core.header import header
print(header)
operation = input("Select action\n\n1-)Gmail Brute Force\n2-)Yandex Brute Force\nChoose:")
if operation=="1":
    data = input("1-)Mini Data\n2-)Big Data\n3-)Add yourself\nChoose:")
    if data=="1":
        login()
    elif data=="2":
        login("Data\\BigData.txt")
    elif data=="3":
        data = input("Enter the txt name(Text file must be in the Data folder):")
        if data.endswith(".txt"):
            login("Data\\{0}".format(data))
        else:
            login("Data\\{0}".format(data)+".txt")

elif operation=="2":
    pass