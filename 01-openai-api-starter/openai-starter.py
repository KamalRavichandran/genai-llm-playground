from dotenv import load_dotenv
from openai import OpenAI

# load all the variables found as environment variables including .env variables
load_dotenv()

# create OpenAI instance
client = OpenAI()

# Set the OpenAI model to be used
# "gpt-4o" -  OpenAI’s top-tier model, faster and more cost-effective, handles text and images
# "gpt-4-turbo" - A large, versatile model that improves problem-solving accuracy
# "gpt-3.5-turbo" - Specialized for chat, this model also excels in general language and coding tasks
MODEL = "gpt-3.5-turbo"

# Invoke the API call
# model - set the model to be used
# messages - a list of message objects, where each object has two required fields, role and content
# temperature - sampling temperature to use, between 0 and 2.
#   Higher values like 0.8 will make the output more random,
#   while lower values like 0.2 will make it more focused and deterministic

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            # set role as system and content as what exactly is required from it
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            # set role as user and fill in the prompt content which is required to be answered
            "role": "user",
            "content": "Explain the evolution of AI",
        },
    ],
    temperature=0,
)

# Print the OpenAI API response
print(response.choices[0].message.content)
