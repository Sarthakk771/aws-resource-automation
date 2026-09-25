import boto3


class IAMManager:

    def __init__(self):
        self.iam = boto3.client("iam")

    def get_users(self):
        response = self.iam.list_users()

        users = []

        for user in response["Users"]:
            users.append({
                "username": user["UserName"],
                "created": user["CreateDate"].strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

        return users

    def audit_users(self):
        users = self.get_users()

        print("===== IAM AUDIT =====")

        if not users:
            print("No IAM users found.")
            return

        for user in users:
            print(f"Username : {user['username']}")
            print(f"Created  : {user['created']}")
            print("-" * 30)