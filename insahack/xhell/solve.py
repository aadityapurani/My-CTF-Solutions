import xlwings as xw
wbxl=xw.Book('xHell.xlsx')
for c in xrange(1, 257):
	for d in xrange(1, 257):
		wbxl.sheets['Feuil1'].range('B1').value = c+46
		wbxl.sheets['Feuil1'].range('C1').value = c
		wbxl.sheets['Feuil1'].range('D1').value = d
		wbxl.sheets['Feuil1'].range('E1').value = d+119
		if wbxl.sheets['Feuil1'].range('E82').value == 1:
			print "INSA{"+str(c+46)+"-"+str(c)+"-"+str(d)+"-"+str(d+119)+"}"

#INSA{75-29-13-132}
#INSA{203-157-13-132}
