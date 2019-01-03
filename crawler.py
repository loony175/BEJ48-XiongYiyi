#!/usr/bin/env python3

import base64
import bs4
import json
import requests

BASE_URL=base64.b64decode('aHR0cDovL3d3LnNlbXYubWUvaW1hZ2VzL3Nob3cvaWQvODQuaHRtbA==').decode()

def main():
    urls={}
    for page in range(1,51):
        while True:
            try:
                resp=requests.get(BASE_URL,params={'page':page})
                if resp.status_code==200:
                    break
            except Exception:
                pass
        items=bs4.BeautifulSoup(resp.text,'html.parser').find_all('img')
        for item in items:
            try:
                urls[item['alt']]=base64.b64encode(item['src'].encode()).decode()
            except KeyError:
                pass
        print('Crawling page %d succeeded.'%page)
    f=open('urls.json','w')
    f.write(json.dumps(urls,indent=2))
    f.write('\n')
    f.close()

if __name__=='__main__':
    main()
