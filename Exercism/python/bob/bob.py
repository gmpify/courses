def response(hey_bob):
    stripped_hey_bod = hey_bob.strip()

    if not stripped_hey_bod:
        return 'Fine. Be that way!'
    elif stripped_hey_bod.endswith('?') and stripped_hey_bod.isupper():
        return "Calm down, I know what I'm doing!"
    elif stripped_hey_bod.endswith('?'):
        return 'Sure.'
    elif stripped_hey_bod.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
