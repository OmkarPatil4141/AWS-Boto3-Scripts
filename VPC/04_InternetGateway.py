
import boto3

vpc = boto3.client('ec2')

def CreateIG():
    response1 = vpc.create_internet_gateway(
        TagSpecifications=[
            {
                'ResourceType': 'internet-gateway',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'internet-gateway-boto3'
                    },
                ]
            },
        ]
    )

    print(response1)
    igw_id = response1['InternetGateway']['InternetGatewayId']


    # Attaching IGW
    response2 = vpc.attach_internet_gateway(
        InternetGatewayId=igw_id,
        VpcId='vpc-058bb5e4a9f4e125a',
    )

    print(response2)


    # Add route table to internet gateway
    response_create_route = vpc.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=igw_id,
        RouteTableId='rtb-0b1b4de1eb50978b4',
    )



def main():
    CreateIG()
    
if __name__ == "__main__":
    main()