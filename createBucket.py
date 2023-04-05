import sys

# [START storage_create_bucket_class_location]
from google.cloud import storage


def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the coldline storage
    class
    """
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "\t\nCreated bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket


# [END storage_create_bucket_class_location]

if __name__ == "__main__":
    try:
        create_bucket_class_location(bucket_name=str(input("\t\nEnter the bucket name : ")))
    except Exception as e:
        print("\n\tError : ",e)
        print("\n\trolling back !")
    finally:
        print("\n\tprogram finished !!")