
import boto3

vpc = boto3.client('ec2')

# Creating Route Table


def CreateRouteTable():
    response1 = vpc.create_route_table(
        VpcId='vpc-058bb5e4a9f4e125a',
        TagSpecifications=[
            {
                'ResourceType': 'route-table',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Route table 1'
                    },
                ]
            },
        ]
    )

    print(response1)
    rtid = response1['RouteTable']['RouteTableId']
    print(rtid)
    print()
    
    #associate RT
    response2 = vpc.associate_route_table(
        RouteTableId=rtid,
        SubnetId='subnet-092ce14954459a3a5',
    )

    print(response2)


def main():
    CreateRouteTable()
    
if __name__ == "__main__":
    main()