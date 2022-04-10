# using httprequest from source:
# https://github.com/alfonsof/aws-python-examples/blob/master/awslambdahttprequest/lambda_function.py


import json

def lambda_handler(event, context):
    
    if 'queryStringParameters' in event:
        body = {'first_name': event['queryStringParameters']['first_name'], 
                'last name': event['queryStringParameters']['last_name']}
    else:
        body = {}
        
    return {
        'statusCode': 200,
        'body': json.dumps(body),
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }
    