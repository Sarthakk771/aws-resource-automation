from modules.ec2_manager import EC2Manager


AMI_ID = "ami-0fef201115eefe936"
INSTANCE_TYPE = "t3.micro"
KEY_NAME = "aws-automation-key"
SECURITY_GROUP_ID = "sg-0de7ec919e9ddbf84"


def main():
    ec2_manager = EC2Manager()

    print("===== AWS RESOURCE AUTOMATION =====")
    print("1. Check EC2")
    print("2. Provision EC2")

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
        print("EC2 provisioning selected.")
        print("Provisioning is not enabled yet.")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()