def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    x=0
    k=s.lower()
    while i<len(k):
        if k[i]!='a' and k[i]!='e' and k[i]!='i' and k[i]!='o' and k[i]!='u':
            x+=1
        i+=1
        
    return x
print(main("CsodeschoolUz"))