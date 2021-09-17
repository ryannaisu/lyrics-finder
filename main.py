import requests as req
import os
from bs4 import BeautifulSoup as soup
from dexcolors import *
request = req.Session()
PATH = '/sdcard/download/lrcfinder/'
MAIN_URL = 'https://www.megalobiz.com'

LOGO = f"""
______________________________________________________
                                            
               This is a Lyrics Finder
         Free to use and Open Source Project.
      
  [{r('#')}] Author: {g('TGM MASTER ( The Genjot Memek Master )')}
  [{r('#')}] Github: {g('https://github.com/')}
  [{r('#')}] Facebook: {g('https://www.facebook.com/ryan.naisu.7')}
  [{r('#')}] Team: {g('No Team im Solo')}
  [{r('#')}] Made with: {g('Python')}
                                            
------------------------------------------------------
            \\   ^__^
             \\  (oo)\\_______
                (__)\\       )\\/\\
                    ||----w |
                    ||     ||
                                     
"""

if os.path.exists(PATH) is False:
 os.mkdir(PATH)

def getList(key):
 html = soup(request.get(MAIN_URL+'/search/all?qry='+key.replace(' ', '%20')).text, 'html.parser')
 return html.find_all('a', {'class': 'entity_name'})

def saveLrc(url, filename):
 html = soup(request.get(url).text, 'html.parser')
 lrc = html.find('div', {'class': 'lyrics_details'}).find('span')
 with open(PATH+filename, 'wb') as file:
  file.write(lrc.text.encode())
 print(f"[{g('#')}] Successfully Downloaded {PATH+filename}")
 
if __name__ == '__main__':
 print(LOGO)
 input1 = input(f"[{c('?')}] Enter Song Title: ")
 data = getList(input1)
 print(f"""
 
        Founded {g(len(data))} Total Lyrics
 
 """)
 for i in range(len(data)):
  if '[' in data[i]['title']:
   print(f"[{g(i + 1)}] {data[i].string.strip()}")
 input2 = int(input(f"\n[{c('?')}] Select: ")) - 1
 saveLrc(MAIN_URL+data[input2]['href'], data[input2]['name']+'.lrc')