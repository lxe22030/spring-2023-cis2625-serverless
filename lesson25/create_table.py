import boto3

# Get the service resource.
dydb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dydb.create_table(
    TableName='users',
    KeySchema= [   {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
}  ],
    AttributeDefinitions = [  {
'AttributeName': 'username',
   'AttributeType': 'S'
        },
        {
  'AttributeName': 'last_name',
   'AttributeType': 'S'
        },
    ],
     ProvisionedThroughput = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
                                             }
      )

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)
