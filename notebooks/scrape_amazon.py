import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 24):
    url = f"https://www.amazon.in/s?k=mobiles+under+50000&page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_="s-main-slot s-result-list s-search-results sg-row")
    if not box:
        continue

    names = box.find_all("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
    prices = box.find_all("span", class_="a-price-whole")
    desc = box.find_all("span", class_="a-color-base")
    reviews = box.find_all("i", class_="-icon a-icon-star-small a-star-small-4-5")

    max_len = max(len(names), len(prices), len(desc), len(reviews))
    for i in range(max_len):
        Product_name.append(names[i].text if i < len(names) else "N/A")
        Prices.append(prices[i].text if i < len(prices) else "N/A")
        Description.append(desc[i].text if i < len(desc) else "N/A")
        Reviews.append(reviews[i].text if i < len(reviews) else "N/A")

df = pd.DataFrame({
    "Product_Name": Product_name,
    "Prices": Prices,
    "Desc": Description,
    "Reviews": Reviews
})
df.to_csv("../data/amazon_mobiles_under_50000.csv", index=False)
