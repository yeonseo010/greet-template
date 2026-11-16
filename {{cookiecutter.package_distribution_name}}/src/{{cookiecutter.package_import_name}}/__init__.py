"""{{ cookiecutter.package_description }}."""


def greet(name: str) -> str:
    """Return a greeting, using world for a blank name."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
