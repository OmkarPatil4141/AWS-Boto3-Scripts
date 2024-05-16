import boto3

IamClient = boto3.client('iam')


def DeleteUser():
    response = IamClient.delete_user(UserName='boto3-user5')  #specify your username here
    print("\nUser deletd successfully!!")


def main():
    DeleteUser()

if __name__ == "__main__":
    main()