import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from readability import Document
from urllib.parse import urljoin
from langdetect import detect

def contentfinder(url, driver):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        if "javascript" in soup.find("html").get("class", []):
            driver.get(url)
            html = driver.page_source
        else:
            html = requests.get(url).text
    except Exception:
        pass

    article = None
    t = soup.find('title')
    title = t.string if t is not None else None
    lang = detect(soup.body.get_text())

    # Look for the <article>, <div>, or <section> tags that contain the main article content
    article = soup.find("article") or soup.find("div", class_="article") or soup.find("section", class_="article")

    # If the <article>, <div>, or <section> tags are not found, look for elements with specific CSS classes
    if not article:
        article = soup.find("div", class_="entry-content") or soup.find("div", class_="main-content")

    # If the <article>, <div>, or <section> tags are not found, look for the <main> tag
    if not article:
        article = soup.find("main")

    # If the <article>, <div>, <section>, or <main> tags are not found, use a content extraction library
    # if not article:
    #     doc = Document(response.text)
    #     article = BeautifulSoup(doc.summary(html_partial=True), "html.parser")

    return article, title, lang

# prints the article content, given that the article content is not None
def printarticle(article):

    # Define a list of valid tag names
    valid_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li']

    # Loop over all elements in the article content
    for element in article.find_all():
        # Check if the element is part of the readable article content and has a valid tag name
        if element.name in valid_tags:
            # Print the name of the element and its text content
            print(element.name, ":", element.get_text(strip=True))

def breakarticleintocomponents(article):

    components = []

    # Define a list of valid tag names
    valid_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li']

    # Loop over all elements in the article content
    for element in article.find_all():
        # Check if the element is part of the readable article content and has a valid tag name
        if element.name in valid_tags:
            # Print the name of the element and its text content
            components.append((element.name, element.get_text(strip=True)))

    return components

class ContentFinder:
    def __init__(self, url):
        self.options = Options()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.content = {}

    def __del__(self):
        self.driver.quit()

    def __str__(self):
        return f"ContentFinder(url={self.url})"
    
    def __repr__(self):
        return f"ContentFinder(url={self.url})"
    
    def __getitem__(self, url):
        return self.content[url]
    
    def __setitem__(self, url, value):
        self.content[url] = value

    def __delitem__(self, url):
        del self.content[url]

    def __iter__(self):
        return iter(self.content)
    
    def __len__(self):
        return len(self.content)
    
    def __dict__(self):
        return self.content

    def scrape_url(self, url):
        self.content[url] = {}
        self.article, self.title, self.lang = contentfinder(self.url, self.driver)
        self.content[url]["article"] = self.article
        self.content[url]["title"] = self.title
        self.content[url]["lang"] = self.lang

    def article_meta(self, url):
        if url not in self.content:
            self.scrape_url(url)
        return self.content[url]["article"], self.content[url]["title"], self.content[url]["lang"]

    def get_article(self, url):
        if url not in self.content:
            self.scrape_url(url)
        return self.content[url]["article"]

    def get_title(self, url):
        if url not in self.content:
            self.scrape_url(url)
        return self.content[url]["title"]

    def get_lang(self, url):
        if url not in self.content:
            self.scrape_url(url)
        return self.content[url]["lang"]

    def print_article(self, url):
        if url not in self.content:
            self.scrape_url(url)
        printarticle(self.content[url]["article"])

    def get_components(self, url):
        if url not in self.content:
            self.scrape_url(url)
        return breakarticleintocomponents(self.content[url]["article"])
    
    def flush_data(self):
        self.content = {}

# if __name__ == "__main__":
#     options = Options()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)
#     url = "https://en.wikipedia.org/wiki/Attalus_I"
#     article, title, lang = contentfinder(url, driver)
#     print(article.text)