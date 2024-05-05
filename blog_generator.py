import openai

# insert openAI API key below
openai.api_key = ''


# 'text-davinci-002' deprecated in GPT3.5, use 'gpt-3.5-turbo-instruct' instead. 
def generate_blog(paragraph_topic):
    response = openai.Completion.create(
        
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a paragraph about the following topic ' + paragraph_topic,
        
        #language models read and write text in chunks called tokens, 1 token ~= 4 chars in English, 30 tokens ~= 1-2 sentence(s), 100 tokens ~= 75 words, 2048 tokens ~= 1,500 words 
        max_tokens = 400,
        
        # hyperparameter 0-2 that affects the computation of token probabilities when generating output through the large language model. (2 = most random)
        temperature = 0.3
    )

    retrieve_blog = response.choices[0].text

    return retrieve_blog

print(generate_blog("Explain how sharpe ratio measures the performance of an investment."))

# cant run program due to exceeded quota. not paying for gpt lol
