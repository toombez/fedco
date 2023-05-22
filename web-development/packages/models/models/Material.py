from typing import Tuple
from models.Model import Model
from dataclasses import dataclass

@dataclass
class Material(Model):
    label: str
    href: str

    @staticmethod
    def from_sql(sql: Tuple[str, str]):
        """
        Create `Material` from sql

        Parameters
        ----------
            sql: Tuple[str, str]
                sql result (label, href)

        Returns
        -------
            Material
        """
        label, href = sql
        return Material(label, href)

    def to_sql(self) -> Tuple[str, str]:
        """
        Create tuple for pass to sql from `Material`

        Returns
        -------
            sql (label, href)
        """
        return (self.label, self.href)
