

import boto3

db = boto3.client('dynamodb')


def UpdateItem():

    response = db.update_item(
        TableName = 'StudentTable',

        # Column name to be updated
        ExpressionAttributeNames={
            '#C': 'studentName',
        },

        # Value to be updated
        ExpressionAttributeValues={
            ':t': {
                'S': 'OM',
            }
        },

        # Where to update
        Key={
            'RollNo': {
                'S': '105',
            }
        },

        UpdateExpression='SET #C = :t',
        # UpdateExpression='SET playerName = :t',
    )

    print(response)


def main():
    UpdateItem()


if __name__ == "__main__":
    main()