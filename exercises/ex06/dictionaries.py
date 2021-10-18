"""Practice with dictionaries."""

__author__ = "730322189"


def main() -> None:
     print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def invert(given: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    invert: dict[str, str] = dict()
    just_keys: list[str] = list()
    for key in given:
        if len(invert) == 0:
            just_keys.append(given[key])
            invert[given[key]] = key
        else:
            if given[key] in just_keys:
                raise KeyError("more than one of the same key")
            else:
                just_keys.append(given[key])
                invert[given[key]] = key
    return invert


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Check which color appears most frequently."""
    colors: list[str] = list()
    counting: dict[str,int] = dict()
    favorite: str
    for key in names_and_colors:
        colors.append(names_and_colors[key])
    for color in colors:
        if color in counting:
            counting[color] += 1
        else:
            counting[color] = 1
    for item in counting:
        max: int = 0
        if counting[item] > 0:
            max = counting[item]
            favorite = item
    return favorite


def count(freq: list[str]) -> dict[str, int]:
    """Create a dictionary that counts frequency of values."""
    store: dict[str,int] = dict()
    for item in freq:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1

    return store


if __name__ == "__main__":
    main()