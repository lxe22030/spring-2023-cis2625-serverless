{"filter":false,"title":"delete_item.py","tooltip":"/lesson25/delete_item.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["import boto3","# Get the service resource.","dydb = boto3.resource('dynamodb')","# Instantiate a table resource object","table = dydb.Table('users')","# delete the item using DynamoDB.Table.delete_item()","table.delete_item(","    Key={","        'username': 'janedoe',","        'last_name': 'Doe'","    }",")","","# Print out items in the table.","print(table.item_count)",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1681400565185,"hash":"187cf8407e8493f972c2a08a385144fe9cbc60c5"}