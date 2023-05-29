"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    string = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += string.count(i)
    return result
string = input("insira algo: ")
vowel_count = count_vowels(string)
print(vowel_count)