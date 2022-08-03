# Task Prioritization Inference
The response from the endpoint will contain the topic and sentiment identified, with the severity score.

An example json response from the endpoint is given below:
```
{
    "prediction":
    [
        {
        "score":0.008033603429794312,
        "sentiment":"negative",
        "topic":"CHANGE_CREDIT_CARD_NUM"}
    ]
}
```

- If you would like to use your own trained model you can do so by adding the path to your model in the environment variable 'MODEL_FILE',  
For example: '/input/model.pt'. 