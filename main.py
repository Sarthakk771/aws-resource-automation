import logging

from modules.ec2_manager import EC2Manager
from modules.audit import ResourceAuditor
from modules.report import ReportGenerator
from modules.s3_manager import S3Manager
from modules.cleanup import ResourceCleaner
from modules.iam_manager import IAMManager


logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


AMI_ID = "ami-0fef201115eefe936"
INSTANCE_TYPE = "t3.micro"
KEY_NAME = "aws-automation-key"
SECURITY_GROUP_ID = "sg-0de7ec919e9ddbf84"
S3_BUCKET = "aws-resource-automation-230355213948"


def main():
    ec2_manager = EC2Manager()
    auditor = ResourceAuditor()
    report_generator = ReportGenerator()
    s3_manager = S3Manager(S3_BUCKET)
    cleaner = ResourceCleaner()
    iam_manager = IAMManager()

    print("===== AWS RESOURCE AUTOMATION =====")
    print("1. Check EC2")
    print("2. Provision EC2")
    print("3. Audit EC2")
    print("4. Cleanup Dry Run")
    print("5. IAM Audit")

    choice = input("Enter choice: ")

    if choice == "1":
        instances = ec2_manager.get_instances()

        if not instances:
            print("No EC2 instances found.")
            return

        for instance in instances:
            print(f"Instance ID : {instance['id']}")
            print(f"State       : {instance['state']}")
            print(f"Type        : {instance['type']}")
            print("-" * 30)

    elif choice == "2":
        print("Starting EC2 provisioning...")
        logger.info("EC2 provisioning started")

        instance_id = ec2_manager.provision_instance(
            AMI_ID,
            INSTANCE_TYPE,
            KEY_NAME,
            SECURITY_GROUP_ID
        )

        print("EC2 instance created successfully!")
        print(f"Instance ID: {instance_id}")

        logger.info(f"EC2 instance created: {instance_id}")

    elif choice == "3":
        print("===== EC2 AUDIT =====")
        logger.info("EC2 audit started")

        instances = auditor.audit_ec2()

        report_file = report_generator.generate_ec2_report(instances)

        print(f"Report generated: {report_file}")

        s3_location = s3_manager.upload_report(report_file)

        print(f"Uploaded to S3: {s3_location}")

        logger.info(
            f"EC2 audit completed. Report: {report_file}"
        )

        logger.info(
            f"Report uploaded to S3: {s3_location}"
        )

        if not instances:
            print("No EC2 instances found.")
            return

        for instance in instances:
            print(f"Instance ID : {instance['id']}")
            print(f"State       : {instance['state']}")
            print(f"Status      : {instance['status']}")
            print(f"Type        : {instance['type']}")
            print(f"Name        : {instance['name']}")
            print(f"Project     : {instance['project']}")
            print(f"Environment : {instance['environment']}")
            print(f"Managed By  : {instance['managed_by']}")
            print(f"Expires At  : {instance['expires_at']}")
            print(f"Findings    : {', '.join(instance['findings'])}")
            print("-" * 40)

    elif choice == "4":
        logger.info("Cleanup dry run started")

        cleaner.dry_run()

        logger.info("Cleanup dry run completed")

    elif choice == "5":
        logger.info("IAM audit started")

        iam_manager.audit_users()

        logger.info("IAM audit completed")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()