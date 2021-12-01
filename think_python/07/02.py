def eval_loop():
    result = None
    while True:
        line = input('> ')
        if line == 'done':
            return result
        result = eval(line)
        print(result)

eval_loop()
