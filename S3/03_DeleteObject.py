
import boto3

s3 = boto3.client('s3')

def DeleteObject():

    response = s3.delete_object(
        
        Bucket='bucket-using-boto3-18-05-2024',
        Key='myimg',
    )

    print(response)

def main():
    
    DeleteObject()

if __name__ == "__main__":
    main()