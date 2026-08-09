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
                tape.append(0)
                pointer += 1

            case "<":
                pointer -= 1

            case "+":
                tape[pointer] = (tape[pointer] + 1) % 256

            case "-":
                tape[pointer] = (tape[pointer] - 1 + 256) % 256

            case ".":
                output += chr(tape[pointer])

            case ",":
                char = input("Enter a character:")

                char = char[0]

                tape[pointer] = ord(char)

            case "[":
                
            case "]":
                
        i += 1

    return output
