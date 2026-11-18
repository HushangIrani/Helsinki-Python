# Write your solution here
def squared(text, length):
    row = 1
    height = 1
    
    while height <= length:
        while row <= length:
            print(text[0], end = "")
            text = text[1:] + text[0]
            row += 1
        
        row = 1
        height +=1
        print()
        
if __name__ == "__main__":
    squared("ab", 3)