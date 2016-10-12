import urllib2
from bs4 import BeautifulSoup
import re
import json
def get_news_json():
    #get html
    response = urllib2.urlopen('http://www.nitsri.net/indexo.htm')
    html = response.read()
    #parse html
    soup = BeautifulSoup(html)
    lies = soup.find_all(class_=re.compile("_news"))
    count=0
    news_container= []
    root_link="www.nitsri.net/"
    
    for li in lies:
        
        news_container.append({'type':str(li.a.get('href').split('.')[-1]),'headline':str((li.find(class_="news_headline").text).encode('ascii','ignore').decode('ascii')),'text':str((li.find(class_="news_text").text).encode('ascii','ignore').decode('ascii')),'link':root_link+str((li.a.get('href').encode('ascii','ignore').decode('ascii'))),'age':str(li.get('class')[0].split('_')[0])})
        #print("headline %d: "%count +(li.find(class_="news_headline").text))
        #print("text: "+(li.find(class_="news_text").text))
        count+=1
        
        
    
    #Encode to json
    j_obj = json.dumps(news_container)
    
    
    return j_obj

    
        
