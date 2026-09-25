import boto3
from datetime import datetime


class ResourceAuditor:

    def __init__(self):
        self.ec2 = boto3.client("ec2")

    def audit_ec2(self):
        response = self.ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:

                tags = {
                    tag["Key"]: tag["Value"]
                    for tag in instance.get("Tags", [])
                }

                state = instance["State"]["Name"]

                if state == "terminated":
                    status = "TERMINATED"
                elif state == "stopped":
                    status = "STOPPED"
                elif state == "running":
                    status = "RUNNING"
                else:
                    status = state.upper()

                findings = []

                if not tags.get("Name"):
                    findings.append("UNTAGGED")

                if not tags.get("Project"):
                    findings.append("MISSING_PROJECT_TAG")

                if not tags.get("Environment"):
                    findings.append("MISSING_ENVIRONMENT_TAG")

                if not tags.get("ManagedBy"):
                    findings.append("MISSING_MANAGED_BY_TAG")

                if state == "stopped":
                    findings.append("STOPPED_RESOURCE")

                if state == "terminated":
                    findings.append("TERMINATED_RESOURCE")

                expires_at = tags.get("ExpiresAt")

                if expires_at:
                    try:
                        expiry_date = datetime.strptime(
                            expires_at,
                            "%Y-%m-%d"
                        ).date()

                        if expiry_date < datetime.now().date():
                            findings.append("EXPIRED_RESOURCE")

                    except ValueError:
                        findings.append("INVALID_EXPIRY_DATE")

                if not findings:
                    findings.append("OK")

                instances.append({
                    "id": instance["InstanceId"],
                    "state": state,
                    "status": status,
                    "type": instance["InstanceType"],
                    "name": tags.get("Name", "UNTAGGED"),
                    "project": tags.get("Project", "UNTAGGED"),
                    "environment": tags.get("Environment", "UNTAGGED"),
                    "managed_by": tags.get("ManagedBy", "UNTAGGED"),
                    "expires_at": expires_at or "NOT_SET",
                    "findings": findings
                })

        return instances