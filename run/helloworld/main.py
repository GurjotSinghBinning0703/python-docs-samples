# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os
import pandas as pd
from flask import Flask
from google.cloud import secretmanager
from google.cloud import storage
import gcsfs
app = Flask(__name__)


@app.route("/")
def hello_world():
    project_id = "gcp-it-ec-seoanlt-dev-tki"
    string = "teststring"
    secret_id = "Singh_test_secret"

    storage_client = storage.Client()
    bucket = storage_client.bucket("seoanlt-dev-keyword-gap")
    new_df = bucket.blob("keyword_testlist_die_dritte.csv")
    df = pd.read_csv('gs://seoanlt-dev-keyword-gap/keyword_testlist_die_dritte.csv')
    test = str(df.iloc[0])




    payload = access_secret_version(project_id = project_id,secret_id=secret_id, version_id = "1" )
    name = os.environ.get("NAME", "World")
    return "Hello Singh neuohne eigenen acc 2 {}!".format(test)







def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """

    # Import the Secret Manager client library.

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    # print("Plaintext: {}".format(payload))
    return payload

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
