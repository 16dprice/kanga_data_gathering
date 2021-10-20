from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json


def get_pages(page_url, urls_to_dump):
    req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    page_soup = BeautifulSoup(webpage, "lxml")
    content = page_soup.find_all("a", {"class": "topictitle"})

    for el in content:
        el_contents = el.encode_contents()
        if el_contents != b"Read Updates: 'Tis The Season 2021 Editing Challenge":
            urls_to_dump[el_contents.decode("utf-8")] = "https://transcripts.foreverdreaming.org{}".format(el['href'][1:])


urls = [
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=25",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=50",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=75",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=100",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=125",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=150",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=175",
    "https://transcripts.foreverdreaming.org/viewforum.php?f=177&start=200"
]

urls_to_dump = {}

for url in urls:
    get_pages(url, urls_to_dump)

print(json.dumps(urls_to_dump, indent=4))

