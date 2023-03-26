import json
import openai

def read_prompt_raw_file(filename):
    with open(filename, 'r') as file:
        return file.read()

openai.api_key = 'abcdef' # your API key
prompt_raw_filename = 'gpt35persona.txt'
prompt_raw = read_prompt_raw_file(prompt_raw_filename)

#more details see 
#https://marcotm.com/articles/information-extraction-with-large-language-models-parsing-unstructured-data-with-gpt/
def parse_job_posting(job_posting: str):
    full_prompt = prompt_raw % (job_posting,) # insert actual job post into prompt

    # call the OpenAI API
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant that parses unstructured job postings into structured JSON data.'},
            {'role': 'user', 'content': full_prompt}
        ],
        temperature=0
    )

    json_str = response.choices[0].message.content
    
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None