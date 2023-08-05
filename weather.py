from import_xyz import import_xyz
#import_xyz("beautifulsoup4")
import_xyz("requests")
import_xyz("requests_html")

from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def find_weather(query = 'kathmandu'):
    url = f'https://www.google.com/search?q={query}+weather'
    print(url)
    head={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    s = HTMLSession()
    try:
        r=s.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"})
        
        title=r.html.find('title',first = True).text
        samaya = r.html.find('div.VQF4g ', first = True).find('#wob_dts',first = True).text
        temp=r.html.find('span#wob_tm',first = True).text
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t',first = True).text
        #print( "current temperature", temp ,unit)
        mausam=r.html.find('div.VQF4g ', first = True).find('#wob_loc',first = True).text
        weather_state=r.html.find('div.VQF4g', first = True).find('span#wob_dc',first = True).text
        #print(mausam, " :",  weather_state)
        #print(samaya)
        
        
        print('information according to google search :', url)
        print(samaya)
        print( "current temperature", temp ,unit)
        print(mausam, " :",  weather_state)
        
    
    except:
        print(f'city or location {query} not found') 
    
    
    