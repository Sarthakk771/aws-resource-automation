from datetime import datetime
from pathlib import Path


class ReportGenerator:

    def generate_ec2_report(self, instances):
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = reports_dir / f"ec2_audit_{timestamp}.txt"

        with open(report_file, "w", encoding="utf-8") as file:
            file.write("AWS RESOURCE AUTOMATION - EC2 AUDIT REPORT\n")
            file.write("=" * 60 + "\n")
            file.write(
                f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            file.write("=" * 60 + "\n\n")

            if not instances:
                file.write("No EC2 instances found.\n")
                return report_file

            for instance in instances:
                file.write(f"Instance ID : {instance['id']}\n")
                file.write(f"State       : {instance['state']}\n")
                file.write(f"Status      : {instance['status']}\n")
                file.write(f"Type        : {instance['type']}\n")
                file.write(f"Name        : {instance['name']}\n")
                file.write(f"Project     : {instance['project']}\n")
                file.write(f"Environment : {instance['environment']}\n")
                file.write(f"Managed By  : {instance['managed_by']}\n")
                file.write(f"Expires At  : {instance['expires_at']}\n")
                file.write(
                    f"Findings    : {', '.join(instance['findings'])}\n"
                )
                file.write("-" * 60 + "\n")

        return report_file