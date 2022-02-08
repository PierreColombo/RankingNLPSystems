import pandas as pd

print(pd.read_csv('glue.data').to_csv('glue.csv', index=False))
