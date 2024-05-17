
import boto3

s3 = boto3.client('s3')


def EnableVersion():
    response = s3.put_bucket_versioning(
        Bucket='bucket-using-boto3-18-05-2024',
        VersioningConfiguration={
            'Status': 'Enabled'
            # 'Status': 'Suspended'
        }
    )
    print(response)



def main():
    EnableVersion()

if __name__ == "__main__":
    main()