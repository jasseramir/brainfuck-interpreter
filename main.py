def compile(code):
    valid = "><+-[].,"
    clean = [char for char in code if char in valid]

    pointer = 0
    output = ""

    tape = [0]
