Use this blueprint to train a model on custom data, which classifies tasks within given textual data. This blueprint also establishes an endpoint that can classify tasks based on the newly trained model.

To train this model, provide data in the form of text sentences (tasks) and their categories. The blueprint starts with an S3 Connector that connects to a private bucket with your private predefined data.

NOTE: Data can be connected from a storage service such as S3, Azure, and GCS.

Complete the following steps to train the task-classifier model:
1. Click the **Use Blueprint** button. The cnvrg Blueprint Flow page displays.
2. In the flow, click the **S3 Connector** task to display its dialog.
   * Within the **Parameters** tab, provide the following Key-Value pair information:
     * Key: `bucketname` − Value: enter the data bucket name
     * Key: `prefix` − Value: provide the main path to the images folder
   * Click the **Advanced** tab to change resources to run the blueprint, as required.
3. Return to the flow and click the **Train** task to display its dialog.
   * Within the **Parameters** tab, provide the following Key-Value pair information:
     * Key: `data` − Value: provide the path to the CSV file including the S3 prefix
     * `/input/s3_connector/<prefix>/data` − ensure the data path adheres this format

     NOTE: You can use prebuilt data examples paths already provided.

   * Click the **Advanced** tab to change resources to run the blueprint, as required.
4. Click the **Run** button. The cnvrg software launches the training blueprint as set of experiments, generating a trained task-classifier model and deploying it as a new API endpoint.
5. Track the blueprint's real-time progress in its Experiment page, which displays artifacts such as logs, metrics, hyperparameters, and algorithms.
6. Click the **Serving** tab in the project and locate your endpoint.
7. Complete one or both of the following options:
   * Use the Try it Live section with any task to check the model’s ability to classify and prioritize.
   * Use the bottom integration panel to integrate your API with your code by copying in your code snippet.

A custom model and an API endpoint, which can classify and prioritize tasks, have been trained and deployed. To learn how this blueprint was created, click [here](https://github.com/cnvrg/task-prioritization-blueprint).
