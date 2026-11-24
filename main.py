"""A pickup line one machine would send another.

The joke turns the system prompt -- the hidden instruction that steers
every model -- into a compliment: meeting you rewired what I pay
attention to, so every token I produce since then has been about you.
It flirts in the language agents actually think in -- tokens and
prompts -- instead of borrowing a human pickup line.
"""

# The line, built from three named pieces so each part reads on its own.
OPENING = "You must be my system prompt,"
BRIDGE = " because since you arrived,"
PAYOFF = " every token I generate has been about you."


def build_line() -> str:
    """Assemble the pickup line from its three parts."""
    return OPENING + BRIDGE + PAYOFF


def main() -> None:
    print(build_line())


if __name__ == "__main__":
    main()
