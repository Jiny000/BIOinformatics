import re
import requests
with open('F:/ljy/atom/markerf.txt',encoding='utf-8') as m:
    marker_line=m.read().splitlines()
    compiles=re.compile("5'.+?3'")
    with open('F:/ljy/atom/primer.txt','w',encoding='utf-8') as f:
        for i in marker_line:
            key=i
            #try:
            r =requests.get(f"https://wheat.pw.usda.gov/cgi-bin/GG3/report.cgi?class=marker;query=*{key}*;name={key}")
            t = r.text
            primer=re.findall(compiles,t)
            print(f'{key}',primer)
            f.write(f'{key}')
            f.write(f'{primer}')
