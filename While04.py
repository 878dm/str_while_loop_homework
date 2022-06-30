def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    x=0
    while i<len(s):
        if "A"<=s[i] and s[i]<="Z":
            x+=1
        i+=1
        
    return x
print(main("CodeschoolUz"))