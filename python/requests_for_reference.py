

import re
import requests
def get_reference(url, key, headers):
    r = requests.get(url, headers=headers, timeout=20)
    #print(r.status_code)
    # if  r.status_code == 200：
    t = r.text
    reference_list_raw = re.findall(compiles, t)
    for i in reference_list_raw:
        rm=re.sub('<.+?>','',i)
        print(f'{key}   ', rm)
        f.write(f'{key} ')
        f.write(f'{rm}')

with open('F:/ljy/atom/markerf.txt', encoding='utf-8') as m:
    marker_line = m.read().splitlines()
    compiles = re.compile('Reference</b></td></tr></table><td><table><tr>.+?\n')
    with open('F:/ljy/atom/reference1.txt', 'w', encoding='utf-8') as f:
        for i in marker_line:
            key = i
            headers = {'user-agent': "Chrome"}
            url = f"https://wheat.pw.usda.gov/cgi-bin/GG3/report.cgi?class=marker;query=*{key}*;name={key}"
            count =0
            while count < 5:
                try:

                    get_reference(url, key, headers)
                    count=6
                except:
                    count = count + 1
                if count ==5:
                    print(f"{key} is lost with five times of search.")
                    lost.write(f"{key}")
                    lost.write("\n")
