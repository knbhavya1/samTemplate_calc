import json

# import requests


def lambda_handler(event, context):
    num1= event["num1"]
    num2= event["num2"]

    

def add(num1,num2):
    return num1 + num2    

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2   

print(add(num1,num2))
print(sub(num1,num2))
print(multiply(num1,num2))                 

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


    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e


   # return {
       # "statusCode": 200,
       # "body": json.dumps({
        #    "message": "hello world",
            # "location": ip.text.replace("\n", "")
   #     }),
  #  }

