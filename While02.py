def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    # s = "python 2022"
    i=0
    k=0
    while i<len(s):
        k+=s[i].isdigit()
        i+=1
    return k
print(main("python55 2022"))