import pandas as pd

df = pd.read_csv(r'C:\Users\ilyao\JupyterLab\cmd\search_result.txt', header=None, sep='  ')

df = df.dropna(axis=1).rename(columns={0:'size_bt', 1:'date', 4:'time', 5:'path'}).assign(size_mb=lambda x: x.size_bt/1000000).loc[:, ['path','date','time','size_mb']].sort_values(by='path')

df.to_excel(r'C:\Users\ilyao\JupyterLab\cmd\search_result_py.xlsx', index=False, sheet_name='report')

