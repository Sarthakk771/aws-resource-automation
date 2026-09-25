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