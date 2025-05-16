# 📱 Mobile Price Comparison - Amazon vs Flipkart

A data science project comparing mobile phone listings (under ₹50,000) across Amazon and Flipkart using Python for scraping, Pandas for processing, and Neo4j for graph-based storage and queries.

## 📌 Features

- Web scraping using BeautifulSoup
- Data cleaning and preprocessing
- Merging datasets from multiple sources
- Graph database schema and queries using Neo4j

## 📁 Project Structure

```
data/       -> Raw and processed CSV files  
notebooks/  -> Python scripts for scraping and processing  
neo4j/      -> Code and Cypher queries for Neo4j graph database  
screenshots/
```

## 🚀 How to Run

1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run scripts in the following order:
   - `scrape_flipkart.py`
   - `scrape_amazon.py`
   - `process_data.py`
   - `neo4j_upload.py`
4. Start Neo4j and open `localhost:7474` to query data.

## 🧠 Insights

- Price variation found between platforms
- Brand popularity trends
- Many new models had no reviews


