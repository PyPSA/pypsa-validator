from typing import Any


def create_details_block(summary: str, content: Any) -> str:
    """Wrap content in a details block (if content is not empty)."""
    if content:
        return f"<details>\n    <summary>{summary}</summary>\n{content}</details>\n\n\n"
    else:
        return ""
