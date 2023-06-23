# Write your solution here
def all_the_longest(strings):
    max_length = 0
    longest_strings = []

    for string in strings:
        length = len(string)
        if length > max_length:
            max_length = length
            longest_strings = [string]
        elif length == max_length:
            longest_strings.append(string)

    return longest_strings
if __name__=='__main__':
    all_the_longest(('Alan', 'Steve', 'Seymour', 'Kim', 'Susan'))