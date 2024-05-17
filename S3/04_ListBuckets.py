import boto3

s3=boto3.client('s3')

def ListBuckets():
    response = s3.list_buckets()
    # print(response)
    for bucket in response['Buckets']:
        print(bucket['Name'])


def main():
    ListBuckets()

if __name__ == "__main__":
    main()
