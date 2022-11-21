import requests as r
from bs4 import BeautifulSoup as bs
import random,string,time,re,sys,os
from concurrent.futures import ThreadPoolExecutor as tdp

uids=[]
n=0
c=0
file=input("Save file to : ")
if file=="":
    file="/sdcard/f.txt"

def gen(code,tt):
    for i in range(tt):
        uids.append(code+''.join(random.choice(string.digits) for _ in range(
        15-len(code)
        )))
        
def geno(code,l,tt):
    for i in range(tt):
        uids.append(code+''.join(random.choice(string.digits) for _ in range(
        l-len(code)
        )))


uao=open("/sdcard/1p.txt","r").read().splitlines()
"""def inputs():
    os.system("clear")
    code=input("Code: ")
    tt=int(input("Test ;"))
    for i in range(tt):
        uids.append(code+''.join(random.choice(string.digits) for _ in range(
        15-len(code)
        )))
    print(uids)"""

def getname(s,uid):
    global n,c
    ua=random.choice(uao)
    hd={'authority':'m.facebook.com',

           'method': 'GET',
            'user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
        
            
            }
    url="https://m.facebook.com/profile.php?id="+uid
    pi=s.get(url,headers=hd)
    bp=bs(pi.content,"html.parser")
    name=bp.find("title").text.split("|")[0].strip()
    if "Content not found" not in name and "Log in to Facebook" not in name:
        n+=1
        print(f"\033[1;32m{uid} {name} [{n}-{c}]")
        open(file,"a").write(uid+"|"+name+"\n")
    #else:
        #print(f"\033[1;34m\{uid} {name}")
    
    c+=1
    print(f'[CHECKED-%s]'%c,end="\r")

s=r.Session()

def run():
    with tdp(max_workers=30) as t:
        for uid in uids:
            t.submit(getname,s,uid)


while True:
    os.system("clear")
    code=input("Code: ")
    tt=int(input("Test ;"))
    if len(code)>=4:
        gen(code,tt)
    else:
        l=int(input("Uid length: "))
        geno(code,l,tt)
    run()
    print("Dumped ids are saved in: "+file)
    rr=input("Dump again? [Y or N]")
    if rr in ["Y","y"]:
        code=input("Code: ")
        tt=int(input("Test ;"))
        n=0
        c=0
        uids=[]
        gen(code,tt)
        print(len(uids))
        run()
    else:
        break
