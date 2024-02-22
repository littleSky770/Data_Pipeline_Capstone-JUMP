import boto3
import json
import urllib3

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    url = "https://date.nager.at/Api/v3/NextPublicHolidaysWorldwide"
    response = http.request('GET', url)

    if response.status == 200:
        data = json.loads(response.data.decode('utf-8'))

        # Upload JSON data to S3 bucket
        s3_bucket = "capstone-bucket-g2"
        s3_key = "holidays.json"

        s3 = boto3.client('s3')
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=json.dumps(data))

        print(f"JSON data uploaded to S3 bucket '{s3_bucket}' with key '{s3_key}'.")
    else:
        print(f"Error: {response.status}")