from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:11013", auth=("neo4j", "Manoharan786"))

def add_friend(tx, name, friend_name):
    tx.run("MERGE (a:Person {name: $name}) "
           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)

def print_friends(tx, name):
    print("DATA\n\n")

    for record in tx.run("MATCH (o:Order)-[rel:CONTAINS]->(p:Product) RETURN p, rel, o"):
        
        print("<",record[0]["productName"],"---",record[1]["quantityOrdered"],"---",record[2]["orderId"],">\n")
        # print(record,"\n")
    print("GRAPH\n\n")
    obj=(tx.run("MATCH (o:Order)-[rel:CONTAINS]->(p:Product) RETURN p, rel, o")).graph()
    nodes=obj.nodes
    relationships=obj.relationships
    for node in nodes:
            print(node)
    print("\n\n")
    for relationship in relationships:
            print(relationship)





def load_csv(tx):
    
    for record in tx.run("LOAD CSV WITH HEADERS FROM 'file:///order-details.csv' AS row WITH toInteger(row.productID) AS productId, toInteger(row.orderID) AS orderId, toInteger(row.quantity) AS quantityOrdered MATCH (pr:Product {productId: productId}) MATCH (or:Order {orderId: orderId}) MERGE (or)-[rell:CONTAINS {quantityOrdered: quantityOrdered}]->(pr) RETURN (rell)"):
        print(type(record))
        print(record.keys())
        print(record,"\n")
                
def load_csv_one(tx):
    for record in tx.run("LOAD CSV FROM 'file:///products.csv' AS row WITH toInteger(row[0]) AS productId, row[1] AS productName, toFloat(row[2]) AS unitCost RETURN productId, productName, unitCost LIMIT 3"):
        print(type(record))
        print(record.data()) 
        # print(record,"\n")   

def load_csv_two(tx):
    for record in tx.run("LOAD CSV FROM 'file:///products.csv' AS row WITH toInteger(row[0]) AS productId, row[1] AS productName, toFloat(row[2]) AS unitCost MERGE (p:Product {productId: productId}) SET p.productName = productName, p.unitCost = unitCost RETURN p"):
        print(type(record))
        print(record.data())
        # print(record,"\n")

    print("\n\n")
    print("")

    for record in tx.run("LOAD CSV WITH HEADERS FROM 'file:///orders.csv' AS row WITH toInteger(row.orderID) AS orderId, datetime(replace(row.orderDate,' ','T')) AS orderDate, row.shipCountry AS country MERGE (o:Order {orderId: orderId}) SET o.orderDateTime = orderDate, o.shipCountry = country RETURN o"):
        print(type(record))
        print(record.data())
        # print(record,"\n")
    
    print("\n\n")

    for record in tx.run("LOAD CSV WITH HEADERS FROM 'file:///order-details.csv' AS row WITH toInteger(row.productID) AS productId, toInteger(row.orderID) AS orderId, toInteger(row.quantity) AS quantityOrdered MATCH (p:Product {productId: productId}) MATCH (o:Order {orderId: orderId}) MERGE (o)-[rel:CONTAINS {quantityOrdered: quantityOrdered}]->(p) RETURN rel"):
        print(type(record))
        print(record.data())
        # print(record,"\n")

with driver.session() as session:
    session.write_transaction(add_friend, "Arthur", "Guinevere")
    session.write_transaction(add_friend, "Arthur", "Lancelot")
    session.write_transaction(add_friend, "Arthur", "Merlin")
    print("PRODUCT \n")
    session.read_transaction(load_csv)
#     print("\n\n")
#     print("ORDER \n")
#     session.read_transaction(load_csv_two)
#     print("\n\n")
#     print("MATCH\n\n")
#     session.read_transaction(print_friends, "Arthur")

