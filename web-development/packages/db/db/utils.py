from os import path
from typing import Tuple

def relative_path(*relative_paths: Tuple[str, ...]) -> str:
    """
    Get relative path for db package

    Returns
    -------
        Relative path
    """
    directory = path.dirname(__file__)

    result_path = path.join(directory, *relative_paths)

    return result_path

def fetch_sql_script(script_file_name: str) -> str:
    """
    Fetch relative sql script

    Parameters
    ----------
        script_file_name: str
            sql script file name without sql extension

    Returns
    -------
        sql script
    """
    with open(relative_path('sql', f'{script_file_name}.sql')) as sql:
        return sql.read()
