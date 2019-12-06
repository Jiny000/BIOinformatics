##read the markers from file and search in Graingenes.Each one seek for five times.
#If one makrer hasn't been found even by five times,it will be recorded in the file.
import re
import requests
def get_marker(url):
    r = requests.get(url, timeout=20)
    t = r.text
    seq_compiles = re.compile("PCR primers.+?\n")
    primer_list = re.findall(seq_compiles,t)
    if primer_list:
        for i in primer_list:
            primer = re.sub('<.+?>','',i)
            return primer






lost=open("f:/ljy/atom/lost.txt",'w',encoding='utf-8')

with open('F:/ljy/atom/markerf.txt', encoding='utf-8') as m:
    marker_line = m.read().splitlines()

    with open('F:/ljy/atom/primer1.txt', 'w', encoding='utf-8') as f:
        for i in marker_line:
            key = i
            headers = {'user-agent': "Chrome"}
            url = f"https://wheat.pw.usda.gov/cgi-bin/GG3/report.cgi?class=marker;query=*{key}*;name={key}"
            count =0
            while count < 5:
                try:

                    f.write(f'{key}:',get_marker(url))
                    count=6
                except:
                    count = count + 1
            if count ==5:
                print(f"{key} is lost with three times of search.")
                lost.write(f"{key}")
                lost.write("\n")

with open('F:/ljy/atom/marker2.txt', encoding='utf-8') as m:
    marker_line = m.read().splitlines()
    compiles = re.compile("5'.+?3'")
    with open('F:/ljy/atom/primer2.txt', 'w', encoding='utf-8') as f:
        for i in marker_line:
            key = i
            headers = {'user-agent': "Chrome"}
            url = f"https://wheat.pw.usda.gov/cgi-bin/GG3/report.cgi?class=marker;query=*{key}*;name={key}"
            count =0
            while count < 5:
                try:

                    f.write(f'{key}:',get_marker(url))
                    count=6
                except:
                    count = count + 1
            if count ==5:
                print(f"{key} is lost with five times of search.")
                lost.write(f"{key}")
                lost.write("\n")

lost.close()

print('OK!')
