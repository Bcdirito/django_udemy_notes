# Regular Expressions Notes

# .search() Example
import re

patterns = ["term1", "term2"]

text = "This is a string with term1, not the other!"

match = re.search("term1", text)

# Prints index where match starts
print(match.start())

# .split() Example

split_term = "@"

email = "user@gmail.com"

print(re.split(split_term, email))

# .findall() Example
print(re.findall("match", "test phrase match in match middle"))

# Metacharacter Syntax

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")

test_phrase = "sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd"

# * accounts for any amount of d's
# + accounts for 1 or more d's
# ? accounts for 0 or 1 d
# {} accounts for a specific count
# {} with multiple entries means either count, BUT NO SPACE AFTER COMMA!
# [] where followed by either entry in brackets
test_pattern = ["sd[sd]+"]

multi_re_find(test_pattern, test_phrase)

# Metacharacter Example 2:

searching_phrase = "This is a string! But has punctuation. How can we remove it?"

checker = [r"\w+"]

multi_re_find(checker, searching_phrase)

# [r"\d+"] -> find all digits
# [r"\D+"] -> find all nondigits
# [r"\w+"] -> find all alphanumeric

