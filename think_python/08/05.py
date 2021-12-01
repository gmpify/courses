def rotate_word(word, rotation):
    new_string = ""
    for c in word:
        if c.islower():
            from_a = ord(c) - ord("a")
            new_char = (from_a + rotation) % (ord("z") - ord("a"))
            new_string += chr(new_char + ord("a"))
        else:
            from_a = ord(c) - ord("A")
            new_char = (from_a + rotation) % (ord("Z") - ord("A"))
            new_string += chr(new_char + ord("A"))
    return new_string

print(rotate_word("Zasdas", 3))
