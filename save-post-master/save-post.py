import argparse
import re
import sys
import requests



def fetchDP(username):
    url = "https://www.instagram.com/{}/?__a=1".format(username)

    r = requests.get(url)

    if r.ok:
        data = r.json()
        return data['graphql']['user']['profile_pic_url_hd']

    else:
        print("\033[1;31m✘ Cannot find user ID \033[1;m")
        sys.exit()


def main():
    parser = argparse.ArgumentParser(
        description="Download any users Instagram display picture/profile picture in full quality")



    args = parser.parse_args()

    username = input('\033[1;37musername : \033[1;m')

    file_url = fetchDP(username)
    fname = username + ".jpg"

    r = requests.get(file_url, stream=True)
    if r.ok:
        with open(fname, 'wb') as f:
            f.write(r.content)
            print("\033[1;37m✔ Downloaded :{} \033[1;m".format(fname))
    else:
        print("Cannot make connection to download image")


if __name__ == "__main__":
    main()
