import boto3;

db = boto3.client('dynamodb')


def GetItem():
    response = db.get_item(
        Key={
            'RollNo': {
                'S': '105',
            },
        },
        TableName='StudentTable',
    )

    print(response)



def main():
    GetItem()


if __name__ == "__main__":
    main()