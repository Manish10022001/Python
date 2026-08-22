#Program for accepting a word and decide whether it is consonant word or not
# e.g. Apple -- not consonant word   try -- consonant word.
word = input("Enter any word: ").lower()
res = "Consonant Word" if 'a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word else "Not Consonant Word"
print("{} is {}".format(word,res))