def anagrams(word, word_list):

    sorted_word = sorted(word.lower())


    anagrams_list = []

    for string in word_list:

        sorted_string = sorted(string.lower().replace(" ", ""))

      if sorted_word == sorted_string:

            anagrams_list.append(string)

    
    return anagrams_list