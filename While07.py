def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if s[i]!='1' and s[i]!='3' and s[i]!='5' and s[i]!='7' and s[i]!='9' and s[i]!='0':
            k+=1
        i+=1
    return k
print(main("5332351246"))
