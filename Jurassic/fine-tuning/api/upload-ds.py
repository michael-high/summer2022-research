import requests

path = 'YOUR_DATASET_PATH'
with open(path, 'rb') as ds:
    response = requests.post(
        "https://api.ai21.com/studio/v1/dataset",
        headers={"Authorization": "Bearer oEK0eJXzKWfeEH55MjUg2FKJiJsCz9R9"},
        files={
            "dataset_file": (path, ds)
        },
        data={
            "dataset_name": "YOUR_DATASET_NAME"
        }
    )