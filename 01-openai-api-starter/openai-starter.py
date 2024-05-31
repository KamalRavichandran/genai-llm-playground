from dotenv import load_dotenv
from openai import OpenAI

# load all the variables found as environment variables including .env variables
load_dotenv()

# create OpenAI instance
client = OpenAI()

# Set the OpenAI model to be used
# "gpt-4o" - GPT-4o (“o” for “omni”) is OpenAI's most advanced model. It is multimodal (accepting text or image inputs and outputting text), and it has the same high intelligence as GPT-4 Turbo but is much more efficient—it generates text 2x faster and is 50% cheaper.
# "gpt-4-turbo" - GPT-4 is a large multimodal model (accepting text or image inputs and outputting text) that can solve difficult problems with greater accuracy than any of the previous models.
# "gpt-3.5-turbo" - GPT-3.5 Turbo models can understand and generate natural language or code and have been optimized for chat using the Chat Completions API but work well for non-chat tasks as well.
MODEL = "gpt-3.5-turbo"

# Invoke the API call
# model - set the model to be used
# messages - a list of message objects, where each object has two required fields, role and content
# temperature - this param controls the randomness of the generated text. A higher temperature will make the output more random, while a lower temperature will make it more focused and deterministic
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
