def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if s[i]!='2' and s[i]!='4' and s[i]!='6' and s[i]!='8' and s[i]!='0':
            k+=1
        i+=1
    return k
print(main("1367534"))