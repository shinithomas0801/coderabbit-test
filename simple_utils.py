def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence):
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def count_characters(sentence):
   return len(sentence)

def fahrenheit_to_celsius(farenheit):
 return (farenheit - 32) * 5/9

def count_numbers(lst):
 return len([x for x in lst if isinstance(x, (int, float))])

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)   