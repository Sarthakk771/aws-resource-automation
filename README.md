\# Python AWS Resource Automation \& Lifecycle Management



A Python-based AWS resource automation utility using Boto3 and AWS CLI to provision, audit, manage and report AWS infrastructure.



\## Technologies



\- Python

\- Boto3

\- AWS CLI

\- Amazon EC2

\- Amazon S3

\- AWS IAM

\- Linux

\- Git/GitHub



\## Features



\### EC2 Automation

\- Discover EC2 instances

\- Provision EC2 instances using Boto3

\- Configure instance type, AMI, key pair and security group

\- Apply standardized resource tags



\### Resource Auditing

\- Detect untagged EC2 resources

\- Detect missing Project, Environment and ManagedBy tags

\- Identify stopped resources

\- Identify terminated resources

\- Check ExpiresAt tags

\- Generate timestamped audit reports



\### S3 Report Storage

\- Generate local infrastructure reports

\- Automatically upload audit reports to Amazon S3

\- Organize reports under the `reports/` prefix



\### Safe Cleanup

\- Identify stopped EC2 instances as cleanup candidates

\- Provide a dry-run cleanup mode

\- No resources are deleted automatically



\### IAM Auditing

\- Retrieve IAM users using Boto3

\- Generate basic IAM inventory information



\### Logging

\- Record provisioning, auditing, cleanup and S3 operations

\- Store execution logs locally



\## Project Structure



```text

aws-resource-automation/

│

├── main.py

├── config.py

├── requirements.txt

├── README.md

│

├── modules/

│   ├── ec2\_manager.py

│   ├── audit.py

│   ├── report.py

│   ├── s3\_manager.py

│   ├── cleanup.py

│   └── iam\_manager.py

│

├── reports/

├── logs/

├── screenshots/

└── architecture/

