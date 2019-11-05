import re
import requests
with open('F:/ljy/atom/markerf.txt',encoding='utf-8') as m:
    marker_line=m.read().splitlines()
    compiles=re.compile("5'.+?3'")
    with open('F:/ljy/atom/primer.txt','w',encoding='utf-8') as f:
        for i in marker_line:
            key=i
            headers ={'user-agent':"Chrome"}
            url=f"https://wheat.pw.usda.gov/cgi-bin/GG3/report.cgi?class=marker;query=*{key}*;name={key}"
            try:
                if count<3:
                count=count+1
                get_marker(url,key,headers)
            except :
                print(f"{key} is Invalid connect")
                f.write(f"{key} is lost.")
                f.write('\n')

def get_marker(url,key,headers):
    r =requests.get(url,headers=headers,timeout=10)
    print(r.status_code)
    #if  r.status_code == 200：
    t = r.text
    primer=re.findall(compiles,t)
    print(f'{key}',primer)
    f.write(f'{key}')
    f.write(f'{primer}')
    f.write('\n')
