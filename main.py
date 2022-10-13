import csv

with open('sales.csv', 'r') as file:
    business = csv.reader(file)
    sales = []
    for row in business:
        sale = (row[2])
        if(sale.isdigit()):
            sales.append(int(sale))
    total_sales = sum(sales)
    print("Total sales is £", total_sales)
    average_sales = sum(sales)/len(sales)
    print("The averages sales is £", average_sales)
    min_sales = min(sales)
    max_sales = max(sales)
    print("The smallest sale within the year was = £", min_sales)
    print("The largest sale of the year was £", max_sales)