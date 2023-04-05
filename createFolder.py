# [START storage_delete_file]
from google.cloud import storage
#blob_list = []
def create_folder(bucket_name, destination_folder_path):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_folder_path)

    blob.upload_from_string('')

    print('\n\tCreated {} .'.format(destination_folder_path))


if __name__ == "__main__":
    try:
        create_folder(
            bucket_name = str(input("\t\nEnter the bucket name : ")),
            destination_folder_path = str(input("\t\nEnter the destination folder name(format : folder_name/) : "))
        )
    except Exception as e:
        print("\n\t",e)
    finally:
        print("\n\tprogram finished !")


    
