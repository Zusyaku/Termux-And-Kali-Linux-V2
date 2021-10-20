import os
for i in ["requests","bs4","html5lib","colorama","tqdm","cloudscraper"]:
    print("installing",i)
    os.system(f"pip3 install {i} -U")