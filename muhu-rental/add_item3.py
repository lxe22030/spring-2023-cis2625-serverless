import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('PropertyBasic')
# add new items to the table using DynamoDB.Table.put_item():
table.put_item(
   Item={
       'pid': '4',
        'street_address': '1000 College St.',
        'city': 'Warrensburg',
        'state': 'MO',
        'zip': '64093',
        'year_built': '1990',
        'type': 'house',
        'size': '1000 sqft',
        'bedrooms': '1',
        'bathrooms': '1',
        
    }
)