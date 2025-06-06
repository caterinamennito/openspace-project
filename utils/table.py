class Seat:
    def __init__(self):
        self.free = True
        self.occupant = ""

    def __str__(self) -> str:
        return f"a {self.free} seat occupied by {self.occupant}"

    def set_occupant(self, name: str):
        self.free = False
        self.occupant = name

    def remove_occupant(self):
        self.free = True
        prev_occupant = self.occupant
        self.occupant = ""
        return prev_occupant


class Table:
    def __init__(self) -> None:
        self.capacity = 6
        self.seats = [Seat() for _ in range(self.capacity)]

    def __str__(self) -> str:
        return f"A table with {self.capacity} seats"

    def has_free_spot(self) -> bool:
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str):
        if not self.has_free_spot():
            print('This table is full!')
            return False
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self) -> int:
        return sum(1 for seat in self.seats if seat.free)

    
    # TODO: This is for debugging purpose. Delete later
    def _inspect(self):
        return [seat.occupant for seat in self.seats]