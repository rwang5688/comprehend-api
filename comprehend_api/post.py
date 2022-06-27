import boto3
import comprehend_util
import json


def lambda_handler(event, context):
    '''Provide an event that contains the following keys:
      - operation: one of the operations in the operations dict below
      - tableName: required for operations that interact with DynamoDB
      - payload: a parameter to pass to the operation being performed
    '''
    
    # DEBUG: print event with formattings
    print("event: %s" % json.dumps(event, indent=2))
    
    # convert body from JSON object to Python dictionary
    body = json.loads(event['body'])
    print("body: %s" % (body))
    
    operation = body['operation']

    if 'tableName' in body:
        dynamo = boto3.resource('dynamodb').Table(body['tableName'])
    
    # replace 12 placeholder digits with AWS ID
    endpoint_arn = "arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/suicide-endpoint"
    
    operations = {
        'create': lambda x: dynamo.put_item(**x),
        'read': lambda x: dynamo.get_item(**x),
        'update': lambda x: dynamo.update_item(**x),
        'delete': lambda x: dynamo.delete_item(**x),
        'list': lambda x: dynamo.scan(**x),
        'detect': lambda x: comprehend_util.call_custom_comprehend_model(the_input=x, endpoint_arn=endpoint_arn),
        'echo': lambda x: x,
        'ping': lambda x: 'pong'
    }
    
    response = {}

    if operation in operations:
        # operate on payload as Python dictionary
        response = operations[operation](body['payload'])
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
    
    print("response: %s" % json.dumps(response, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

