Use this blueprint to run in batch mode a pretrained model on custom data, which classifies tasks within given textual data and creates a CSV file that maps each input task to its category and priority.

To classify texts by predefined categories, provide data in one of two forms, either a JSON file with listed texts or a CSV file with a text column. The blueprint starts with an S3 Connector that connects to a private bucket with your predefined data.

Complete the following steps to deploy a task-classifier model in batch mode:
1. Click **Use Blueprint** button. The cnvrg Blueprint Flow page displays.
2. Click the **S3 Connector** task to display its dialog.
   - Within the **Parameters** tab, provide the following Key-Value information:
     - Key: `bucketname` − Value: provide the data bucket name
     - Key: `prefix` − Value: provide the main path to the data folder
   - Click the **Advanced** tab to change resources to run the blueprint, as required.
3. Click the **Batch-Predict** task to display its dialog.
   - Within the **Parameters** tab, provide the following Key-Value pair information:
     - Key: `batch_input` − Value: provide the path to the data file including the S3 prefix
     - `/input/s3_connector/<prefix>/task_prioritization_data` − ensure the data path adheres this format

     NOTE: You can use prebuilt data example path provided.

   - Click the **Advanced** tab to change resources to run the blueprint, as required.
4. Click the **Run** button. The cnvrg software deploys in batch mode a task-classifier model that classifies and prioritizes tasks within given textual data and creates a CSV file with each task, its category, and priority.
5. Track the blueprint’s real-time progress in its Experiments page, which displays artifacts such as logs, metrics, hyperparameters, and algorithms.
6. Select **Batch Inference > Experiments > Artifacts** and locate the output CSV file.
7. Click the **batch.csv** File Name, click the Menu icon, and select **Open File** to view the output CSV file.

A custom model that classifies and prioritizes textual tasks has been deployed in batch mode. To learn how this blueprint was created, click [here](https://github.com/cnvrg/task-prioritization-blueprint).
