import sys

# [START storage_delete_bucket]
from google.cloud import storage


def delete_bucket(bucket_name):
    """Deletes a bucket. The bucket must be empty."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    print(f"\t\nBucket {bucket.name} deleted")


# [END storage_delete_bucket]

if __name__ == "__main__":
    try:
        delete_bucket(bucket_name=str(input("\t\nEnter the bucket name : ")))
    except Exception as e:
        print("\n\tError : ",e)
        print("\n\trolling back !")
    finally:
        print("\n\tprogram finished !!")