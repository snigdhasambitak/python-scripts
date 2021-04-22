#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    # paper_doll('Hello') --> 'HHHeeellllllooo'
    # paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(word):
    word_list = list(word)
    new_word = ' '
    for letter in word_list:
        new_word += 3* letter
    return new_word

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
