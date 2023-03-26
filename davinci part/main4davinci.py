import json
import openai

openai.api_key = 'abcdef' # your API key
prompt_raw = 'Your task is to parse an unstructured [..]' # see above

def parse_job_posting(job_posting: str):
    full_prompt = prompt_raw % (job_posting,) # insert actual job post into prompt
    num_prompt_tokens = int(len(full_prompt) / 3) # estimate the length of the prompt
    max_tokens = 4000 - num_prompt_tokens # calculate the max available tokens for the response

    # call the OpenAI API
    response = openai.Completion.create(
        model='text-davinci-003', # the best GPT-3 model
        prompt=full_prompt,
        temperature=0,
        max_tokens=max_tokens,
        top_p=0.1,
        stop=['```'],
        echo=True # returns the whole prompt including the completion
    )

    result_raw = response.choices[0].text
    json_str = result_raw.split('```json')[1].strip() # since we used echo=True, we can split on the json marker

    return json.loads(json_str)