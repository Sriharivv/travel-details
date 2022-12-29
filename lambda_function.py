import json
from Businesslogiclayer import UserManager
from decimal import * 

user_manager = UserManager()

 

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def getbyid(param):
    print(param)
    item=user_manager.get_user(tablename="employeedetails1",parameter=param)
    return item

 

def getall():
    response=user_manager.getall_users(tablename="employeedetails1")
    return response


def lambda_handler(event, context):
    if event['httpMethod']=='GET':
        parameter=event['queryStringParameters']
        print(parameter)
        if parameter is None:
            print("hello ")
            response = getall()
            return {
                'statusCode': 200,
                'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(response,cls=DecimalEncoder)
            }

        else:
            response=getbyid(parameter)
            return {
                'statusCode': 200,
                'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(response,cls=DecimalEncoder)
            }
    else:
        data=json.loads(event['body'])
        # client=boto3.client("sns")
        # resp=client.publish(TopicArn="arn:aws:sns:ap-south-1:025051377485:employeenotification",Message=json.dumps({"event":"employeenotification","body":"booking id :"+data['id']+" is either updated or added"}))
        action=user_manager.add_user(tablename="employeedetails1",value=data)
        return {
            'statusCode': 200,
            'body': 'successfully Added Employee!',
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }


 
