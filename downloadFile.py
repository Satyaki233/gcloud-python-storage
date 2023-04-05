
import sys

# [START storage_download_file]
from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "\n\tDownloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )


# [END storage_download_file]

if __name__ == "__main__":
    try:
        download_blob(
            bucket_name=str(input("\n\tEnter the bucket name : ")),
            source_blob_name=str(input("\n\tEnter the blob name : ")),
            destination_file_name=str(input("\n\tEnter the destination file name (including path) : ")),
        )
    except Exception as e:
        print("\n\tError : ",e)
        print("\n\trolling back !")
    finally:
        print("\n\tprogram finished !!")