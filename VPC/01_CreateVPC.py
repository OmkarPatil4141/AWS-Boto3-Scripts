import boto3

vpc = boto3.client('ec2')

def CreateVpc():
    response = vpc.create_vpc(
        CidrBlock='192.172.0.0/16',
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'VPC-Boto3'
                    },
                ]
            },
        ]
    )

    print(response)

def main():
    CreateVpc()

if __name__ == "__main__":
    main()