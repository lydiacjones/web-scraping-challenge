from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Visit visitcostarica.herokuapp.com
    url = "https://visitcostarica.herokuapp.com/"
    driver.get(url)

    html= driver.page_source
    soup = bs(html)

    wdiv = soup.find('div', id="weather")

    # import ipdb; ipdb.set_trace()
    min_temp = wdiv.find_all('strong')[0].text

    max_temp = wdiv.find_all('strong')[1].text

    if max_temp[-1] != "F":
        max_temp = max_temp + "F"
    
    sloth_url = url+soup.find_all('img')[2]["src"]
    driver.close()


    return {"max_temp":max_temp,"min_temp":min_temp,"sloth_url": sloth_url}





if __name__ == "__main__":
    print(scrape_info() )