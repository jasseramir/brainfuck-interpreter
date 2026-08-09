def compile(code):
    valid = "><+-[].,"
    clean = [char for char in code if char in valid]

    pointer = 0
    output = ""

    tape = [0]

    i = 0

    while i < len(clean):
        match clean[i]:
            case ">":
                
            case "<":
                
            case "+":
                
            case "-":
                
            case ".":
                
            case ",":
                
            case "[":
                
            case "]":
                
        i += 1

    return output
