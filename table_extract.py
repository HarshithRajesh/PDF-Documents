import tabula

table = tabula.read_pdf('weather.pdf')
table[0].to_csv('outpuct.csv',index=None)