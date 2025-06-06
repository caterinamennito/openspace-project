from table import Table
from file_utils import file_utils
from typing import List
import random


class Openspace:
    def __init__(self):
        self.number_of_tables = 6
        self.tables = [Table() for _ in range(self.number_of_tables)]

    def __str__(self) -> str:
        return f"An openspace with {self.number_of_tables} tables"

    def organize(self, names: List[str]):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
        return self.tables

    def display(self):
        for i, table in enumerate(self.tables):
            print(f"Table {i+1}: {table._inspect()}")
