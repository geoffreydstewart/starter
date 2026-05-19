"""Small conversion helpers and CLI entrypoints."""


def int_to_hex(value: int) -> str:
    """Convert an integer to a lowercase hex string."""
    return hex(value)


def hex_to_int(value: str) -> int:
    """Convert a hex string to an integer."""
    return int(value, 16)


def prompt_int_to_hex() -> str:
    """Prompt for an integer and return it as a hex string."""
    value = int(input("Enter an integer: "))
    return int_to_hex(value)


def prompt_hex_to_int() -> int:
    """Prompt for a hex number and return it as an integer."""
    value = input("Enter a hex number: ")
    return hex_to_int(value)


def int_to_hex_cli() -> None:
    """CLI entrypoint for integer to hex conversion."""
    print(prompt_int_to_hex())


def hex_to_int_cli() -> None:
    """CLI entrypoint for hex to integer conversion."""
    print(prompt_hex_to_int())
