import pyperclip

def copy_to_clipboard(text):
    """
    Copy the given text to the clipboard.

    Args:
        text (str): The text to be copied to the clipboard.
    """
    pyperclip.copy(text)