# Write your solution here
def find_words(search_term: str):
    with open("words.txt") as my_file:
        match_list = []
        for line in my_file:
            line = line.strip()

            if search_term==line:
                match_list.append(line)

            elif search_term[0] == "*":
                remove_wildcard = search_term[1:]
                if line.endswith(remove_wildcard):
                    match_list.append(line)

            elif search_term[-1] == "*":
                remove_wildcard = search_term[:-1]
                if line.startswith(remove_wildcard):
                    match_list.append(line)

            elif "." in search_term:
                if len(line) == len(search_term):
                    index = 0
                    while index < len(search_term):
                        if search_term[index] == ".":
                            index += 1
                            continue
                        if search_term[index] != line[index]:
                            break
                        index += 1
                    else:
                        match_list.append(line)

        return match_list
if __name__ == "__main__":
    #print(find_words("ca."))
    #print(find_words("cat"))
    print(find_words("reson*"))
    print(find_words("*okes"))



