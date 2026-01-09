import boto3

class DIDLibrary:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket_name = 'did-library-bucket'

    def upload_media(self, file_name, object_name=None):
        if object_name is None:
            object_name = file_name
        self.s3_client.upload_file(file_name, self.bucket_name, object_name)

    def list_media(self):
        response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
        return [item['Key'] for item in response.get('Contents', [])]

    def delete_media(self, object_name):
        self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_name)

# Example usage
if __name__ == "__main__":
    library = DIDLibrary()
    library.upload_media('example_media.mp4')
    print(library.list_media())
    library.delete_media('example_media.mp4')
