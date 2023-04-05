from google.cloud import storage

blob_list = []


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    

    # Note: The call returns a response only when the iterator is consumed.
    # print("\n\tThe files are :")
    for blob in blobs:
        #print("\t",blob.name)
        blob_list.append(blob.name)

def delete_blob(bucket_name, blob_name):

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

def get_files_to_delete(bucket_name,blob_list,file_type):
    for i in blob_list:
        if file_type in i:
            delete_blob(bucket_name,i)


if __name__=="__main__":
    try:
        s_bucket_name=str(input("\n\tEnter the name of the bucket : "))
        list_blobs(s_bucket_name)
        get_files_to_delete(
            s_bucket_name,
            blob_list,
            file_type=str(input("\n\tEnter the file extension you want to delete : "))
            )
        
    except Exception as e:
        print("\n\tError : ",e)
        print("\n\trolling back !")
    finally:
        print("\n\tprogram finished !!")