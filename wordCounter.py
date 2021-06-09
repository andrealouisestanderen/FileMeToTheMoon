
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

    total_unique_words = len(unique_words)

    return total_words, total_unique_words, unique_words
