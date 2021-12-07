import csv
def writeReport(result):

    list1=[]

    for data in result:
        datas = {}
        for dataset in data['PriceHistory']:
            datas['product'] = data["productVariantId"]
            datas['effort'] = dataset['effort']
            datas['type'] = dataset['priceType']
            datas['startdate'] = dataset['startDate']
            datas['enddate'] = dataset['endDate']
            datas['price'] = dataset['price']
            name=[datas['product'],datas['effort'],datas['type'],datas['startdate'],datas['enddate'],datas['price']]
            list1.append(name)
    fields = ["product", 'effort', 'priceType', 'startdate','enddate', 'price']
    filename = "order_export.csv"
    data_file = open(filename, 'a', newline='')
    csv_writer = csv.writer(data_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(list1)
    data_file.close()
    print("end")
