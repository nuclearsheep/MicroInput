import lettersc
from digitalio import DigitalInOut, Direction, Pull
import board
from time import sleep
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
prevstate = False
signal = 0
silence = 0
dits = 0
bits = 0
UNIT_TIME = 100

while True:

	for i in row_pins:
		if i == ONE:
			pass
		else:
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
				lettersc.lookup(coords, ONE)
				#lettersc.Release(ONE)
				while (col == 0) & (~ONE.value):
					signal += 1
					sleep(0.001)
				#else:
					#signal = 0
			else:
				if (prevstate != ONE.value):
					if not signal:
						pass
					elif signal < (UNIT_TIME*2):  # Tally signal to binary
						dits <<= 1  # Dit
						bits += 1
						print("dit")
					else:
						dits <<= 1  # Dah
						dits += 1
						bits += 1
						print("dah")
					silence = 0
					mask = 0b000011111111
					dits = ((dits & mask) | (bits << 8))
					prevstate = ONE.value
				else:
					silence += 1
					if (silence < UNIT_TIME*2):
						pass
					elif (silence < (UNIT_TIME*6)):
						if dits != 0:
							dits = lettersc.emitLetter(dits)
							#dits = 0
							bits = 0
							signal = 0
					else:
						#dits = lettersc.emitLetter(dits)
						dits = 0
						bits = 0
			sleep(0.001)

		#row_pins[row].direction = Direction.INPUT
		#row_pins[row].pull = Pull.UP
	#print(bin(dits), signal)

