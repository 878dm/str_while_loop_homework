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
        if "!"<=s[i] and s[i]<="&":
            x+=1
        i+=1
        
    return x
print(main("#h#@@@@@ashta@g@@@@@$"))