import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 24):
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_="DOjaWF gdgoEp")
    if not box:
        continue

    names = box.find_all("div", class_="KzDlHZ")
    prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    desc = box.find_all("ul", class_="G4BRas")
    reviews = box.find_all("div", class_="XQDdHH")

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
df.to_csv("../data/flipkart_mobiles_under_50000.csv", index=False)
