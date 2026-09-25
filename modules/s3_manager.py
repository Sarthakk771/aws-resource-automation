import boto3


class S3Manager:

    def __init__(self, bucket_name):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def upload_report(self, file_path):
        file_name = file_path.name

        self.s3.upload_file(
            str(file_path),
            self.bucket_name,
            f"reports/{file_name}"
        )

        return f"s3://{self.bucket_name}/reports/{file_name}"