import json 


def do_something(dictionary: dict) -> dict:
    """ echos post body """
    return dictionary 


def lambda_handler(event, context):
    try:
        print('Event: {}'.format(event))
        print("Log stream name:", context.log_stream_name)
        print("Log group name:", context.log_group_name)
        print("Request ID:", context.aws_request_id)
        print("Mem. limits(MB):", context.memory_limit_in_mb)
    except Exception as e:  
        raise Exception('Error occurred during execution')  # notify aws of failure
    
    # catch preflight response. Messy, but don't know how to fix... using httpstatus?
    try:
        body = event['body'] 
    except Exception as e: 
        return {
            'statusCode': 204,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            }
        } 
    
    response_body = do_something(json.loads(body))
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': response_body
    }