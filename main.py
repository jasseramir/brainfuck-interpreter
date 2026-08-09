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

    validation = validate(clean)

    if validation["has_syntax_err"]:
        raise SyntaxError(validation["err_type"])

    stack = []
    jumps = {}

    for i in range(len(clean)):
        char = clean[i]

        if char == "[":
            stack.append(i)

        if char == "]":
           start = stack.pop()

           jumps[start] = i
           jumps[i] = start

    pointer = 0
    output = ""

    tape = [0] * 30000

    i = 0

    while i < len(clean):
        match clean[i]:
            case ">":
                # Max memory size: 30,000 cells
                if pointer + 1 >= 30000:
                    raise IndexError("Out of range (Right)")

                pointer += 1

            case "<":
                if pointer - 1 < 0:
                    raise IndexError("Out of range (Left)")

                pointer -= 1

            case "+":
                tape[pointer] = (tape[pointer] + 1) % 256

            case "-":
                tape[pointer] = (tape[pointer] - 1 + 256) % 256

            case ".":
                output += chr(tape[pointer])

            case ",":
                char = input("Enter a character:")

                if not char:
                    raise RuntimeError("Insufficient input")

                char = char[0]

                # Max cell value: 255
                if ord(char) > 255:
                    raise RuntimeError("Can't save this type of character")

                tape[pointer] = ord(char)

            case "[":
                if (tape[pointer] == 0):
                    i = jumps[i]

            case "]":
                if tape[pointer] != 0:
                    i = jumps[i]

        i += 1

    return output
