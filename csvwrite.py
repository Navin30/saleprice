import csv
def writeReport(result):
    fields = ["productVariantId", 'effort', 'priceType', 'startDate', 'endDate','price']
    filename = "order_export.csv"
    data_file = open(filename, 'a', newline='')
    csv_writer = csv.DictWriter(data_file, fieldnames=fields)
    csv_writer.writeheader()

    for data in result:
        csvObject = {};
        for dataset in data['PriceHistory']:
            csvObject['productVariantId'] = data["productVariantId"]
            csvObject['effort'] = dataset['effort']
            csvObject['priceType'] = dataset['priceType']
            csvObject['startDate'] = dataset['startDate']
            csvObject["endDate"] = dataset['endDate']
            csvObject['price'] = dataset['price']

            csv_writer.writerow(csvObject);

    data_file.close()
    print("end")
