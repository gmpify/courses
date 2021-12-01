from random import randint

def has_duplicates(a):
    """
    Check if there are duplicates on the list

    p: Integer

    return: Boolean
    """
    d = 0
    for i in sorted(a):
        if d == i:
            return True
        d = i
    return False

def generate_anniversaries(p):
    """
    Generate p number of anniversaries and return them as a list.

    p: Integer

    return: List
    """
    results = []
    for i in range(p):
        d = randint(1, 365)
        results.append(d)
    return results

def run_experiment(p, n):
    """
    For n set number of people p, check the chances of people having
    the same anniversary in a given group.

    p, n: Integer

    returns: Double
    """
    results = []
    for i in range(n):
        anniversaries = generate_anniversaries(p)
        results.append(has_duplicates(anniversaries))

    return results.count(True)/len(results)

def main():
    precision = 1000
    people = 41
    chances = run_experiment(people, precision)
    print(chances)

if __name__ == '__main__':
    main()
