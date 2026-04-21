import json
import boto3

def lambda_handler(event, context):
    # 1. Connect to the 'AI' service
    rekognition = boto3.client('rekognition')
    
    # 2. Get the bucket name and file name from the 'event'
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # 3. Ask the AI to detect what's in the image
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=10
    )
    
    print(f"I found these in {key}:")
    for label in response['Labels']:
        print(f"- {label['Name']} ({label['Confidence']:.2f}%)")
        
    return {"status": "success"}

