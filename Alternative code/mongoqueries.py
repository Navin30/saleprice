from datetime import datetime, timezone
import csv
import numpy
import pandas as pd
from pymongo import MongoClient
from Handler import writeReport
# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient(
    'mongodb+srv://domainApiUser:4ulTPq9q2t8IZt5p@dev01-eddiebauer-com-x6i4a.mongodb.net/admin?authSource=admin&replicaSet=dev01-eddiebauer-com-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')
result = client['atomic_pim']['pricesforskus'].aggregate([
    {
        '$match': {
            '$and': [
                {
                    'createdAt': {
                        '$gte': datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
                    }
                }
            ]
        }
    }, {
        '$project': {
            '_id': 0,
            'productVariantId': 1,
            'PriceHistory': {
                '$filter': {
                    'input': '$PriceHistory',
                    'as': 'priceType',
                    'cond': {
                        '$and': [
                            {
                                '$in': [
                                    '$$priceType.effort', [
                                        '792', '892', '692'
                                    ]
                                ]
                            }, {
                                '$gte': [
                                    '$$priceType.startDate', datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
                                ]
                            }, {
                                '$lte': [
                                    '$$priceType.endDate', datetime(2021, 1, 30, 0, 0, 0, tzinfo=timezone.utc)
                                ]
                            }
                        ]
                    }
                }
            }
        }
    }, {
        '$project': {
            'productVariantId': 1,
            'PriceHistory.effort': 2,
            'PriceHistory.price': 3,
            'PriceHistory.priceType': 4,
            'PriceHistory.startDate': 5,
            'PriceHistory.endDate': 6
        }
    }
])
writeReport(result)
