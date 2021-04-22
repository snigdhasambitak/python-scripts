### MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(sentence):
    sentence_array = sentence.split()
    return " ".join(sentence_array[::-1])

print(master_yoda('I am home'))
print(master_yoda('We are ready'))


