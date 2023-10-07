def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a=s[0]
    b=s[-1]
    return s[0]+s[-1]
print(main("hay"))
print(main("hello"))