## List of supported database type strings
valid_db_types: list[str] = ["sqlite", "postgres", "mssql"]


def validate_db_type(in_str: str = None) -> bool:
    """Validate db_type string in functions that utilize db_type."""
    if not in_str:
        raise ValueError("Missing input string to validate")

    if in_str not in valid_db_types:
        return False

    return True
