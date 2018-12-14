from bs4 import BeautifulSoup
from Models.Receipt import Receipt
import urllib.request as request


def get_receipt(url):
    with request.urlopen(url) as resp:
        parser = BeautifulSoup(resp.read())
        table = parser.find("table", {"id": "from"})
        if not table:
            return None
        products = []
        for row in table.findAll("tr")[2:]:
            span = row.find("span")
            if not span:
                return None
            text = span.text
            products.append(text)
        guide_lines = [x.text for x in parser.find("div", {"id": "how"}).findAll("p")]
        title = parser.find("h1", {"class": "title"}).text
        return Receipt(products, guide_lines, title)

if __name__ == '__main__':
    with open("file.html", "r") as f:
        get_receipt(f.read())