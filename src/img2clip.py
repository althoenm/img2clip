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
spinner = halo.Halo(text='Analyzing text...', spinner='dots')
spinner.start()

try:
    base64_image = image_encoder.encode_image(image_path)
    llm_response = openai_request.openai_request(base64_image)
    clipboard_manager.copy_to_clipboard(llm_response)
    spinner.succeed('Text extraction complete, smash that ⌘ / ctrl V!')  # Display green checkmark and message
except Exception as e:
    spinner.fail(str(e))  # Display red cross and error message
