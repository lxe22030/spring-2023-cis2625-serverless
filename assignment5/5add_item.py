import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('Students1')
# add new items to the table using DynamoDB.Table.put_item():
table.put_item(
   Item={
        'SID': '1234',
        'first_name': 'Luke',
        'last_name': 'Engel',
        'age': 20,
        'email': 'lxe22030@ucmo.edu',
    }
)
