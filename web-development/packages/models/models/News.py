from typing import Union, Tuple
from dataclasses import dataclass
from models.Model import Model

@dataclass
class News(Model):
    heading: str
    content: str
    image_url: Union[str, None] = None

    @staticmethod
    def from_sql(sql: Tuple[str, str, Union[str, None]]):
        """
        Create `News` model from sql result

        Parameters
        ----------
            sql: Tuple[str, str, Union[str, None]]
                (heading, content, image_url)

        Returns
        -------
            `News` model
        """
        heading, content, image_url = sql
        return News(heading, content, image_url)

    def to_sql(self):
        """
        Pass `News` to sql

        Returns
        -------
            Tuple (heading, content, image_url)
        """
        return (self.heading, self.content, self.image_url)
