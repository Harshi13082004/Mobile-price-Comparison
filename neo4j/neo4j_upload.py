from py2neo import Graph, Node, Relationship
import pandas as pd

graph = Graph("bolt://localhost:7687", auth=("neo4j", "your_password_here"))

df = pd.read_csv("../data/merged_mobiles_data.csv")

for _, row in df.iterrows():
    mobile = Node("Mobile", name=row["Name"], price=row["Price"], rating=row["Rating"], description=row["Description"])
    brand_name = row["Name"].split()[0]
    brand = Node("Brand", name=brand_name)
    platform = Node("Platform", name=row["Source"])

    graph.merge(mobile, "Mobile", "name")
    graph.merge(brand, "Brand", "name")
    graph.merge(platform, "Platform", "name")
    graph.merge(Relationship(mobile, "BRAND_OF", brand))
    graph.merge(Relationship(mobile, "LISTED_ON", platform))

print("Data successfully stored in Neo4j!")
