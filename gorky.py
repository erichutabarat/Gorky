import requests
import random
import urllib.parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import time
import ast

glist = ['www.google.com.ph','www.google.com.pk','www.google.pl','www.google.pn','www.google.com.pr','www.google.ps','www.google.pt','www.google.com.py','www.google.com.qa','www.google.ro','www.google.ru','www.google.rw','www.google.com.sa','www.google.com.sb','www.google.sc','www.google.se','www.google.com.sg','www.google.sh','www.google.si','www.google.sk','www.google.com.sl','www.google.sn','www.google.so','www.google.sm','www.google.sr','www.google.st','www.google.com.sv','www.google.td','www.google.tg','www.google.co.th','www.google.com.tj','www.google.tl','www.google.tm','www.google.tn','www.google.to','www.google.com.tr','www.google.tt','www.google.com.tw','www.google.co.tz','www.google.com.ua','www.google.co.ug','www.google.co.uk','www.google.com.uy','www.google.co.uz','www.google.com.vc','www.google.co.ve','www.google.vg','www.google.co.vi','www.google.com.vn','www.google.vu','www.google.ws','www.google.rs','www.google.co.za','www.google.co.zm','www.google.co.zw','www.google.cat']
cleankeyword = ['What date is it now', 'Who is the creator of google', 'What time is it now','When was google created','When was facebook created','Who is the richest man','When was SpaceX created']
dirtyglist = glist

#Gorky Banner
def gorkybanner():
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("================================")
  print("|    Gorky  - Google Dorker    |")
  print("| Version : 1            |")
  print("| https://github.com/ericgans")
  print("| .                            .")
  print("")
  print("===============================")
# Blacklist domain
bl = open('blacklist.txt', 'r')
blacklist = bl.read().split('\n')
# gugelinit
def gugelsinit():
  global servergi
  global randomg
  global cookiezinit
  timeinit = []
  glists = random.shuffle(glist)
  cleankeywords = random.shuffle(cleankeyword)
  kwenc = urllib.parse.quote(random.choice(cleankeyword))
  randomg = random.choice(glist)
  headerzinit = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
  }

  #  COOKIES
  cfiles = open('Cookies.txt', 'r').read()
  cookiezinit = ast.literal_eval(cfiles)
  # Start Gugelinit
  gugelinit = requests.Session()
  gugelinit = requests.get('https://'+randomg+'/search?q='+kwenc+'&oq='+kwenc, cookies=cookiezinit, allow_redirects=True,headers=headerzinit)
  servergi = gugelinit.headers['Server']


# Grabbing next page result
def nextpage(url, cookie,head):
  npreq = requests.Session()
  npreq = requests.get('https://'+url, allow_redirects=True, cookies=cookie, headers=head)
  npsoup = BeautifulSoup(npreq.text, 'html.parser')
  np2ahref = npsoup.find_all("a")
  np2ahrefs = []
  np2urlq = []
  np2searchq = []
  np2sites = []
  np2linknext = []
  checkdupli = open('result.txt', 'r')
  checkduplis = checkdupli.read().split('\n')
  for ss in np2ahref:
    np2ahrefs.append(ss['href'])
  for i in np2ahrefs:
    if '/url?q=' in i:
      np2urlq.append(i)
    elif '/search?q=' in i:
     np2searchq.append(i)
  # Extract sites result from Next page (page2)
  for z in np2urlq:
    zz = z.replace('/url?q=', '')
    zzz = urlparse(zz)
    np2sites.append(zzz.scheme+'://'+zzz.netloc)
  # Print sites result from next page
  np2sites1 = list(set(np2sites))
  for y in np2sites1:
    if any(s in y for s in blacklist):
      pass
    else:
      if y in checkduplis:
        pass
      else:  
        print(y)
        npsavefiles = open('result.txt', 'a')
        npsavefiles.write(y+'\n')
        npsavefiles.close()


def gugelsearch(que):
  global headersgs
  global linknextpage
  global npcookie
  gugelsinit()
  ua1 = ['Mozilla/5.0 (Windows 98; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0','Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0','Mozilla/5.0 (Windows NT 5.1; rv:1.9a1) Gecko/20060217 Firefox/1.6a1','Mozilla/5.0 (Windows NT 5.1; rv:2.0b13pre) Gecko/20110223 Firefox/4.0b13pre','Mozilla/5.0 (Windows NT 5.1; rv:2.0b9pre) Gecko/20110105 Firefox/4.0b9pre','Mozilla/5.0 (Windows NT 5.1; rv:2.0b8pre) Gecko/20101127 Firefox/4.0b8pre','Mozilla/5.0 (Windows NT 5.1; rv:6.0) Gecko/20100101 Firefox/6.0 FirePHP/0.6','Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.8.0) Gecko/20060728 Firefox/1.5.0','Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0','Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0','Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.8.1) Gecko/20091102 Firefox/3.5.5','Mozilla/5.0 (Windows NT 5.1; U; tr; rv:1.8.0) Gecko/20060728 Firefox/1.5.0','Mozilla/5.0 (Windows NT 6.0; U; sv; rv:1.8.1) Gecko/20061208 Firefox/2.0.0','Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0','Mozilla/5.0 (Windows NT 6.0; U; hu; rv:1.8.1) Gecko/20061208 Firefox/2.0.0','Mozilla/5.0 (Windows NT 6.0; U; tr; rv:1.8.1) Gecko/20061208 Firefox/2.0.0','Mozilla/5.0 (Windows NT 5.2; U; de; rv:1.8.0) Gecko/20060728 Firefox/1.5.0','Mozilla/5.0 (Windows NT 5.2; rv:2.0b13pre) Gecko/20110304 Firefox/4.0b13pre','Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13','Mozilla/5.0 (Windows; U; Windows NT 6.1; it-IT) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.25 Safari/532.5','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.71 (KHTML like Gecko) WebVideo/1.0.1.10 Version/7.0 Safari/537.71']
  randomua = random.choice(ua1)
  quenc = urllib.parse.quote(que)
  gsreq = requests.Session()
  headersgs = {
  'User-Agent' : randomua,
  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Encoding' : 'gzip, deflate, br',
  'Accept-Language' : 'en-US,en;q=0.5',
  'Connection' : 'keep-alive'
  }
  gsreq = requests.get('https://'+randomg+'/search?q='+quenc+'&oq='+quenc+'&sclient='+servergi+'-wiz', cookies=cookiezinit, allow_redirects=True, headers=headersgs)
  gssoup = BeautifulSoup(gsreq.text, 'html.parser')
  ahrefall = gssoup.find_all("a")
  ahrefalls = []
  urlq = []
  urlqs = []
  searchq = []
  linknextpage = []
  cd = open('result.txt', 'r')
  cdl = cd.read().split('\n')
  npcookie = gsreq.cookies.get_dict()
  for a in ahrefall:
    ahrefalls.append(a['href'])
  for sortahref in ahrefalls:
    if '/url?q=' in sortahref:
      urlq.append(sortahref)
    elif '/search?q=' in sortahref:
      searchq.append(sortahref)
  for s in searchq:
    if 'start=' in s:
      linknextpage.append(randomg+s)
  for o in urlq:
    oo = o.replace('/url?q=', '')
    ooo = urlparse(oo)
    urlqs.append(ooo.scheme+'://'+ooo.netloc)
  # Print the sites result and saved to result.txt
  for j in urlqs:
      print(j)
  urlqs = list(set(urlqs))
  # Detecting Google Captcha and trying again..
  if len(urlqs) == 0:
    print("[  Google Captcha detected..  ]")
    print(" Please solve Google Captcha in your browser then grab and rewrite your cookies into Cookies.txt ")
    pass
  else:
    for k in urlqs:
      if any(bl in k for bl in blacklist):
        pass
      else:
        if k in cdl:
          pass
        else:
          savefiles = open('result.txt','a')
          savefiles.write(k+'\n')
          savefiles.close()  
    linknextpage = list(set(linknextpage))    
    # Grabbing sites result in the next page
    print('  Grabbing in the next page ...')
    time.sleep(1.5)
    for npages in range(len(linknextpage)):
      nextpage(linknextpage[npages],cookiezinit,headersgs)

gorkybanner()
dlist = input("  Give me your Google dork list :  ")
dlists = open(dlist,'r')
dlists1 = dlists.read().split('\n')

# START Google Dorker
for t in range(len(dlists1)):
  gugelsearch(dlists1[t])

