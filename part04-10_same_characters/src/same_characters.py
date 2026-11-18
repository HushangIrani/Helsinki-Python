def same_chars(string, index1, index2):
    if index1 > len(string) - 1 or index2 >= len(string) - 1:
        answer = False
    elif string[index1] == string[index2]:
        answer = True
    else:
        answer = False

    return answer


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 0, 12))