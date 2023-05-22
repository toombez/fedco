from abc import ABC

class Model(ABC):
    def prepare_for_sql(self):
        raise NotImplementedError()
