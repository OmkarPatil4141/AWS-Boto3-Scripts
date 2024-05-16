import boto3

IamClient = boto3.client('iam')



def CreateRole():
    response = IamClient.create_role(
    RoleName='botoRole-Ec2',    #Here you can specify any name 
    AssumeRolePolicyDocument='{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": {"Service": "ec2.amazonaws.com"}, "Action": "sts:AssumeRole"}]}',
    Description='Service role for communication with EC2',
    MaxSessionDuration= 3600,
    PermissionsBoundary='arn:aws:iam::aws:policy/AdministratorAccess',
    Tags=[
        {
            'Key': 'Department',
            'Value': 'Ec2 role'
        },
    ]
)

    print("\nRole created Suceessfully!! with the name :",response['Role']['RoleName'])


def main():
    CreateRole()

if __name__ == "__main__":
    main()