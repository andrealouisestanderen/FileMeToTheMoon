import sys

from pyspark import SparkContext, SparkConf


def countWordsSpark(filename):
    # create Spark context with necessary configuration. local since the program will not run in a
    # distributed cluster, and * indicating that the host machine should use all its cores to
    # realize the performance of the virtual worker threads.
    sc = SparkContext("local[*]", "PySpark Word Count Exmaple")

    # read data from text file and split each line into words
    words = sc.textFile(
        'static/' + filename).flatMap(lambda line: line.split(" "))

    # count the occurrence of each word
    wordsmap = words.map(lambda word: (word, 1))
    wordCounts = wordsmap.reduceByKey(lambda a, b: a + b)

    out = wordCounts.collect()
    outSort = sorted(out, key=lambda word: -word[1])

    words = []
    values = []
    for element in outSort:
        word = element[0].replace('"', '').replace('?', '')
        value = element[1]
        words.append(word)
        values.append(value)
        #print('first el: ', word)
        #print('second el: ', value)

    total_unique_words = wordCounts.count()
    total_words = wordsmap.count()

    #print('total u_w: ', total_unique_words)
    #print('total w: ', total_words)

    return total_words, total_unique_words, words, values


# countWordsSpark()


"""
sc = SparkContext("local[*]", "PySpark Word Count Exmaple")

words = sc.textFile("static/MindenSep12_2020.txt").flatMap(lambda line: line.split(" "))

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

wordCounts.saveAsTextFile("/home/ansible/cloud/lab5/output/")
"""
