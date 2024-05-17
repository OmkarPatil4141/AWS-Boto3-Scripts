import boto3
dynamodb = boto3.client('dynamodb')


def DeleteItem():
    response = dynamodb.delete_item(
        Key={
            'playerId': {
                'N': '103',
            },
            'playerName': {
                'S': 'Omkar Patil',
            }
        },
        TableName='PlayersTable',
    )

    print(response)



def main():
    DeleteItem()


if __name__ == "__main__":
    main()