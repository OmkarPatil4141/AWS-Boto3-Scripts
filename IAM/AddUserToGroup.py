import boto3

IamClient = boto3.client('iam')

def AddUserToGroup():
    response = IamClient.add_user_to_group(

    GroupName='boto-group3',     #specify your group name
    UserName='boto3-user5'       #specify your user name
)
    print("\nUser added to group successfully!!") 


def main():
    AddUserToGroup()

if __name__ == "__main__":
    main()