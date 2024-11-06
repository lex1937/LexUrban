def single_root_words(root_word: str, *other_words: str):
    """ Функция принимает два строковых параметра.
        root_word - обязательный аргумент,
        *other_words - неограниченная последовательность аргументов
    """

    same_words = []
    w1 = root_word.upper()
    for w in range(len(other_words)):
        w2 = other_words[w].upper()
        if w2.count(w1) == 1 or w1.count(w2) == 1:
            same_words.append(other_words[w])
    return same_words


result1 = single_root_words('rich', 'richiest',
                            'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement',  'Able',
                            'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
