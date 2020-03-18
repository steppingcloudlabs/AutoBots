import pandas as pd
import base64

data = pd.read_csv('./PhotoExport_60.csv', sep=",")

for idx, data in data.iterrows():
     code = data['photo']
     userId = data['userId']
     imgdata = base64.b64decode(code)
     with open('./photos/'+userId, 'wb') as f:
         f.write(imgdata)
         f.close()
