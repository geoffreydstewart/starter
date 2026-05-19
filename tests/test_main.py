from starter.main import hex_to_int, int_to_hex, prompt_hex_to_int, prompt_int_to_hex


def test_int_to_hex_converts_int_to_lowercase_hex() -> None:
    assert int_to_hex(10) == "0xa"
    assert int_to_hex(255) == "0xff"


def test_hex_to_int_converts_prefixed_and_unprefixed_hex() -> None:
    assert hex_to_int("0xa") == 10
    assert hex_to_int("ff") == 255


def test_prompt_int_to_hex(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "255")

    assert prompt_int_to_hex() == "0xff"


def test_prompt_hex_to_int(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "0xa")

    assert prompt_hex_to_int() == 10
