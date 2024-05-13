import boto3
import pymysql
from botocore.exceptions import NoCredentialsError

def read_data_from_s3(bucket_name, file_name):
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        data = response['Body'].read().decode('latin-1', errors='replace')
        return data
    except NoCredentialsError as e:
        print("AWS credentials not found:", e)
        return None
    except Exception as e:
        print("Error reading data from S3:", e)
        return None

def push_to_rds(data):
    try:
        # Connect to RDS (replace with your RDS configuration)
        connection = pymysql.connect(host='my-db.cp0yay242i6r.us-east-2.rds.amazonaws.com',
                                     user='user',
                                     password='user123',
                                     database='my-db')
        
        with connection.cursor() as cursor:
            # Example: Insert data into RDS table
            sql = "INSERT INTO your_table (column_name) VALUES (%s)"
            cursor.execute(sql, (data,))
        
        connection.commit()
        print("Data pushed to RDS successfully")
    except Exception as e:
        print("Error pushing data to RDS:", e)

def push_to_glue_database(data):
    try:
        # Push data to Glue Database
        # Replace this with your code to push data to Glue Database
        print("Data pushed to Glue Database")
    except Exception as e:
        print("Error pushing data to Glue Database:", e)

if __name__ == "__main__":
    # Read data from S3
    bucket_name = 'siddhi-bucket'
    file_name = 'sample.csv'
    data = read_data_from_s3(bucket_name, file_name)
    
    if data:
        # Push data to RDS
        push_to_rds(data)
    else:
        # If data not available from S3, push to Glue Database
        push_to_glue_database(data)
