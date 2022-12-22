Use this blueprint to run in batch mode a pretrained model on Zendesk data, which connects to the Zendesk API, retrieves open tickets, and creates a CSV file that classifies each text, identifies its sentiment, and establishes its score.

To access the Zendesk tickets, an administrator must enable password access. In Admin Center, click the Apps and integrations icon in the sidebar, then select APIs > Zendesk APIs. In the Settings tab, enable password access.

To classify tasks or Zendesk subjects by predefined categories, provide data in one of two forms, either a JSON file with listed subjects or a CSV file with a subject column. The blueprint starts with a Zendesk Connector that connects to a Zendesk API with your credentials and predefined data.

Complete the following steps to deploy a task-classifier model in batch mode:
1. Click **Use Blueprint** button. The cnvrg Blueprint Flow page displays.
2. Click the **Zendesk Connector** task to display its dialog.
   - Within the **Parameters** tab, provide the following Key-Value information:
     - Key: `--domain` – Value: provide the Zendesk domain
     - Key: `--email` – Value: provide the email associated with the Zendesk account
     - Key: `--password` – Value: provide the password for the Zendesk account
     - Key:`--field` – Value: provide the subject field to be extracted from the tickets
   - Click the **Advanced** tab to change resources to run the blueprint, as required.
3. Click the **Batch-Predict** task to display its dialog.
   - Within the **Parameters** tab, provide the following Key-Value pair information:
     - Key: `batch_input` − Value: provide the path to the data file including the Zendesk prefix
     - `/input/zendesk_connector/tickets.json` − ensure the data path adheres this format

     NOTE: You can use prebuilt data example path provided.

   - Click the **Advanced** tab to change resources to run the blueprint, as required.
4. Click the **Run** button. The cnvrg software deploys in batch mode a task-classifier model that classifies and prioritizes Zendesk ticket subjects and creates a CSV file that maps each of your tickets to its category and priority.
5. Track the blueprint’s real-time progress in its Experiments page, which displays artifacts such as logs, metrics, hyperparameters, and algorithms.
6. Select **Batch Predict > Experiments > Artifacts** and locate the output CSV file.
7. Click the **batch.csv** File Name, click the Menu icon, and select **Open File** to view the output CSV file.

A custom model that classifies and prioritizes Zendesk ticket subjects has been deployed in batch mode. To learn how this blueprint was created, click [here](https://github.com/cnvrg/task-prioritization-blueprint).
