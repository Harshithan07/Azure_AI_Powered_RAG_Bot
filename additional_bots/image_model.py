import os
import base64
import mimetypes
from openai import AzureOpenAI



client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key
)

# Load the image 
IMAGE_PATH = "C:\\Users\\harsh\\OneDrive\\Desktop\\demo_GenAI\\panda_bamboo.png"

# Encode the image
mime_type, _ = mimetypes.guess_type(IMAGE_PATH)
with open(IMAGE_PATH, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
data_url = f"data:{mime_type};base64,{encoded_image}"

# Chat prompt with image 
messages = [
    {
        "role": "system",
        "content": [
            {"type": "text", "text": "You are a helpful assistant that describes images."}
        ]
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is this animal doing in the image?"},
            {"type": "image_url", "image_url": {"url": data_url}}
        ]
    }
]

# Call the model
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stream=False
)

# Output
print("Assistant:", completion.choices[0].message.content)
print("Model:", completion.model)
print("Usage:")
print("\tPrompt tokens:", completion.usage.prompt_tokens)
print("\tCompletion tokens:", completion.usage.completion_tokens)
print("\tTotal tokens:", completion.usage.total_tokens)
