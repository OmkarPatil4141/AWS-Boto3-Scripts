import boto3

dynamodb = boto3.client('dynamodb')


def PutItem():
    response = dynamodb.put_item(
        Item={
            'RollNo': {
                'S': '105',
            },
            'studentName': {
                'S': 'Pratik',
            }
        },
        ReturnConsumedCapacity='TOTAL',
        TableName='StudentTable',
    )

    print(response)

def main():
    PutItem()


if __name__ == "__main__":
    main()