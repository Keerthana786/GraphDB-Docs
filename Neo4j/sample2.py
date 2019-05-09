import csv
product=[]
order=[]
relationship=[]
with open("products.csv") as pr_csv:
    pr_reader=csv.reader(pr_csv,delimiter=',')
    for row in pr_reader:
        product.append(row)
pr_csv.close()
with open("orders.csv") as or_csv:
    or_reader=csv.reader(or_csv,delimiter=',')
    next(or_reader)
    for row in or_reader:
        order.append(row)
or_csv.close()
with open("order-details.csv") as rr_csv:
    rr_reader=csv.reader(rr_csv,delimiter=',')
    next(rr_reader)
    for row in rr_reader:
        relationship.append(row)
rr_csv.close()


for row in relationship:
    print("relation : ",row,"\n")
    for row_p in product:
        for row_o in order:
            if row[0]==row_o[0] and row[1]==row_p[0]:
                print(row_p,"---------------",row_o,"\n")
