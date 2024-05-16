import boto3

IamClient = boto3.client('iam')



def CreateUser():
    response = IamClient.create_user(
    UserName='boto3-user5',             #here you can use any username
    Tags=[
        {
            'Key': 'Department',
            'Value': 'DevSecOps_Engineers'
        },
    ],
)
    print("\n\nUser created Successfully!! with the name",response['User']['UserName'])



def main():
    CreateUser()

if __name__ == "__main__":
    main()