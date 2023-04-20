import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('Students1')
# update attributes of the item in the table using DynamoDB.Table.update_item()
table.update_item(
    Key={
        'SID': '1234',
        'email': 'lxe22030@ucmo.edu'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 27
    }
)
