from os import path
from typing import Tuple

def relative_path(*relative_paths: Tuple[str, ...]):
    directory = path.dirname(__file__)

    result_path = path.join(directory, *relative_paths)

    return result_path
