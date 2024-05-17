import boto3
import pymysql

# RDS instance details
db_host = 'mymysqlinstance.cfke813lcjsm.ap-south-1.rds.amazonaws.com'
db_user = 'boto_user'
db_pass = 'botomj123456'
db_name = 'zeem'   

# Create RDS client
rds_client = boto3.client('rds')

# Get RDS instance endpoint
response = rds_client.describe_db_instances(DBInstanceIdentifier='mymysqlinstance')
db_endpoint = response['DBInstances'][0]['Endpoint']['Address']

# Connect to MySQL database
try:
    conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
    cursor = conn.cursor()

    # Switch the connection to the zeem database
    conn.select_db('zeem')

    # Update roll number of John Doe in student table in zeem database
    update_data_query = "UPDATE student SET roll_no = '1234' WHERE name = 'Jane Smith'"
    cursor.execute(update_data_query)
    conn.commit()
    print("Roll number updated successfully for Jane Smith in student table in zeem database.")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()