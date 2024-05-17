import boto3

rds = boto3.client('rds')

def CreateDBInstance():
    response = rds.create_db_instance(
        
        AllocatedStorage=5,
        DBInstanceClass='db.t3.micro',  # t3.micro is a supported instance class
        DBInstanceIdentifier='boto3-instance',
        Engine='mysql',  
        EngineVersion='8.0.35',  # Ensure EngineVersion matches a supported version
        LicenseModel='general-public-license',
        MasterUserPassword='omkar12345',
        MasterUsername='omkar',
    )

    print(response)


def main():
    CreateDBInstance()

if __name__ == "__main__":
    main()



