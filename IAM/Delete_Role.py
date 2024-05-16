import boto3

IamClient = boto3.client('iam')

def DeleteRole():
    response = IamClient.delete_role(RoleName='botoRole-2') #specify your role name here
    print('\nRole deleted successfully!!')


def main():
    DeleteRole()

if __name__ == "__main__":
    main()