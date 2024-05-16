import boto3

IamClient = boto3.client('iam')



def ListGroups():
    response = IamClient.list_groups()
    print("\n\t\tList of Groups")
    for user in response['Groups']:
        print(user['GroupName'])


def main():
    ListGroups()

if __name__ == "__main__":
    main()