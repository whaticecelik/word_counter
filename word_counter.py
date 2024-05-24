text = str(input("Enter the text to find out the number of words: "))

def count(text):
  words = text.split()
  print(type(words))
  word_count = len(words)
  return word_count

numOfWords = count(text)
print("There are", numOfWords, "words in the text.")
