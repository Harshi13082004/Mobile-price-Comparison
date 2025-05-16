import pandas as pd

flipkart_df = pd.read_csv("../data/flipkart_mobiles_under_50000.csv")
amazon_df = pd.read_csv("../data/amazon_mobiles_under_50000.csv")

amazon_df.fillna({"Prices": "0", "Desc": "Not Available", "Reviews": "No Reviews"}, inplace=True)
flipkart_df.fillna({"Prices": "0", "Desc": "Not Available", "Reviews": "No Reviews"}, inplace=True)

amazon_df.dropna(subset=["Product_Name"], inplace=True)
flipkart_df.dropna(subset=["Product_Name"], inplace=True)

amazon_df.rename(columns={"Product_Name": "Name", "Prices": "Price", "Desc": "Description", "Reviews": "Rating"}, inplace=True)
flipkart_df.rename(columns={"Product_Name": "Name", "Prices": "Price", "Desc": "Description", "Reviews": "Rating"}, inplace=True)

def clean_price(price):
    if isinstance(price, str):
        price = price.replace("₹", "").replace(",", "").strip()
        return int(price) if price.isdigit() else 0
    return 0

amazon_df["Price"] = amazon_df["Price"].apply(clean_price)
flipkart_df["Price"] = flipkart_df["Price"].apply(clean_price)

amazon_df["Source"] = "Amazon"
flipkart_df["Source"] = "Flipkart"

merged_df = pd.concat([amazon_df, flipkart_df], ignore_index=True)
merged_df.to_csv("../data/merged_mobiles_data.csv", index=False)
print("Merged dataset saved.")
