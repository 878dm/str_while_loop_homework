def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    l=0
    while i<len(s):
        if s[i]!='2' and s[i]!='4' and s[i]!='6' and s[i]!='8' and s[i]!='0':
            k+=1
            l+=int(s[i])
            # print(l)
        i+=1
    return l
print(main("1567534"))