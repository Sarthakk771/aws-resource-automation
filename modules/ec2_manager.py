import boto3


class EC2Manager:

    def __init__(self):
        self.ec2 = boto3.client("ec2")

    def get_instances(self):
        response = self.ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "id": instance["InstanceId"],
                    "state": instance["State"]["Name"],
                    "type": instance["InstanceType"]
                })

        return instances

    def provision_instance(
        self,
        ami_id,
        instance_type,
        key_name,
        security_group_id
    ):
        response = self.ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=[security_group_id],
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": "AWS-Automation-Test"},
                        {"Key": "Project", "Value": "AWS-Resource-Automation"},
                        {"Key": "Environment", "Value": "Development"},
                        {"Key": "ManagedBy", "Value": "Boto3"}
                    ]
                }
            ]
        )

        instance = response["Instances"][0]

        return instance["InstanceId"]