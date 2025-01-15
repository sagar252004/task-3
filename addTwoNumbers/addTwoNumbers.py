import json
import boto3
import base64

# AWS Lambda function to add two numbers and return the result
def lambda_add_numbers(event, context):
    try:
        # Extract numbers from the event
        num1 = event.get('num1', 0)
        num2 = event.get('num2', 0)

        # Ensure the numbers are valid integers or floats
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Both num1 and num2 must be numbers.")

        # Perform addition
        result = num1 + num2

        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': result
            })
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e)
            })
        }

# AWS Lambda function to store a document or PDF file in an S3 bucket
def lambda_store_document(event, context):
    try:
        # Extract bucket name and file information from the event
        bucket_name = event['bucket_name']
        file_name = event['file_name']
        file_content_base64 = event['file_content']  # File content should be base64 encoded

        # Decode the file content
        file_content = base64.b64decode(file_content_base64)

        # Initialize S3 client
        s3 = boto3.client('s3')

        # Upload file to S3 bucket
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'File "{file_name}" has been successfully uploaded to bucket "{bucket_name}".'
            })
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e)
            })
        }
