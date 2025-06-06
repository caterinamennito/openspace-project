from table import Table
from file_utils import file_utils
from typing import List
import random
import math


class Openspace:
    def __init__(self):
        self.number_of_tables = 6
        self.tables = [Table() for _ in range(self.number_of_tables)]
        self.assigned_people = []

    def __str__(self) -> str:
        return f"An openspace with {self.number_of_tables} tables"

    def organize(self, names: List[str]):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    self.assigned_people.append(name)
                    break
        # Assuming all tables have same capacity
        table_capacity = self.tables[0].capacity
        total_seats = self.number_of_tables * table_capacity

        if len(names) > total_seats:
            dif = len(names)- total_seats
            nr_tables_to_add = int(math.ceil(dif/ table_capacity))
            new_tables =[]
            for _ in range(nr_tables_to_add):
                new_table = Table()
                self.tables.append(new_table)
                new_tables.append(new_table)
            people_to_assign = [person for person in names if person not in self.assigned_people]
            # TODO: extract this to a reusable function
            for name in people_to_assign:
                for table in new_tables:
                    if table.has_free_spot():
                        table.assign_seat(name)
                        self.assigned_people.append(name)
                        break



    def display(self):
        available_seats = 0
        for i, table in enumerate(self.tables):
            print(f"Table {i+1}: {table._inspect()}")
            available_seats += table.left_capacity()
        print(f"Seats left: {available_seats}")
