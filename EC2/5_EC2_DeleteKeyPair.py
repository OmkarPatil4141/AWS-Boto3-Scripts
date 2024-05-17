import boto3

ec2=boto3.client('ec2')

def delete_key_pairs(key_pair_names):
    # Delete each key pair
    for key_name in key_pair_names:
        ec2.delete_key_pair(KeyName=key_name)
        print(f"Key pair '{key_name}' deleted.")

def main():
    key_pair_names = ['boto3key3', 'boto3key4', 'boto3key5'] 
    
    delete_key_pairs(key_pair_names)

if __name__ == "__main__":
    main()