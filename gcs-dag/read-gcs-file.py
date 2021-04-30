# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os

from airflow import models
from airflow.models import Variable
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator


BUCKET = "my-test-airflow-gcs-bucket"
PROJECT_ID = Variable.get("gcp-project-id")

PATH_TO_REMOTE_FILE = "test-gcs-example-remote.txt"
PATH_TO_LOCAL_FILE = "test-gcs-example-local.txt"

with models.DAG(
    "example_gcs_to_local",
    start_date=days_ago(1),
    schedule_interval=None,
    tags=['example'],
) as dag:
    download_file = GCSToLocalFilesystemOperator(
        task_id="download_file",
        object_name=PATH_TO_REMOTE_FILE,
        bucket=BUCKET,
        filename=PATH_TO_LOCAL_FILE,
    )
    
#     run_this = BashOperator(
#         task_id='output_file',
#         bash_command='cat ' + PATH_TO_LOCAL_FILE,
#     )
    
#     download_file >> run_this
    
if __name__ == "__main__":
    dag.cli()
