from modules.ec2_manager import EC2Manager


def main():
    ec2_manager = EC2Manager()

    instances = ec2_manager.get_instances()

    print("===== EC2 INSTANCES =====")

    if not instances:
        print("No EC2 instances found.")
        return

    for instance in instances:
        print(f"Instance ID : {instance['id']}")
        print(f"State       : {instance['state']}")
        print(f"Type        : {instance['type']}")
        print("-" * 30)


if __name__ == "__main__":
    main()