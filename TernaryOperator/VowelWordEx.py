#Program for accepting a word and decide whether it is vowel word or not
# e.g. Apple -- vowel word   try -- not vowel word.
word = input("Enter any word: ").lower()
res = "Vowel Word" if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word else "Not Vowel"
print("{} is {}".format(word,res))