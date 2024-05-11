import re

def remove_unnecessary_characters(text, keep_punctuation=False):
    """
    Cleans the input text by removing HTML tags, special characters (optionally keeps punctuation),
    and excessive whitespace, returning a cleaned string.

    Args:
    text (str): The text to be cleaned.
    keep_punctuation (bool): If True, retains punctuation marks.

    Returns:
    str: The cleaned text.
    """
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', str(text))
    
    # Define the character class to keep
    if keep_punctuation:
        # Keep letters, digits, whitespace, and punctuation
        pattern = r'[^\w\s\.,;:!?"\'-]'
    else:
        # Keep only letters, digits, and whitespace
        pattern = r'[^\w\s]'
    
    # Remove unwanted special characters
    text = re.sub(pattern, '', text)
    
    # Normalize whitespace to a single space and strip leading/trailing spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Example usage in a data processing context (like with pandas)
# df['clean_text'] = df['text'].apply(remove_unnecessary_characters)
