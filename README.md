markdown
Copy code
# img2clip

img2clip is a Python application that extracts text from images using OpenAI's multi-modal GPT-4o model and automatically copies the extracted text to the user's clipboard.

## Demo
![img2clip demo](images/img2clip-demo.gif)

## Prerequisites

Before running the img2clip application, you need to set your OpenAI API key as an environment variable.

```bash
OPENAI_KEY="sk-p..."
```

If you do not set the API key as an environment variable, the application will prompt you to enter it manually each time you run it.

## Usage
- Install dependencies using pip install -r requirements.txt.
- Run `python img2clip.py path/to/image.jpg` to extract text from the specified image and copy it to the clipboard.
- Once the application has extracted the text, you can paste it into any text editor or application.

## Disclaimer
This project is for educational and demonstration purposes only. Use responsibly and ensure compliance with OpenAI's use case policy and any relevant laws or regulations.
