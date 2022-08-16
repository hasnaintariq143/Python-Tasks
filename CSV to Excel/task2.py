import pandas

csv=pandas.read_csv(r'1.csv',encoding='latin1')
csv.to_excel(r'1.xlsx',index=None,header=True)
