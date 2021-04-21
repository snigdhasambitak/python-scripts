#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# old_macdonald('macdonald') --> MacDonald

def old_macdonald(word):
    return word[:3].capitalize() + word[3:].capitalize()

print(old_macdonald('macdonald'))