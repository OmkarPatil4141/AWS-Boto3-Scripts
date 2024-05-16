import boto3

IamClient = boto3.client('iam')



def CreateGroup():
    response = IamClient.create_group(GroupName='boto-group3')   #Here you can specify any name
    
    print('\nGroup created successfully!! with the name :',response['Group']['GroupName'])



def main():
    CreateGroup()

if __name__ == "__main__":
    main()