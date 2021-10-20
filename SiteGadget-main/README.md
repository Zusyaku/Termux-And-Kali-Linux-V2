[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# SiteGadget
A cross-platform python based utility for information gathering! Hi, Inspector Gadget...

 Help me develop the tool and check the To-Do list :pray:
 
 #### :briefcase: Features:
  - IP Lookup
    - Location
    - Related emails
    - Subdomains
    - CloudFlare Check :cloud:
    - Robot.txt Check 
  - DNS Lookup
  - Reverse IP Lookup
  - HTTP Headers
  - [API] Detect CMS
  - [API] Find related emails
  - Scraping The Links
  - Port Scan
  - Find Admin Panel
  - Find Shell

:bangbang: You can turn features on off from the `config.json` :bangbang:

```json
[
  {
    "Tree": "True",
    "DNS Lookup": "True",
    "HTTP Headers": "True",
    "Reverse IP Lookup": "True",
    "whatcms.org API": "set API KEY Here",
    "hunter.io API": "set API KEY Here",
    "Scraping The Links": "True",
    "Port Scan": "True",
    "Find Admin Panel": "True",
    "Find Shell": "True"
  }
]

```

## :key: API Key:
**[not required to run the program]**

https://whatcms.org/ --> API Integration
You can detect Content Management Systems

https://hunter.io/ --> API Integration
You can show the emails related to the domain

#### For Use:
Save your API keys in the `config.json`


## :package: Cloning:
`git clone https://github.com/alpkeskin/SiteGadget.git`

## :shipit: Usage:
`cd SiteGadget`

`pip3 install -r requirements.txt`

- You can edit the `Config.json` file

`python3 run.py`

- Then, set the domain (i.e : nasa.gov, google.com...)

## :computer: Screen:
```python
  ______ _                _______           _                   
 / _____|_)  _           (_______)         | |              _   
( (____  _ _| |_ _____    _   ___ _____  __| | ____ _____ _| |_ 
 \____ \| (_   _) ___ |  | | (_  (____ |/ _  |/ _  | ___ (_   _)
 _____) ) | | |_| ____|  | |___) / ___ ( (_| ( (_| | ____| | |_ 
(______/|_|  \__)_____)   \_____/\_____|\____|\___ |_____)  \__)
                                             (_____|v1.0 
https://github.com/alpkeskin    

SITE >
```
#### :eyes: Example Output :
<a href="https://github.com/alpkeskin/SiteGadget/blob/main/insides/output.txt" target="_blank">SiteGadget's Full Output</a>

### :money_with_wings: My Bitcoin Wallet:
`3NFfd1QXUVFsZzfbwGJiAJdehtPB9D88tK`

#### :white_check_mark: Tested on :
- Kali Linux
- MacOS

#### To-Do List :
- [ ] Demo Video
- [ ] Add -> Whois query
- [ ] Add -> scan used technologies
- [ ] Add -> Really useful API's
- [ ] Improve The Codes

<h1 align="center">
  <br>
  <a href="https://github.com/alpkeskin/SiteGadget"><img src="https://i.imgur.com/HVp1Khw.png" alt="Site Gadget"></a>
</h1>
