import boto3
s3 = boto3.client('s3')

#Create bucket
bucket_name = 'bucket-using-boto3-18-05-2024'
region = 'ap-south-1'  

location_constraint = {'LocationConstraint': region}

# Create the bucket with region specified

def CreateBucket():
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration=location_constraint
    )

    print(response)

def main():
    CreateBucket()

if __name__ == "__main__":
    main()