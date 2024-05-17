import boto3
import pymysql

# RDS instance details
db_host = 'mymysqlinstance.cfke813lcjsm.ap-south-1.rds.amazonaws.com'
db_user = 'boto_user'
db_pass = 'botomj123456'
db_name = 'zeem'  # or set it to an empty string ''

# Create RDS client
rds_client = boto3.client('rds')

# Get RDS instance endpoint
response = rds_client.describe_db_instances(DBInstanceIdentifier='mymysqlinstance')
db_endpoint = response['DBInstances'][0]['Endpoint']['Address']

# Connect to MySQL database
try:
    conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
    cursor = conn.cursor()

    # Delete data for John Doe from student table
    delete_data_query = "DELETE FROM student WHERE name = 'John Doe'"
    cursor.execute(delete_data_query)
    conn.commit()
    print("Data for John Doe deleted successfully from student table.")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()