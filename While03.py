def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    x=0
    while i<len(s):
        x+=s[i].isalpha()
        i+=1
    return len(s)-x
print(main("#hash555tag@$"))