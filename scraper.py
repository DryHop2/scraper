import requests
from bs4 import BeautifulSoup
import pprint
from time import sleep


res = requests.get(f'https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlsit):
    return sorted(hnlsit, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title,
                           'link': href,
                           'votes': points})

    return sort_stories_by_votes(hn)


def scrape_pages(links, subtext, num=1):
    if num > 1:
        for i in range(2, num + 1):
            sleep(0.1)
            res = requests.get(f'https://news.ycombinator.com/news?p={i}')
            soup = BeautifulSoup(res.text, 'html.parser')
            links += soup.select('.titleline > a')
            subtext += soup.select('.subtext')
            return (create_custom_hn(links, subtext))
    else:
        return create_custom_hn(links, subtext)


pprint.pprint(scrape_pages(links, subtext))
