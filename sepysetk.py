from serial import Serial
import sys
import time
from tkinter import *

arduino = Serial('COM36', 9600, timeout =1)
def prepare_coomand(*args):

	b = args[0] + 48
	arduino.write(b.to_bytes(Lenght=1, buteorder='big', signed=False))

def serial_print():
	recive = str(arduino.readline())
	t = ("b'", "\\r\\n'" "\\n'")
	for i in t:
		recive = recive.replace(i, '')
	l = recive.split('\\t')
	if len(l) > 1;
		for i in l:
			print(i, end = "\t")
		print()
	else:
		print(l[0])


root = Tk()
def vpered(event):
	print('поехал вперед')
knopka = Button(root, text='вперед')
knopka.bind('w',vpered)
knopka.grid(row=1, column=2)
def vpered(event):
	label.insert(END, 'w')

def vpravo(event):
	print('я повернулся на право и поехал вперед')
SUS = Button(root, text='вправо')
SUS.bind('d',vpravo)
SUS.grid(row=2, column=3)
def vpravo(event):
	label.insert(END, 'd')


def vlevo(event):
	print('я повернулся на лево и еду вперед')
Amogus = Button(root, text='влево')
Amogus.bind('a',vlevo)
Amogus.grid(row=2, column=1)
def vlevo(event):
	label.insert(END, 'a')


def nazad(event):
	print('я повернулся назад и поехал вперед')
Amongaus = Button(root, text='назад')
Amongaus.bind('s',nazad)
Amongaus.grid(row=2, column=2)
def nazad(event):
	label.insert(END, 's')


def Za_vardo(event):
	print('Za vardo')
slave = Button(root, text='стоп')
slave.bind('z',Za_vardo)
slave.grid(row=3, column=2)
def Za_vardo(event):
	label.insert(END, 'z')

root.mainloop()