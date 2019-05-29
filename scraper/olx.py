"""olx simple scraper"""
import requests
from bs4 import BeautifulSoup


def scrape(query):
    """To scrape method"""
    query_fix = '-'.join(query.split(' '))
    url = f"https://www.olx.co.id/properti/q-{query_fix}/"
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16'}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, features='html.parser')
    listings = soup.select('tr.cursor.adListingType')
    result = []
    for listing in listings:
        data = {}
        data['link'] = listing.select('.link.detailsLink')[0]['href']
        data['title'] = listing.select('.link.detailsLink')[0].get_text().strip()
        data['image'] = listing.select('.thumb > img')[0]['src']
        data['price'] = listing.select('.price.large')[0].get_text().strip()
        result.append(data)

    return result
