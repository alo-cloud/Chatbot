import json

def lambda_handler(event, context):

    intent_name = event['currentIntent']['name']

    message = 'Hello {} {} {}!'.format(event['currentIntent']['slots']['ClothType'],
                                    event['currentIntent']['slots']['ColorType'],
                                    event['currentIntent']['slots']['WriteLength'])


    return {
          'message' : message
      }



###---Two different codes---###



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

number1 = '16308021235'
number2 = '14025415893'

def lambda_handler(event, context):

    sns = boto3.client('sns')
    message1 = sns.publish(
        PhoneNumber = number1,
        Message = 'This is a Function Factories Test message',
        MessageAttributes={
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Transactional'
            }
        }
    )

    message2 = sns.publish(
        PhoneNumber = number2,
        Message = 'This is a Function Factories Test message',
        MessageAttributes={
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Transactional'
            }
        }
    )

    print(message1)
    print(message2)
