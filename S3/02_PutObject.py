
import boto3

s3 = boto3.client('s3')


def PutObject():
    response = s3.put_object(
        
        Body='S3/image.png',
        Bucket='bucket-using-boto3-18-05-2024',
        Key='myimg',              
    )

    print(response)


def main():
    PutObject()

if __name__ == "__main__":
    main()
