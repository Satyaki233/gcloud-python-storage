
import sys

# [START storage_delete_file]
from google.cloud import storage


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    generation_match_precondition = None

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to delete is aborted if the object's
    # generation number does not match your precondition.
    blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
    generation_match_precondition = blob.generation

    blob.delete(if_generation_match=generation_match_precondition)

    print(f"\n\tBlob {blob_name} deleted.")


# [END storage_delete_file]

if __name__ == "__main__":
    try:
        delete_blob(
            bucket_name=str(input("\n\tEnter the name of the bucket : ")), 
            blob_name=str(input("\n\tEnter file name to delete"))
        )
    except Exception as e:
        print("\n\tError : ",e)
        print("\n\trolling back !")
    finally:
        print("\n\tprogram finished !!")