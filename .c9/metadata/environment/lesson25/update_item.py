{"filter":false,"title":"update_item.py","tooltip":"/lesson25/update_item.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"17c05854cee1204d5cf597bce26d37e66e13e7c3","mime":"text/x-script.python","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["import boto3","# Get the service resource.","dydb = boto3.resource('dynamodb')","# Instantiate a table resource object","table = dydb.Table('users')","# update attributes of the item in the table using DynamoDB.Table.update_item()","table.update_item(","    Key={","        'username': 'janedoe',","        'last_name': 'Doe'","    },","    UpdateExpression='SET age = :val1',","    ExpressionAttributeValues={","        ':val1': 27","    }",")",""],"id":1}]]},"timestamp":1681400566997}