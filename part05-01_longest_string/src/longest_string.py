def longest(strings: list):
    longest=strings[0]
    for item in strings:
        if len(longest)<len(item):
            longest=item
    return (longest)
if __name__ == "__main__":
    longest(["hi", "hiya", "hello", "howdydoody", "hi there"])
    longest(["ab","a"])