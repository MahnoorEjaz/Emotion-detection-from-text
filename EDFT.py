# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:56:50 2023

@author: ELITEBOOK
"""
import re #import regular expression for pattern matching and string manupulation

def negation_handling_emotion_detection(text):
    # Define lists of positive and negative emotions
    positive_emotions = ['happy', 'joyful', 'excited', 'positive', 'good']
    negative_emotions = ['sad', 'unhappy', 'angry', 'negative', 'bad']
    # Define a list of negation words
    negation_words = ['not', 'no', 'never']

    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower()) # finds all occurrences of the specified pattern in the given string, Tokenize into words
    
    # Identify negations and invert the polarity of sentiment words
    negated_words = [] # list of negated words
    negation_active = False # flag to check negatiom is active or not
    for word in words:
        if word in negation_words:
            negation_active = not negation_active
        else:
            if negation_active:
                negated_words.append(word)
                negation_active=not negation_active

      
    # Determine the dominant emotion based on negation handling
    if any(emotion in negated_words for emotion in positive_emotions) and any(emotion in negated_words for emotion in negative_emotions):
        dominant_emotion="nutral"
    elif any(emotion in negated_words for emotion in positive_emotions):
        dominant_emotion = 'negative'
    elif any(emotion in negated_words for emotion in negative_emotions):
        dominant_emotion = 'positive'
    else:
        dominant_emotion = 'neutral'

    return dominant_emotion
# Example usage
text_to_analyze = "I am not good with the product."

result = negation_handling_emotion_detection(text_to_analyze)

print(f"Dominant Emotion: {result}")