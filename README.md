\`\`\`markdown
# img2clip

This project aims to leverage multi-modal LLM capabilities for the purpose of extracting text from user submitted images and automatically sending the extracted content to the user's clipboard for easy pasting in other applications.

## Setting up OpenAI Key

Before you can use img2clip, you need to set your OpenAI key as an environment variable. Here's how you can do this:

### On macOS and Linux:

1. Open your terminal.
2. Run the following command, replacing `your_openai_key` with your actual OpenAI key:

\`\`\`bash
echo 'export OPENAI_KEY="your_openai_key"' >> ~/.bash_profile
\`\`\`

3. Restart your terminal or run `source ~/.bash_profile` to load the new environment variable.

### On Windows:

1. Open the Start Menu and search for "Environment Variables".
2. Click on "Edit the system environment variables".
3. In the System Properties window that appears, click on "Environment Variables".
4. In the Environment Variables window, click on "New" under the "User variables" section.
5. Enter `OPENAI_KEY` as the variable name and your actual OpenAI key as the variable value.
6. Click "OK" in all windows to save the new environment variable.

If you don't set the OpenAI key as an environment variable, you will be prompted to enter it when you run img2clip.
\`\`\`