import time
import threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Function to get article links related to a query from Financial Times
def get_article_links(query):
    # Initialize headless Chrome driver with specific user-agent
    op = webdriver.ChromeOptions()
    op.add_argument('no-sandbox')
    op.add_argument('window-size=1920,1080')
    op.add_argument('disable-gpu')
    op.add_argument("headless")
    op.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    )
    driver = webdriver.Chrome(options=op)
    links = []
    try:
        # Navigate to Financial Times search page with the query
        driver.get(f"https://www.ft.com/search?q={query}")
        # Find elements containing article links
        link_data = driver.find_elements(By.CSS_SELECTOR, 'a[data-trackable="heading-link"]')
        # Fetch the href of the first three links
        for link in link_data[:3]:
            links.append(link.get_attribute("href"))
        print("links:", links)
    except Exception as e:
        print(f"Unable to extract the links: {e}")
    finally:
        #driver.close()
        return links

# Function to get article data from a given URL
def get_article_data(href, article_list):
    # Initialize headless Chrome driver with specific user-agent
    op = webdriver.ChromeOptions()
    op.add_argument('no-sandbox')
    op.add_argument('window-size=1920,1080')
    op.add_argument('disable-gpu')
    op.add_argument("headless")
    op.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    )
    driver = webdriver.Chrome(options=op)
    data = ""
    try:
        # Navigate to archive.is
        driver.get("https://archive.is/")
        # Find search box and submit the URL
        search_box = driver.find_element(By.ID, "q")
        search_box.send_keys(href)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        # Click the first link in the search results
        driver.find_element(By.ID, "row0").find_elements(By.TAG_NAME, "a")[0].click()
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # Find article body and extract text
        article_body = soup.find(id="article-body")
        if article_body is not None:
            for div in article_body.find_all("div"):
                if div.text.strip():
                    data += str(div.text)
        print("Article:", data)
        article_list.append(data)
    except Exception as e:
        print(f"Unable to extract the article text: {e}")
    finally:
        #driver.close()
        return article_list
