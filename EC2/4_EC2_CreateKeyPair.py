import boto3

ec2 = boto3.client('ec2')

def create_key_pair():
    mykey=ec2.create_key_pair(KeyName='boto3key5')
    print("key pair created")

    print(type(mykey))
    key_name = mykey['KeyName']
    print(f"KeyName: {key_name}")

def main():

    create_key_pair()

if __name__ == "__main__":
    main()
