import lettersc
from digitalio import DigitalInOut, Direction, Pull
import board
A = DigitalInOut(board.D3)
B = DigitalInOut(board.D4)
C = DigitalInOut(board.D5)
D = DigitalInOut(board.D6)
ONE = DigitalInOut(board.D7)
TWO = DigitalInOut(board.D0)
THREE = DigitalInOut(board.D1)
FOUR = DigitalInOut(board.D2)
del board, DigitalInOut
row_pins = [A,B,C,D]
col_pins = [ONE,TWO,THREE,FOUR]
import disposable
rows = disposable.rows(row_pins)
cols = disposable.cols(col_pins)
del disposable
prevstate = ONE.value

while True:
    for i in row_pins:
        i.direction = Direction.INPUT
        i.pull = Pull.UP
    for i in col_pins:
        i.direction = Direction.INPUT
        i.pull = Pull.UP
    for row in rows:
        row_pins[row].direction = Direction.OUTPUT
        row_pins[row].value = False
        for col in cols:
            if not col_pins[col].value:
                coords = (row, col)
                print(coords)
                lettersc.lookup(coords, ONE)
            else:
                pass
        lettersc.Release(ONE)
        row_pins[row].direction = Direction.INPUT
        row_pins[row].pull = Pull.UP



