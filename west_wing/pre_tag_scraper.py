from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json


def get_clean_text(page_url):
    req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    page_soup = BeautifulSoup(webpage, "lxml")

    contents = page_soup.find_all("pre")
    clean_text = '\n'.join(BeautifulSoup(contents[0].encode_contents(), "lxml").stripped_strings)

    return clean_text


urls_file = open('page_urls_for_pre_scraper.json')
all_page_urls = json.load(urls_file)
urls_file.close()

for episode_title, url in all_page_urls.items():
    episode_file = open("episodes/{}".format(episode_title), "w")
    episode_file.write(get_clean_text(url))
    episode_file.close()


