import json
import datetime
import time
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.Session(
    region_name="us-east-1"
)
sns_client = session.client('sns')

number = '16308021235'

def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response

def build_response_message(message_content):
    return {'contentType': 'PlainText', 'content': message_content}

def lambda_handler(event, context):
    intent_name = event['currentIntent']['name']
    session_attributes = event['sessionAttributes']
    print(intent_name)
    if intent_name == 'ScheduleCall':
        print(intent_name)
        sns = boto3.client('sns')
        responsesns = sns.publish(
            PhoneNumber = number,
            Message = 'Hello, {} from {} wants to chat with the FF team about {} on {} at {}. Their email is {}'.format(event['currentIntent']['slots']['Name'],
                  event['currentIntent']['slots']['Organization'],
                  event['currentIntent']['slots']['ServiceTopics'],
                  event['currentIntent']['slots']['Date'],
                  event['currentIntent']['slots']['Time'],
                  event['currentIntent']['slots']['Email']),

            MessageAttributes={
                'AWS.SNS.SMS.SMSType': {
                    'DataType': 'String',
                    'StringValue': 'Transactional'
                    }
                }
            )
        print(responsesns)
        return close(session_attributes, 'Fulfilled', build_response_message('I will let the team know and they will be reaching out to you via email!'))
