from openai import OpenAI
import prompts
import os
import getpass

# Get the OpenAI API key from the environment variables
openai_key = os.getenv("OPENAI_API_KEY")

# If the API key is not set in the environment variables, prompt the user to enter it
if not openai_key:
    openai_key = getpass.getpass("Please enter your OpenAI API key: ")

client = OpenAI(api_key=openai_key)

def openai_request(base64_image: str) -> str:
    """
    Sends a request to the OpenAI API to process an image.

    This function takes a base64-encoded image as input and sends a request to the OpenAI API to process the image.
    The request includes a series of messages, including a system prompt and the image data.

    Parameters:
    base64_image (str): The base64-encoded image data.

    Returns:
    str: The response from the OpenAI API.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"{prompts.SYS_PROMPT}"},
            {
            "role": "user",
            "content": [
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        temperature=0,
        max_tokens=4095,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content