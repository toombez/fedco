from typing import Tuple
from abc import ABC, abstractmethod

class Model(ABC):
    @staticmethod
    @abstractmethod
    def from_sql(sql: Tuple[any, ...]):
        """
        Create model from python `sqlite3` `cursor.fetchone()` method result

        Returns
        -------
            Model
        """
        raise NotImplementedError()

    def to_sql(self) -> Tuple[any, ...]:
        """
        Create tuple for pass to python `sqlite3` `cursor.execute` method

        Returns
        -------
            Parameters for sql query
        """
        raise NotImplementedError()
