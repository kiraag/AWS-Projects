import json
import boto3
from datetime import datetime
import uuid

# Initialize AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = "REPLACE-WITH-YOUR-DYNAMODB-TABLE"
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Extract bucket and object key from the S3 event
        record = event['Records'][0]
        source_bucket = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Destination bucket
        destination_bucket = "REPLACE-WITH-YOUR-PRIVATE-BUCKET"
        
        # Debug logging
        print(f"[INFO] Source bucket: {source_bucket}, Object key: {object_key}")
        print(f"[INFO] Destination bucket: {destination_bucket}")
        
        # Copy object to destination bucket
        copy_source = {'Bucket': source_bucket, 'Key': object_key}
        print(f"[INFO] Copying {source_bucket}/{object_key} to {destination_bucket}/{object_key}")
        s3.copy_object(
            CopySource=copy_source,
            Bucket=destination_bucket,
            Key=object_key
        )
        print(f"[INFO] File copied successfully")
        
        # Log success entry to DynamoDB
        log_entry = {
            'LogID': str(uuid.uuid4()),
            'SourceBucket': source_bucket,
            'DestinationBucket': destination_bucket,
            'ObjectKey': object_key,
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Status': 'Success'
        }
        table.put_item(Item=log_entry)
        print(f"[INFO] Successfully logged to DynamoDB:\n{json.dumps(log_entry, indent=4)}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"File successfully copied to {destination_bucket}")
        }
    
    except Exception as e:
        # Log failure entry to DynamoDB
        error_log_entry = {
            'LogID': str(uuid.uuid4()),
            'SourceBucket': source_bucket if 'source_bucket' in locals() else "N/A",
            'DestinationBucket': destination_bucket if 'destination_bucket' in locals() else "N/A",
            'ObjectKey': object_key if 'object_key' in locals() else "N/A",
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Status': 'Failure',
            'Error': str(e)
        }
        print(f"[ERROR] Logging failure to DynamoDB:\n{json.dumps(error_log_entry, indent=4)}")
        try:
            table.put_item(Item=error_log_entry)
        except Exception as db_error:
            print(f"[ERROR] Failed to log error to DynamoDB: {str(db_error)}")
        
        # Return error response
        print(f"[ERROR] {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
