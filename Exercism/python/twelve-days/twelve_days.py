def recite(start_verse, end_verse):
    result = []

    lyrics = (
        ('first', 'a Partridge in a Pear Tree.'),
        ('second', 'two Turtle Doves, and '),
        ('third', 'three French Hens, '),
        ('fourth', 'four Calling Birds, '),
        ('fifth', 'five Gold Rings, '),
        ('sixth', 'six Geese-a-Laying, '),
        ('seventh', 'seven Swans-a-Swimming, '),
        ('eighth', 'eight Maids-a-Milking, '),
        ('ninth', 'nine Ladies Dancing, '),
        ('tenth', 'ten Lords-a-Leaping, '),
        ('eleventh', 'eleven Pipers Piping, '),
        ('twelfth', 'twelve Drummers Drumming, ')
    )

    for i in range(start_verse - 1, end_verse):
        verses = [f"On the {lyrics[i][0]} day of Christmas my true love gave to me: "]
        verses.extend(map(lambda x: x[1], lyrics[i::-1]))
        
        result.append(''.join(verses))

    return result
