from APIdata import* 
import tkinter as tk

for i in ResortIds:
	CreateData(i['id'])
	print (data[0]['name'])
