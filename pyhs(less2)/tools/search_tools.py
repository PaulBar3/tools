import os


# ! Top-Down func definitions
# Тут сейчас будем переделывать.
def simple_search(
    path: str,
    query: str,
    time_stamp: int | None = None,
    time_now: int | None = None,
) -> list[str]:
    """_summary_

    Args:
        path (str): _description_
        query (str): _description_
        time_stamp (int | None, optional): _description_. Defaults to None.
        time_now (int | None, optional): _description_. Defaults to None.

    Returns:
        list[str]: _description_
    """
    matches = []

    for address, dirs, files in os.walk(path):
        for file in files:
            if query not in file:
                continue

            full_path: str = os.path.join(address, file)  # Формируем полный путь к файлу
            if should_add_file(full_path, time_stamp, time_now):
                matches.append(full_path)
    return matches


def should_add_file(full_path, time_stamp, time_now):
    """_summary_

    Args:
        full_path (_type_): _description_
        time_stamp (_type_): _description_
        time_now (_type_): _description_

    Returns:
        _type_: _description_
    """
    if os.path.islink(full_path):
        return False
    if time_stamp:
        return time_now - os.path.getctime(full_path) < time_stamp
    return True
