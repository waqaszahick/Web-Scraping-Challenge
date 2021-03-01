from bs4 import BeautifulSoup
from splinter import Browser
import requests
from IPython.display import display
import pandas as pd
import os
def scrape_info():
    url_1 = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    page = requests.get(url_1)
    soup = BeautifulSoup(page.text, 'html.parser')
    news_title = soup.findAll('div',attrs={'class':'content_title'})[0].text[2:-2]
    news_p = soup.findAll('div',attrs={'class':'rollover_description_inner'})[0].text[1:-1]    
    url_2 = 'https://space-facts.com/mars/'
    dfs = pd.read_html(url_2)
    dfs[0].columns = ['Description', 'Mars']
    html_tab = dfs[0].to_html(index = False)

    text_file = open("table.html", "w")
    text_file.write(html_tab)
    text_file.close()

    url_s = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    index = 'index.html'
    url = url_s+index
    exe = 'chromedriver.exe'
    ch_dr = os.path.abspath(exe)
    print(ch_dr)    
    browser = Browser('chrome', exe, headless=False)
    browser.visit(url)
    html_s = browser.html
    soup_s = BeautifulSoup(html_s,'html.parser')
    browser.quit()
    header = soup_s.find('img',class_='headerimage')
    f_img = header['src']
    featured_image_url = url_s+f_img
    home_page = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    site = 'https://astrogeology.usgs.gov'
    page = requests.get(home_page)
    soup = BeautifulSoup(page.text, 'html.parser')
    hemisphere_image_urls = []
    for item in soup.findAll('div',attrs={'class':'item'}):
        hm_dict = {}
        hm_dict['title'] = str(item.find_all('div',attrs={'class':'description'})[0].text)        
        hm_url = site+str(item.find_all('a',href=True)[0]['href'])
        hm_page = requests.get(hm_url)
        hm_soup = BeautifulSoup(hm_page.text, 'html.parser')
        for items in hm_soup.findAll('div',attrs={'class':'wide-image-wrapper'}):            
            hm_dict['img_url'] = str(items.ul.li.find_all('a', href=True)[0]['href'])            
        hemisphere_image_urls.append(hm_dict)

    print('\n',hemisphere_image_urls)
    data = {'news_title':news_title, 'news_p':news_p , 'table':html_tab, 'featured_img':featured_image_url, 'hemispheres':hemisphere_image_urls}
    return data