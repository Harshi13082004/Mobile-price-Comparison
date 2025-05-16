# Neo4j Queries

### 1. View all stored mobile phones
```cypher
MATCH (m:Mobile) RETURN m LIMIT 10;
```

### 2. View all brands
```cypher
MATCH (b:Brand) RETURN b;
```

### 3. Relationships between Mobile, Brand, Platform
```cypher
MATCH (m:Mobile)-[:BRAND_OF]->(b:Brand), (m)-[:LISTED_ON]->(p:Platform)
RETURN m.name, b.name, p.name;
```

### 4. Find all mobiles listed on Amazon
```cypher
MATCH (m:Mobile)-[:LISTED_ON]->(p:Platform {name: "Amazon"}) RETURN m;
```

### 5. Find mobiles from OnePlus
```cypher
MATCH (m:Mobile)-[:BRAND_OF]->(b:Brand {name: "OnePlus"}) RETURN m;
```
