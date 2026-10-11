def analyze_string(s):
    vowels = "aeiouAEIOU"
    vowel_chars = ""
    consonant_chars = ""
    num_vowels = 0
    num_consonants = 0
    num_digits = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_chars += char
                num_vowels += 1
            else:
                consonant_chars += char
                num_consonants += 1
        elif char.isdigit():
            num_digits += 1

    print("Vowels:", vowel_chars, num_vowels)
    print("Consonants:", consonant_chars, num_consonants)
    print("Numbers:", num_digits)


def is_palindrome(s):
    s = s.lower()
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char
    if cleaned == cleaned[::-1]:
        print(f'"{s}" is a palindrome')
    else:
        print(f'"{s}" is not a palindrome')


input_str = input("Please input the string: ")
analyze_string(input_str)
is_palindrome(input_str)

