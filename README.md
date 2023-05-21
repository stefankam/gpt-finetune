# gpt-finetune
The idea of this project is

1. Using GPT , we will figure out whether fake news in ukrain war is predictable . The challenge is to find out how to perform fine tuning in this supervised learning classification, assuming that GPT tools do not need feature selection algorithms which is usually the most difficult task in machine learning.
2. Perform network modeling on the ukrain war news data in order to find the fake news hubs, perhaps find out where the fake news originate from, and how they are cascaded.

In the first step, we used the python file minedata.py to extract data from https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/response_conflict-reponse_conflits/crisis-crises/ukraine-fact-fait.aspx?lang=eng#dataset-filter

this file also formats data to the gpt-finetune requested format according to https://platform.openai.com/docs/guides/fine-tuning/advanced-usage

{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
...
  
then we divide data into data_training.jsonl and data_verification.jsonl in order to first train the model , and further verify the model.

To start the modeling, we use the command
  
openai api fine_tunes.create -t data_training.jsonl -v data_validation.jsonl -m ada
  
This will use the ada model to fine tune , and test the model according the extracted and formatted data. 
Once the modeling is done, we could see the results using the following command:
  
openai api fine_tunes.results -i ft-72Zdxae7SlTzGb5uwuDdBqik
  
The analysis result appears in results.csv, attached, which includes the following fields:
  
step,elapsed_tokens,elapsed_examples,training_loss,training_sequence_accuracy,training_token_accuracy,validation_loss,validation_sequence_accuracy,validation_token_accuracy
  
In order to predict a label (completion), one needs to follow the predure bellow:
  
curl https://api.openai.com/v1/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": YOUR_PROMPT, "model": FINE_TUNED_MODEL}'

 curl https://api.openai.com/v1/completions -H "Content-Type: application/json" -H "Authorization: Bearer $OPENAI_API_KEY" -d '{"prompt":"Posted on:</strong> 2023-05-18 - National Defence</p><p><strong>The facts:</strong></p><ul class=lst-spcd><li>On May 16, a Patriot battery in Kyiv defended against a Russian missile barrage that included Kinzhal missiles.</li><li>Ukrainian authorities have also released photos of debris from an earlier Kinzhal missile attack that a Ukrainian Patriot battery intercepted on May 3.</li><li>Russia appears to have repeatedly and specifically targeted Patriot sites in Ukraine over the past two weeks, likely because of the system&rsquo;s combat effectiveness.</li></ul><p><strong","max_tokens": 1,"model": "ada:ft-personal-2023-05-20-20-12-44"}'
