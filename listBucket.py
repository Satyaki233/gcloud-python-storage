from google.cloud import storage


def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()
    print(buckets)

    for bucket in buckets:
        print("\n\t",bucket.name )


# [END storage_list_buckets]


if __name__ == "__main__":
    list_buckets()