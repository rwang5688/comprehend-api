import comprehend_util
import json


def lambda_handler(event, context):
    """Sample pure Lambda function

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
    
    # DEBUG: print event with formattings
    print("event: %s" % json.dumps(event, indent=2))

    message = ''
    if 'queryStringParameters' in event:
        query_string_parameters = event['queryStringParameters']
        print("query_string_parameters: %s" % (query_string_parameters))
    
        if 'message' in query_string_parameters:
            message = query_string_parameters['message']
            print("message: %s" % (message))
    
    # this is for demonstrating Git pull request worklfow
    #print('this is a super superfluous message to demonstrate Git pull request sworkflow')

    # this is just a call for testing a call to comprehend
    #response = comprehend_util.call_detect_sentiment(the_input=query_string_parameters, language_code='en')

    # uncomment the following lines to test against inference endpoint
    endpoint_arn = "arn: arn:aws:comprehend:us-west-2:842610740959:document-classifier-endpoint/suicide-endpoint"
    response = comprehend_util.call_custom_comprehend_model(the_input=query_string_parameters, endpoint_arn=endpoint_arn)

    print("response: %s" % json.dumps(response, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

