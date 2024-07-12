from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from usb_hid import devices
from time import sleep
global UNIT_TIME
global prevstate
prevstate = True
global mouse
global keyboard
mouse = Mouse(devices)
keyboard = Keyboard(devices)
del Mouse, Keyboard, devices

letters = {
	0b001000000001: 4,  #A ".-" len 2: 0b0010000000
	0b010000001000: 5,  #B "-..." len 4: 0b01000000
	0b010000001010: 6,  #C "-.-."
	0b001100000100: 7,  #D "-.." len 3: 0b001100000
	0b000100000000: 8,  #E "." len 1: 0b00010000000
	0b010000000010: 9,  #F "..-."
	0b001100000110: 10,  #G "--."
	0b010000000000: 11,  #H "...."
	0b001000000000: 12,  #I ".."
	0b010000000111: 13,  #J ".---"
	0b001100000101: 14,  #K "-.-"
	0b010000000100: 15,  #L ".-.."
	0b001000000011: 16,  #M "--"
	0b001000000010: 17,  #N "-."
	0b001100000111: 18,  #O "---"
	0b010000000110: 19,  #P ".--."
	0b010000001101: 20,  #Q "--.-"
	0b001100000010: 21,  #R ".-."
	0b001100000000: 22,  #S "..."
	0b000100000001: 23,  #T "-"
	0b001100000001: 24,  #U "..-"
	0b010000000001: 25,  #V "...-"
	0b001100000011: 26,  #W ".--"
	0b010000001001: 27,  #X "-..-"
	0b010000001011: 28,  #Y "-.--"
	0b010000001100: 29,  #Z "--.."
	0b010100001111: 30,  #1 ".----" len 5 0b0101 
	0b010100000111: 31,  #2 "..---"
	0b010100000011: 32,  #3 "...--"
	0b010100000001: 33,  #4 "....-"
	0b010100000000: 34,  #5 "....."
	0b010100010000: 35,  #6 "-...."
	0b010100011000: 36,  #7 "--..."
	0b010100011100: 37,  #8 "---.."
	0b010100011110: 38,  #9 "----."
	0b010100011111: 39,  #0 "-----"
	0b010100010001: 46,  #= "-...-"
	0b010100010111: 45,  #- "-.---"
	0b010100001001: 56,  #/ ".-..-"
	0b010100011011: 49,  #\ "--.--"
	0b010100010010: 47,  #[ "-..-."
	0b010100010011: 48,  #] "-..--"
	0b011000010101: 55,  #. ".-.-.-" len 6 0b011000
	0b011000110011: 54,  #, "--..--"
	0b011000111000: 51,  #; "---..."
	0b011000010010: 52,  #' ".-..-."
	0b010100000100: 81,  #UP "..-.."
	0b010100001010: 81,  #DOWN ".-.-."
	0b010100001000: 80,  #LEFT ".-..."
	0b010100000010: 79,  #RIGHT "...-."
	0b010000000101: 41,  #ESC ".-.-"
	0b010000001110: 44,  #SPACE "---."
	0b010000001111: 42,  #BACKSPACE "----"
	0b010100001110: 40,  #ENTER ".---."
	0b011000000011: 76,  #DELETE "....--"
	0b011000011110: 43,  #TAB ".----."
	0b010000000011: 225,  #SHIFT "..--"
	0b010100010100: 224,  #CTRL "-.-.."
	0b010100010101: 226,  #ALT "-.-.-"
	0b011000100000: 58,  #F1 "-....."
	0b011000010000: 59,  #F2 ".-...."
	0b011000001000: 60,  #F3 "..-..."
	0b011000000100: 61,  #F4 "...-.."
	0b011000000001: 62,  #F5 ".....-"
	0b011000001100: 63,  #F6 "..--.."
	0b010100000110: 64,  #F7 "..--."
	0b011000111000: 65,  #F8 "---..."
	0b010100010110: 66,  #F9 "-.--."
	0b010100001011: 67,  #F10 ".-.--"
	0b010100001100: 68,  #F11 ".--.."
	0b010100001101: 69,  #F12 ".--.-"
	0b010100011010: 102,  #Keyboard Power "--.-."
	}
toglist = {
	0b010000000011: 0,  # SHIFT 
	0b010100010100: 0,  # CTRL 
	0b010100010101: 0,  # ALT
	}
"""
def morsePress(signal, ONE):
	global prevstate
	global signal
	#print("button pressed!")
	if (prevstate != ONE.value):
		signal = 0
	else:
		signal += 1
	prevstate = ONE.value
	sleep(0.001)

def Release(button):
	global silence
	global signal
	global dits
	global bits
	global prevstate
	global UNIT_TIME

	if (prevstate != button.value):
		print(prevstate, button.value)
		if signal < (UNIT_TIME*2):  # Tally signal to binary
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
		prevstate = button.value
		sleep(0.3)
	else:
		print("silence")
		silence += 1
		if (silence < UNIT_TIME*2):
			pass
		elif (silence < (UNIT_TIME*6)):
			if dits != 0:
				emitLetter(dits)
				dits = 0
				bits = 0
		else:
			emitLetter(dits)
			dits = 0
			bits = 0

"""
def lookup(coordinates, ONE):
	if coordinates[0] == 0:
		if coordinates[1] == 0:  # RXxA3
			pass
			#morsePress(signal, ONE)
		elif coordinates[1] == 1:
			pass
		elif coordinates[1] == 2:
			pass
		else:
			pass
	elif coordinates[0] == 1:
		if coordinates[1] == 0:
			pass
		elif coordinates[1] == 1:
			mouse.click(1)  # Left
		elif coordinates[1] == 2:
			mouse.move(-3, 0, 0)
		else:
			mouse.move( 0, 0, 3)
	if coordinates[0] == 2:
		if coordinates[1] == 0:
			pass
		elif coordinates[1] == 1:
			mouse.move( 0,-1, 0)
		elif coordinates[1] == 2:
			mouse.click(4) # Middle
		else:
			mouse.move( 0, 1, 0)
	else:
		if coordinates[1] == 0:
			pass
		elif coordinates[1] == 1:
			mouse.click(2)  # Right
		elif coordinates[1] == 2:
			mouse.move( 1, 0, 0)
		else:
			mouse.move( 0, 0,-1)

def emitLetter(code):
	try:
		keyboard.press(letters[code])
		sleep(0.001)
		try:
			toglist[code]
		except:
			keyboard.release(letters[code])
		else:
			if toglist[code]:
				keyboard.release(letters[code])
			toglist[code] ^= 1
		success = 0
	except:
		success = code
	return success
