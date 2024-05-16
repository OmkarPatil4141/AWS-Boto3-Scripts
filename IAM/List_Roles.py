import boto3

IamClient = boto3.client('iam')

def ListRoles():
    response = IamClient.list_roles() 
    print("\n\t\tList of Roles :")
    for user in response['Roles']:
        print(user['RoleName'])


def main():
    ListRoles()

if __name__ == "__main__":
    main()