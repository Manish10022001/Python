#Program for Deciding whether the given word contains Vowel char or Not
word = input("Enter a word:")
res = "does not have Vowel char"

for ch in word:
    # print(ch)
    if ch.lower() in ['a','e','i','o','u']:
        res = "has a vowel char"
        break
print("{} {}".format(word,res))