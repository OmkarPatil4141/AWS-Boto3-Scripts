import boto3

IamClient = boto3.client('iam')

def AttachGroupPolicy():
    response = IamClient.attach_group_policy(
    GroupName='boto-group3',                                 #specify your group name 
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'  #specify your policies ARN
)
    print("\nPolicy Attached successfully!!")


def main():
    AttachGroupPolicy()

if __name__ == "__main__":
    main()