import openai

openai.api_key = 'abcdef' # your API key

#utilizing embedding we can determine the similarity of the text read
#similarity can be used to perform tasks such as filtering and sorting which was more difficult before embedding
def get_embedding(job_description: str):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=job_description
    )
    return response.data[0].embedding