import boto3


class ResourceCleaner:

    def __init__(self):
        self.ec2 = boto3.client("ec2")

    def find_cleanup_candidates(self):
        response = self.ec2.describe_instances(
            Filters=[
                {
                    "Name": "instance-state-name",
                    "Values": ["stopped"]
                }
            ]
        )

        candidates = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                candidates.append(instance["InstanceId"])

        return candidates

    def dry_run(self):
        candidates = self.find_cleanup_candidates()

        print("===== CLEANUP DRY RUN =====")

        if not candidates:
            print("No stopped EC2 instances found.")
            return

        print("Resources that would be cleaned:")
        for instance_id in candidates:
            print(f"- {instance_id}")

        print("\nNo resources were deleted.")