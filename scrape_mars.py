import os
import time
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bsoup

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# Scrape Recent NASA Mars News
def scrape():
    browser = init_browser
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)
    time.sleep(2)
    html = browser.html
    soup = bsoup(html, "lxml")
    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    mars_news['news_title'] = news_title
    mars_news['news_paragraph'] = news_p

# JPL Mars Space Images - Featured Image
# image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# browser.visit(image_url)
# html = browser.html
# browser.click_link_by_partial_text("FULL IMAGE")
# browser.is_element_present_by_text("more info", wait_time=5)
# browser.click_link_by_partial_text("more info")
# soup = bsoup(html, "lxml")
# image_results = soup.find('div', class_='download_tiff')
# featured_image_url = image_results.a['href']
# featured_image_url

# Mars Weather
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(2)
    weather_html = browser.html
    soup = bsoup(weather_html, "lxml")
    mars_weather = soup.find("div", class_="js-tweet-text-container").text

# Mars Facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    time.sleep(2)
    tables = pd.read_html(facts_url)
    mars_df = tables[0]
    mars_df.columns = ['Observation', 'Measurement']
    mars_facts = mars_df.set_index('Observation', inplace=True)

    mars_data = {
    "mars_news": mars_news,
    "mars_weather": mars_weather,
    "mars_facts": mars_facts
    }
    browser.quit()

    return mars_data


# Mars Hemispheres
#hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
#browser.visit(hemi_url)
#html = browser.html
#soup = bsoup(html, "lxml")

