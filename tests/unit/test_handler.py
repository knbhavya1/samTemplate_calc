import json
import unittest

#import pytest

from hello_world import app

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(10,5),15)
        self.assertEqual(app.add(-1,1),0)
        self.assertEqual(app.add(-1,-1),-2)

    def test_sub(self):
        self.assertEqual(app.sub(10,5),5)
        self.assertEqual(app.sub(-1,1),-2)
        self.assertEqual(app.sub(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(app.multiply(10,5),50)
        self.assertEqual(app.multiply(-1,1),-1)
        self.assertEqual(app.multiply(-1,-1),1) 

if __name__ == '__main__':
     unittest.main()               

# @pytest.fixture()
# def apigw_event():
#     """ Generates API GW Event"""

#     return {
#         "body": '{ "test": "body"}',
#         "resource": "/{proxy+}",
#         "requestContext": {
#             "resourceId": "123456",
#             "apiId": "1234567890",
#             "resourcePath": "/{proxy+}",
#             "httpMethod": "POST",
#             "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
#             "accountId": "123456789012",
#             "identity": {
#                 "apiKey": "",
#                 "userArn": "",
#                 "cognitoAuthenticationType": "",
#                 "caller": "",
#                 "userAgent": "Custom User Agent String",
#                 "user": "",
#                 "cognitoIdentityPoolId": "",
#                 "cognitoIdentityId": "",
#                 "cognitoAuthenticationProvider": "",
#                 "sourceIp": "127.0.0.1",
#                 "accountId": "",
#             },
#             "stage": "prod",
#         },
#         "queryStringParameters": {"foo": "bar"},
#         "headers": {
#             "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
#             "Accept-Language": "en-US,en;q=0.8",
#             "CloudFront-Is-Desktop-Viewer": "true",
#             "CloudFront-Is-SmartTV-Viewer": "false",
#             "CloudFront-Is-Mobile-Viewer": "false",
#             "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
#             "CloudFront-Viewer-Country": "US",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#             "Upgrade-Insecure-Requests": "1",
#             "X-Forwarded-Port": "443",
#             "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
#             "X-Forwarded-Proto": "https",
#             "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
#             "CloudFront-Is-Tablet-Viewer": "false",
#             "Cache-Control": "max-age=0",
#             "User-Agent": "Custom User Agent String",
#             "CloudFront-Forwarded-Proto": "https",
#             "Accept-Encoding": "gzip, deflate, sdch",
#         },
#         "pathParameters": {"proxy": "/examplepath"},
#         "httpMethod": "POST",
#         "stageVariables": {"baz": "qux"},
#         "path": "/examplepath",
#     }


# def test_lambda_handler(apigw_event):

#     ret = app.lambda_handler(apigw_event, "")
#     data = json.loads(ret["body"])

#     assert ret["statusCode"] == 200
#     assert "message" in ret["body"]
#     assert data["message"] == "hello world"
