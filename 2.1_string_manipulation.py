"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My four transformations, and when each is useful:


# Your code below
# Get the sentence from the user
text = input("Enter a sentence: ")

print("\nOriginal text:", text)

# Transformation 1: All Loud Capitals
trans_1 = text.upper()
print("1. Uppercase: ", trans_1)
# CHECK: Yes! Everything turned into big capital letters just like I expected.

# Transformation 2: All Small Letters
trans_2 = text.lower()
print("2. Lowercase: ", trans_2)
# CHECK: Yes! The capital letter in the middle became a small letter.