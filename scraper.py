import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        hn.append({'title': title,
                   'link': href})
        points = votes[index].getText()
        print(points)
    return hn


create_custom_hn(links, votes)
