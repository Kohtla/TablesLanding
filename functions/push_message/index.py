import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('MainTable')

    id = event.id
    time = event.time
    place = event.place

    '''table.put_item(
        Item={
            'ID': 1,
            'time': 'puss',
            'place': 'gtm'
        }
    )'''

    return str(id) +"-"+str(time)+"-"+str(place)
