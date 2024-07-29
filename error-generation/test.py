def remove_last_punctuation(sentence):
    # Define the punctuation marks you want to remove
    punctuation_marks = {'?', '።', '!'}
    
    # Check if the last character is a punctuation mark
    if sentence and sentence[-1] in punctuation_marks:
        return sentence[:-1], sentence[-1]
    return sentence, ""

# Example usage
input_sentence = "ሩዝን በ5 ዞኖች? ለማልማት እየሠራን ነው።"
output_sentence = remove_last_punctuation(input_sentence)
print(output_sentence)  # Output: ሩዝን በ5 ዞኖች? ለማልማት እየሠራን ነው
