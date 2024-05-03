import openai

# insert openAI API key below
openai.api_key = ''


# 'text-davinci-002' deprecated, use 'gpt-3.5-turbo-instruct' instead. exceeded quota. not paying for gpt
def generate_blog(paragraph_topic):
    response = openai.Completion.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic ' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
    )

    retrieve_blog = response.choices[0].text

    return retrieve_blog

print(generate_blog("What was Buddha's perspective on the afterlife?"))