import sys
import image_encoder
import openai_request
import clipboard_manager
import halo

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Please provide an image path as an argument.")
    sys.exit(1)

# Get the image path from the first command-line argument
image_path = sys.argv[1]

# Start the halo spinner
spinner = halo.Halo(text='Analyzing image...', spinner='dots')
spinner.start()

try:
    # Encode the image to base64
    base64_image = image_encoder.encode_image(image_path)

    # Make a request to OpenAI for text extraction
    llm_response = openai_request.openai_request(base64_image)

    # Copy the extracted text to clipboard
    clipboard_manager.copy_to_clipboard(llm_response)

    # Display success message with a green checkmark
    spinner.succeed('Text extraction complete, smash that ⌘ / ctrl V!')
except Exception as e:
    # Display error message with a red cross
    spinner.fail(str(e))
