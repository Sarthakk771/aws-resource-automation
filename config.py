AWS_REGION = "us-east-1"

EC2_AMI_ID = "ami-0fef201115eefe936"
EC2_INSTANCE_TYPE = "t3.micro"
EC2_KEY_NAME = "aws-automation-key"
EC2_SECURITY_GROUP_ID = "sg-0de7ec919e9ddbf84"

S3_BUCKET_NAME = "aws-resource-automation-230355213948"

RESOURCE_TAGS = {
    "Project": "AWS-Resource-Automation",
    "Environment": "Development",
    "ManagedBy": "Boto3"
}

CLEANUP_STATES = [
    "stopped"
]