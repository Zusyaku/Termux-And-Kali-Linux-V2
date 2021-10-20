import re
import requests
import json
import urllib.request
import os
import sys
from random import random
from colorama import init
import argparse

# This magic spell lets me erase the current line. 
# I can use this to show for example "Downloading..."
# and then "Downloaded" on the line where 
# "Downloading..." was.  
ERASE_LINE = '\x1b[2K'
CURSOR_UP_ONE = '\x1b[1A'

def download(username, html, content_type):

        # This is extracts the JSON data from the HTML page
        data = re.findall('window.__PRELOADED_STATE__ = (.*?)</script>', html)[0]

        array = json.loads(data).get("medias").get("byId")

        for content in array:
            
            file_url = array.get(content).get("media").get("videoUrl")
            
            # If there is not video, then look for the image
            if file_url == None:
                file_url = array.get(content).get("media").get("responsiveUrl")
            
            # Need to have https:// to have valid url
            file_url = "https://"+file_url
            
            # The file name is just some random number and the filename
            # gotton from the url. That is because some of the files
            # have the same names and this will cause issues
            fname = str(random())[3:9]+file_url.split("/")[-1]
            dir_name = username+"/"
            path = dir_name+fname

            if (("mp4" in fname and "video" in content_type)
                or ("jpg" in fname and "photo" in content_type)
                or ("CONTENT" in content_type)):
                    urllib.request.urlretrieve(file_url, path)

                    # This will let me show the output on the same line
                    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

                    print("\033[92m✔ Downloaded:\033[0m {}".format(path.replace(dir_name, "")))


def main():
        
        parser = argparse.ArgumentParser(description = "Download all of the images and videos from a VSCO user")

        parser.add_argument('username', action="store", help="Username of VSCO user")

        parser.add_argument('pages', action="store", help="Number of pages the user has", type=int)

        parser.add_argument('--content', action="store",
                            help="Option to download only videos (video) or photos (photo)")

        args = parser.parse_args()

        if args.content == None:
                args.content = "CONTENT"


        for page in range(args.pages):
                url ="https://vsco.co/{}/images/{}"

                r = requests.get(url.format(args.username, page+1))

                if r.status_code == 404:
                        print("\033[91m✘ Invalid username\033[0m")
                        sys.exit()

                print("\033[92m✔ Fetched data\n\033[0m")
                os.makedirs(args.username, exist_ok=True)
                html = r.text
                
                download(username=args.username, html=html, content_type=args.content)
                print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + CURSOR_UP_ONE)
	
        if "video" in args.content and not os.listdir(args.username):
                os.rmdir(args.username)
                print("\033[91m✘ No videos found\033[0m")
        else:
                print("\033[92m✔\033[0m Download is complete")

init()
main()
