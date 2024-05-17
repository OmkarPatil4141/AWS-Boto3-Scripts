import boto3
import pymysql

# RDS instance details
db_host = 'mymysqlinstance.cfke813lcjsm.ap-south-1.rds.amazonaws.com'
db_user = 'boto_user'
db_pass = 'botomj123456'
db_name = None  # or set it to an empty string ''

# Create RDS client
rds_client = boto3.client('rds')

# Get RDS instance endpoint
response = rds_client.describe_db_instances(DBInstanceIdentifier='mymysqlinstance')
db_endpoint = response['DBInstances'][0]['Endpoint']['Address']

# Connect to MySQL database
try:
    conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
    cursor = conn.cursor()

    # Create zeem database if not exists
    create_db_query = "CREATE DATABASE IF NOT EXISTS zeem"
    cursor.execute(create_db_query)
    conn.commit()
    print("zeem database created successfully.")

    # Switch the connection to the zeem database
    conn.select_db('zeem')

    # Create student table in zeem database
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS student (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            roll_no VARCHAR(20) NOT NULL
        )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    print("Student table created successfully in zeem database.")

    # Insert sample data into student table
    insert_data_query = '''
        INSERT INTO student (name, roll_no) VALUES
        ('John Doe', '2021001'),
        ('Jane Smith', '2021002'),
        ('Alice Johnson', '2021003')
    '''
    cursor.execute(insert_data_query)
    conn.commit()
    print("Sample data inserted into student table.")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()