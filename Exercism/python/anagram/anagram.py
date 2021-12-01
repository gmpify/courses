def find_anagrams(word, candidates):
    result = filter(lambda x: sorted(x.lower()) == sorted(word.lower()) and x.lower() != word.lower(), candidates)
    return list(result)