def hyperlink(url: str, text: str) -> str:
    """Render text as a clickable OSC 8 terminal hyperlink."""
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"
