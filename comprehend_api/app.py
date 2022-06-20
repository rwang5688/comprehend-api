from __future__ import print_function

import boto3
import comprehend_util
import json

print('Loading function')


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

    operations = {
        'create': lambda x: dynamo.put_item(**x),
        'read': lambda x: dynamo.get_item(**x),
        'update': lambda x: dynamo.update_item(**x),
        'delete': lambda x: dynamo.delete_item(**x),
        'list': lambda x: dynamo.scan(**x),
        'detect': lambda x: comprehend_util.call_detect_sentiment(the_input=x, language_code='en'),
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

    return response

    # below is what we used to return
    return {
        "statusCode": 200,
        "body": json.dumps({
            "response": response
        }),
    }

