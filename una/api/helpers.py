def safe_cast_int(string):
    integer = int(string) if string.isdigit() else None
    return integer
