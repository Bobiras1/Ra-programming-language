import sys

# Symbol-to-command mapping
COMMANDS = {
    "𓂀": "print",   # Eye of Ra
    "𓊍": "let",     # Throne
    "𓆑": "if",      # Cobra
    "𓂻": "loop",    # Walking man
    "𓊵": "func",    # Sun rising
    "𓇳": "ai"       # Sun disk
}

# Store variables
ENV = {}

def execute(tokens):
    if not tokens:
        return
    
    cmd = tokens[0]

    # PRINT
    if cmd == "𓂀":
        expr = " ".join(tokens[1:])
        value = ENV.get(expr, expr)
        print(value)

    # LET (assignment)
    elif cmd == "𓊍":
        if len(tokens) >= 3 and tokens[2] == "=":
            var_name = tokens[1]
            value = " ".join(tokens[3:])
            ENV[var_name] = value
        else:
            print("Usage: 𓊍 name = value")

    # AI invocation
    elif cmd == "𓇳":
        prompt = " ".join(tokens[1:])
        print(f"[AI invoked with prompt: {prompt}]")

    # HELP
    elif cmd.lower() in ["help", "?"]:
        print("☥ Ra Language Commands ☥")
        for sym, meaning in COMMANDS.items():
            print(f"  {sym} : {meaning}")
        print("  help : show this message")
        print("  exit : quit REPL")

    else:
        print(f"Unknown command: {cmd}")


def run_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split()
            execute(tokens)


def repl():
    print("☉ Welcome to the Ra REPL ☉")
    print("Type 'help' for a list of commands. Type 'exit' to quit.")
    while True:
        try:
            line = input("Ra >> ").strip()
            if line.lower() in ["exit", "quit"]:
                break
            tokens = line.split()
            execute(tokens)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Ra.")
            break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()
