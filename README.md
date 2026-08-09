# Brainfuck Interpreter (Python)

A small, dependency-free [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter written in pure Python. It validates bracket syntax before running, then executes the program against a fixed-size memory tape.

## Features

- **Syntax validation** — checks bracket matching (`[` / `]`) before execution and reports the exact type of mismatch (`Unmatched '['` or `Unmatched ']'`). Validation runs on the *cleaned* code, so brackets typed inside comments are correctly ignored.
- **Comment stripping** — any character that isn't a valid Brainfuck instruction (`> < + - [ ] . ,`) is ignored, so you can freely add comments/whitespace in your source.
- **Precomputed jump table** — bracket pairs are resolved once before execution for fast loop jumps (no re-scanning on every `[`/`]`).
- **Fixed-size tape** — the tape is a full 30,000-cell array (`[0] * 30000`) allocated up front, matching standard Brainfuck behavior so moving left/right always preserves previously written values.
- **Wrapping cell values** — cell values wrap around modulo 256 (`0-255`), matching standard Brainfuck behavior.
- **Bounds checking** — raises a clear `IndexError` if the pointer tries to move past either edge of the tape.
- **Interactive input** — the `,` instruction reads a character from the user via `input()`.

## Requirements

- Python 3.10+ (uses `match` / `case` statements)
- No external dependencies

## Usage

```python
from interpreter import compile

# "Hello World!" program
program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

result = compile(program)
print(result)
```

Or run it as a script:

```bash
python interpreter.py
```

## API

### `compile(code: str) -> str`

Validates and runs a Brainfuck program.

- **`code`** — the Brainfuck source as a string. Non-instruction characters (comments, whitespace, etc.) are ignored.
- **Returns** — the program's output as a string (built from `.` instructions).
- **Raises**
  - `SyntaxError` — unbalanced brackets.
  - `IndexError` — pointer moved out of tape bounds (left of cell 0, or past cell 29,999).
  - `RuntimeError` — no input given to `,`, or an input character with a code point above 255.

### `validate(clean: list[str]) -> dict`

Checks bracket matching independently of execution. Takes the **already-cleaned** list of instruction characters (not raw source) so that stray brackets inside comments don't trigger false positives. Returns:

```python
{"has_syntax_err": False}
# or
{"has_syntax_err": True, "err_type": "Unmatched '['"}
```

## Brainfuck Instruction Reference

| Symbol | Meaning                                             |
|--------|------------------------------------------------------|
| `>`    | Move the pointer right                                |
| `<`    | Move the pointer left                                 |
| `+`    | Increment the current cell (wraps at 256)              |
| `-`    | Decrement the current cell (wraps at 256)              |
| `.`    | Output the current cell as a character                |
| `,`    | Read one character of input into the current cell      |
| `[`    | Jump past matching `]` if the current cell is 0        |
| `]`    | Jump back to matching `[` if the current cell is not 0 |

## Known Limitations

- **Input limited to ASCII/single code points ≤ 255**: multi-byte or high code-point characters raise `RuntimeError`.
- **Blocking input**: `,` uses Python's built-in `input()`, so it will block waiting for user input and prompt once per read — not ideal for programs that read large amounts of input or run non-interactively.
- **No output streaming**: output is accumulated into a string and returned only after the whole program finishes, rather than printed as it's produced.

## License

This project is licensed under the [MIT License](LICENSE).
