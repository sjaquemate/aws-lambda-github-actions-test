[ERROR] Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'aws_lambda_decorators'
from aws_lambda_decorators import cors 


@cors(allow_origin='*', allow_methods='POST', allow_headers='Content-Type', max_age=86400)
def lambda_handler(event, context):
    return {'statusCode': 200, 'body': 'returns something here'}