# gptfinetune
The idea of this project is

1. Using GPT , we will figure out whether fake news in ukrain war is predictable . The challenge is to find out how to perform fine tuning in this supervised learning classification, assuming that GPT tools do not need feature selection algorithms which is usually the most difficult task in machine learning.
2. Perform network modeling on the ukrain war news data in order to find the fake news hubs, perhaps find out where the fake news originate from, and how they are cascaded.

In the first step, we used the python file minedata.py to extract data from https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/response_conflict-reponse_conflits/crisis-crises/ukraine-fact-fait.aspx?lang=eng#dataset-filter

this file also formats data to the gpt-finetune requested format according to https://platform.openai.com/docs/guides/fine-tuning/advanced-usage

{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
...
  
then we divided data into data_training.jsonl and data_verification.jsonl in order to first train the model , and further verify the model.

To start the modeling, we use the command
openai api fine_tunes.create -t data_training.jsonl -v data_validation.jsonl -m ada
  
This will use the ada model to fine tune , and test the model according the extracted and formatted data. 
Once the modeling is done, we could see the results using the following command:
  
openai api fine_tunes.results -i ft-72Zdxae7SlTzGb5uwuDdBqik
