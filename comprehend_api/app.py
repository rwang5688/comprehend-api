import json


def lambda_handler(event, context):
    """Lambda handler for Comprehend API call

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # DEBUG: print event as received
    print("event: %s" % (event))
    
    # convert body value to Python dictionary
    body = json.loads(event['body'])
    print("body: %s" % (body))

    # perform the equivalent of Postman Echo
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": body
        }),
    }
