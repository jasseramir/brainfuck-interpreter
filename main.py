def validate(code):
    stack = []

    for char in code:
        if char == "]" and len(stack) == 0:
            return {"has_syntax_err": True, "err_type": "Unmatched ']'"}

        if char == "[":
            stack.append(char)
        elif char == "]":
            stack.pop()

    return (
        {"has_syntax_err": True, "err_type": f"Unmatched '{stack[-1]}'"}
        if len(stack) != 0
        else {"has_syntax_err": False}
    )

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
