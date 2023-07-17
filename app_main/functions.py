import re
import random
import string

def generate_random_string(min_len, max_len, ref_string=None):
    length = random.randint(min_len, max_len)
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def strip_special_characters(string):
    # Define the regex pattern to match any non-alphanumeric character
    regex_pattern = r'[^a-zA-Z0-9]'

    # Use the regex pattern to replace all special characters with an empty string
    stripped_string = re.sub(regex_pattern, '', string)

    return stripped_string

def generate_mapping_url(url):
    _url = strip_special_characters(url)
    mapping_url = generate_random_string(2, 5, ref_string=_url)
    return mapping_url