from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return_data = {}

    #URL 1
    #Run driver to scrape NASA URL content   
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    driver.get(url)
    html = driver.page_source
    soup = bs(html, 'html.parser')

    #Assign the text to variables that you can reference later.
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    

    #URL 2
    #Run driver to scrape Featured JPL Image URL content   
    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    driver.get(jpl_url)

    #Narrow down using div class_='header'
    html = driver.page_source
    soup = bs(html, 'html.parser')
    image_url = soup.find('div', class_= 'header')
    #break to image src
    image_url=soup.find('img', class_='headerimage fade-in')['src'] 

    #create  final jpg URL
    base_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    featured_image_url = base_url + image_url


    #URL 3
    #connect to space facts website
    space_facts = 'https://space-facts.com/mars/'
    driver.get(space_facts)

    #Get body of table using <tbody> tag
    html = driver.page_source
    soup = bs(html, 'html.parser')
    table = soup.find('tbody')
    #use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    tables = pd.read_html(space_facts)
    #grab first part of table (first set; indices 0-8)
    mars_facts_df = tables[0]
    #reset column headers
    mars_facts_df.columns = ["Facts", "Mars"] 
    #Use Pandas to convert the data to a HTML table string.
    html_table = mars_facts_df.to_html(classes=['table', 'table-bordered'])
    html_table = html_table.replace('\n', '')


    #URL 4 
    #connect to mars hemispheres website
    mars_hems = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    base_url = 'https://astrogeology.usgs.gov'
    driver.get(mars_hems)
    #Get body of table using div class_='item'
    html = driver.page_source
    soup = bs(html, 'html.parser')
    hem = soup.find_all('div', class_ = 'item')
    #test first a tag with href 
    hem[0].find('div',class_='description').find('a')['href']
    hemisphere_image_dict = []
    #loop through to grab each image froom description --> a --> href
    for h in hem:
        #get href from main page
        hemisphere_link = h.find('div',class_='description').find('a')['href']
        #create URL to high res image
        url = base_url+hemisphere_link
        #webdriver to secondary page
        driver.get(url)
        html = driver.page_source
        soup = bs(html, 'html.parser')
        #get URL for imade
        high_res = soup.find('a', text = 'Sample')['href']
        #get image title
        high_res_title = h.find('h3').text
        #create dict
        hemisphere_image_dict.append({"title" : high_res_title, "img_url" : high_res})


    return_data = {"title": news_title, 
                    "paragraph": news_p, 
                    "featured_image": featured_image_url, 
                    "html_table": html_table, 
                    "hemisphere_images": hemisphere_image_dict }

    driver.close()
    return return_data

if __name__ == "__main__":
    print(scrape_info() )