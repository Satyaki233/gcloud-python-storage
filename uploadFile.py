import sys

# [START storage_upload_file]
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


# [END storage_upload_file]

if __name__ == "__main__":
    try:
        upload_blob(
            bucket_name=str(input("\n\tEnter the name of the bucket : ")),
            source_file_name=str(input("\n\tEnter the path of the file to upload : ")),
            destination_blob_name=str(input("\n\tEnter the name and path of the blob : ")),
        )
    except Exception as e:
        print("\n\tError : ",e)
        print("\n\trolling back !")
    finally:
        print("\n\tstopping the program!!")
