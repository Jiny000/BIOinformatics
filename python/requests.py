import re
import requests
def get_marker(url, key, headers):
    r = requests.get(url, headers=headers, timeout=20)
    print(r.status_code)
    # if  r.status_code == 200：
    t = r.text
    primer = re.findall(compiles, t)
    print(f'{key}', primer)
    f.write(f'{key}')
    f.write(f'{primer}')
    f.write('\n')

lost=open("f:/ljy/atom/lost.txt",'w',encoding='utf-8')

with open('F:/ljy/atom/markerf.txt', encoding='utf-8') as m:
    marker_line = m.read().splitlines()
    compiles = re.compile("5'.+?3'")
    with open('F:/ljy/atom/primer.txt', 'w', encoding='utf-8') as f:
        for i in marker_line:
            key = i
            headers = {'user-agent': "Chrome"}
            url = f"https://wheat.pw.usda.gov/cgi-bin/GG3/report.cgi?class=marker;query=*{key}*;name={key}"
            count =0
            while count < 5:
                try:

                    get_marker(url, key, headers)
                    count=6
                except:
                    count = count + 1
                if count ==5:
                    print(f"{key} is lost with three times of search.")
                    lost.write(f"{key}")

with open('F:/ljy/atom/marker2.txt', encoding='utf-8') as m:
    marker_line = m.read().splitlines()
    compiles = re.compile("5'.+?3'")
    with open('F:/ljy/atom/primer.txt', 'w', encoding='utf-8') as f:
        for i in marker_line:
            key = i
            headers = {'user-agent': "Chrome"}
            url = f"https://wheat.pw.usda.gov/cgi-bin/GG3/report.cgi?class=marker;query=*{key}*;name={key}"
            count =0
            while count < 5:
                try:

                    get_marker(url, key, headers)
                    count=6
                except:
                    count = count + 1
                if count ==5:
                    print(f"{key} is lost with five times of search.")
                    lost.write(f"{key}")



print('OK!')
