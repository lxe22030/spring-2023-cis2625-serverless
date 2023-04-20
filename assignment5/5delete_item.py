import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('Students1')
# delete the item using DynamoDB.Table.delete_item()
table.delete_item(
    Key={
        'SID': '1234',
        'email': 'lxe22030@ucmo.edu'
    }
)

# Print out items in the table.
print(table.item_count)
