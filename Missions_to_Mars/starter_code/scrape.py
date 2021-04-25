from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return_data = {}
    driver.close()
    return return_data
    

if __name__ == "__main__":
    print(scrape_info() )