"""Contain helper functions and any constants"""

from pathlib import Path

# Get the root directory of the project
ROOT_DIR = Path(__file__).parent.parent


def insert_inputs(fields: list[str], optionals: list[int], **extra):
    data: dict[str, str | None] = {}

    extra_detail: dict[int, str] = extra.get("extra_detail", {})

    for idx, field in enumerate(
        fields
    ):  # (0, first_name), (1, last_name), (2, email), (3, format)
        value = input(
            f"""Enter {field} {"(Optional)" if idx in optionals else ""} {extra_detail.get(idx, "")} : 
            
            """
        )

        if idx in optionals and not value:
            value = None

        data[field] = value

    return data


if __name__ == "__main__":
    fields: list[str] = ["first_name", "last_name", "email", "format"]
    optionals: list[int] = [1, 2, 3]
    extra_info: dict[int, str] = {3: "(ebook, hardcover)"}
    inputs = insert_inputs(fields, optionals, extra_detail=extra_info)


# 'Enter first_name: '
# 'Enter last_name (optional): '
# 'Enter email (optional):
# 'Enter format (optional) (ebook, hardcover):
