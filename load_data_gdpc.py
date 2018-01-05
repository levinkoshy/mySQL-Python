import pandas as pd
from sqlalchemy import create_engine

# engine to connect with mysql server
engine = create_engine('mysql://root@localhost:3306/freddata')

# read the text file as dataframe
gdpc_dataframe = pd.read_csv(r"C:\Users\levi3\Desktop\fred_dat\umrate.txt\UNRATE_1.txt",sep='\t')

# load the dataframe to mysql freddata table
gdpc_dataframe.to_sql(name='umrate_table', con=engine, if_exists = 'replace', index=False)
print("Data loaded successfully")
