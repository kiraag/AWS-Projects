# EC2 Volume Encryption Checker with Alerts

This project automates the process of checking Amazon EC2 volumes for encryption status. It uses AWS Lambda to analyze all volumes and send alerts through Amazon SNS for any unencrypted volumes. CloudWatch is integrated to schedule periodic checks.

---

## Features

- **Automated Volume Scanning**: Lists all EC2 volumes and identifies unencrypted ones.
- **Alert System**: Sends detailed alerts about unencrypted volumes via Amazon SNS.
- **Scheduled Monitoring**: Runs checks automatically on a schedule using Amazon CloudWatch.

---

## Prerequisites

1. An AWS account.
2. IAM roles with necessary permissions:
   - **`ec2:DescribeVolumes`** for EC2 access.
   - **`sns:Publish`** for SNS alerts.
3. Python environment for local testing (optional).

---

## Setup Instructions

### Step 1: Create an SNS Topic

1. Open the **Amazon SNS Console**.
2. Create a new topic (e.g., `UnencryptedVolumesAlert`).
3. Add subscriptions (e.g., email addresses) and confirm them.
4. Note the Topic ARN for later use.

### Step 2: Configure Lambda Function

1. Open the **AWS Lambda Console**.
2. Create a new Lambda function.
3. Use the following Python code:

```python
import json
import boto3

# Initialize AWS clients
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

# Specify your SNS topic ARN
SNS_TOPIC_ARN = '<YOUR_SNS_TOPIC_ARN>'

def lambda_handler(event, context):
    try:
        # Fetch all volumes
        response = ec2_client.describe_volumes()
        volumes = response.get('Volumes', [])

        # Check encryption status for each volume
        unencrypted_volumes = []
        for volume in volumes:
            if not volume['Encrypted']:
                unencrypted_volumes.append(volume['VolumeId'])

        # Send alert if unencrypted volumes are found
        if unencrypted_volumes:
            message = {
                'total_volumes': len(volumes),
                'unencrypted_volumes': unencrypted_volumes
            }
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject='Unencrypted Volumes Alert',
                Message=json.dumps(message, indent=2)
            )

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Alert sent for unencrypted volumes',
                    'details': message
                })
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'All volumes are encrypted'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

4. Replace `<YOUR_SNS_TOPIC_ARN>` with your SNS topic ARN.

### Step 3: Assign IAM Role

Attach a role to the Lambda function with the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeVolumes",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "<YOUR_SNS_TOPIC_ARN>"
        }
    ]
}
```

Replace `<YOUR_SNS_TOPIC_ARN>` with the ARN of your SNS topic.

### Step 4: Integrate with CloudWatch

1. Open the **Amazon CloudWatch Console**.
2. Create a new rule with the following settings:
   - **Event Source**: Schedule (e.g., `Rate(1 day)`).
   - **Target**: Select your Lambda function.
3. Enable the rule.

---

## Testing

1. **Manual Testing**: Trigger the Lambda function from the AWS Lambda Console.
2. **Scheduled Testing**: Wait for the CloudWatch rule to trigger the function based on the defined schedule.
3. **Verify Alerts**: Check the SNS subscription (e.g., email) for alerts.

---

## Output Example

### Alert Sent for Unencrypted Volumes
```json
{
    "total_volumes": 3,
    "unencrypted_volumes": [
        "vol-0abcdef1234567890"
    ]
}
```

### All Volumes Encrypted
```json
{
    "message": "All volumes are encrypted"
}
```

