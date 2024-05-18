def generate_words(word_list, min_length, max_length):
    """
    Generate a list of words from a given list by filtering based on length.
    
    Parameters:
    word_list (list of str): The original list of words to filter.
    min_length (int): The minimum length of words to include.
    max_length (int): The maximum length of words to include.
    
    Returns:
    list of str: A list of words that meet the length criteria.
    """
    # Filter the list of words based on the length criteria
    filtered_words = [word for word in word_list if min_length <= len(word) <= max_length]
    
    # Return the filtered list of words
    return filtered_words

# Example usage:
# Assuming 'all_words' is a list of words available in the scope
selected_words = generate_words(all_words, 3, 7)
print(selected_words)
