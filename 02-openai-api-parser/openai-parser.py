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
    # set response format as json_object
    response_format={"type": "json_object"},
    messages=[
        {
            # set role as system and content as what exactly is required from it
            "role": "system",
            "content": """You will be provided with unstructured data, and your task is to parse it into JSON output. 
             Include Fruit name, color and taste properties""",
        },
        {
            # set role as user and fill in the prompt content which is required to be answered
            "role": "user",
            "content": """There are many fruits that were found on the recently discovered planet Goocrux. 
            There are neoskizzles that grow there, which are purple and taste like candy. 
            There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. 
            Pounits are a bright green color and are more savory than sweet. 
            There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. 
            Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, 
            and a pale orange tinge to them.""",
        },
    ],
    temperature=0.7,
)

# Print the OpenAI API response
print(response.choices[0].message.content)
