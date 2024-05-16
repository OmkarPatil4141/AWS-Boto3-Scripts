import boto3

IamClient = boto3.client('iam')



def ListUsers():
    response = IamClient.list_users()
    print("\n\t\tList of users:")
    for user in response['Users']:
        print(user['UserName']) 


def main():
    ListUsers()

if __name__ == "__main__":
    main()