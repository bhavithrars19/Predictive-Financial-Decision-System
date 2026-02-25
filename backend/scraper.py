import requests
from bs4 import BeautifulSoup


def get_affordable_alternatives(product_name, max_results=5):
    """
    Academic-level stable scraping using books.toscrape.com
    Returns:
    [
        {"title": ..., "price": ..., "link": ...}
    ]
    """

    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.select("article.product_pod")

        recommendations = []

        for product in products[:max_results]:
            title = product.h3.a["title"]
            price = product.select_one(".price_color").text
            link = product.h3.a["href"]

            full_link = f"https://books.toscrape.com/catalogue/{link}"

            recommendations.append({
                "title": title,
                "price": price,
                "link": full_link
            })

        return recommendations

    except Exception:
        return []
