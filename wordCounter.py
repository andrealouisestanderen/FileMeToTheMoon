import collections


def countWords(filename):
    unique_words = {}
    textfile = open('static/' + filename, 'r')
    text_list = [line.replace(',', '').replace(
        '?', '').split(" ") for line in textfile]
    total_words = 0

    for line in text_list:
        for word in line:
            word = word.lower()
            total_words += 1
            if word not in unique_words:
                unique_words[word] = 1
            else:
                unique_words[word] += 1

    unique_words = {key: val for key, val in unique_words.items() if val != 1}

    sorted_dict = sorted(
        unique_words.items(), key=lambda kv: kv[1], reverse=True)

    sorted_unique_words = collections.OrderedDict(sorted_dict)

    words = sorted_unique_words.keys()
    values = sorted_unique_words.values()
    total_unique_words = len(unique_words)

    return total_words, total_unique_words, words, values
