from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import json


def get_pages(page_url, urls_to_dump):
    req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    page_soup = BeautifulSoup(webpage, "lxml")
    content = page_soup.find_all("div", {"class": "entry clr"})

    children = content[0].findChildren("a", recursive=True)

    for child in children:
        regex = "^Season "
        try:
            title = child["title"]

            match = re.match(regex, title)
            if match:
                # print(child["href"])
                # urls_to_dump[child[""]]
                episode_title = child.encode_contents().decode("utf-8")
                episode_title = episode_title.replace("\u2013", "-")
                episode_title = episode_title.replace("\u201c", "")
                episode_title = episode_title.replace("\u201d", "")
                episode_title = episode_title.replace("\u2018", "")
                episode_title = episode_title.replace("\u2019", "")
                episode_title = episode_title.replace("\u2033", "")

                urls_to_dump[episode_title] = child["href"]
        except:
            pass


urls_to_dump = {}

for season in range(1, 8):
    get_pages("https://westwingwiki.com/the-wiki/scripts/season-{}/".format(season), urls_to_dump)

print(json.dumps(urls_to_dump, indent=4))