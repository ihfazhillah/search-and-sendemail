"""olx simple scraper"""
import requests
from bs4 import BeautifulSoup


def scrape(query):
    """To scrape method"""
    query_fix = '-'.join(query.split(' '))
    url = f"https://www.olx.co.id/properti/q-{query_fix}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
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
