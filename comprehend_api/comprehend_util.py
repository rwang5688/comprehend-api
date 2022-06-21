import boto3
import json


def call_custom_comprehend_model(the_input=None,endpoint_arn=None):
    '''call the custom comprehend model that has been previously trained to classify the document according to its medical specialty type.'''
    client = boto3.client('comprehend')

    print("the_input: %s" % (the_input))

    response = {}

    if 'message' in the_input:
        message = the_input['message']
        print ("message: %s" % message)

        response = client.classify_document(
            Text=message,
            EndpointArn=endpoint_arn
            )
    
    return(response)


def call_detect_sentiment(the_input=None,language_code=None):
    '''call the deetect_sentiment API.'''
    client = boto3.client('comprehend')

    print("the_input: %s" % (the_input))

    response = {}

    if 'message' in the_input:
        message = the_input['message']
        print ("message: %s" % message)

        response = client.detect_sentiment(
            Text=message,
            LanguageCode=language_code
            )
    
    return(response)

