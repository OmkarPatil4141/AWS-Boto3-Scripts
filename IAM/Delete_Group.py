import boto3

IamClient = boto3.client('iam')

def DeleteGroup():
    response = IamClient.delete_group(GroupName='boto-group2') #specify your role name here
    print("\nGroup deletd successfully!!")


def main():
    DeleteGroup()

if __name__ == "__main__":
    main()