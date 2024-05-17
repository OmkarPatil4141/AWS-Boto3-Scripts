
import boto3

s3 = boto3.client('s3')

def DeleteBucket():

    response = s3.delete_bucket(
        Bucket='bucket-using-boto3-18-05-2024'
    )

    print(response)

def main():
    DeleteBucket()

if __name__ == "__main__":
    main()