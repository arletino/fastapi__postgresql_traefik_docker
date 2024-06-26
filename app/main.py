from sqlmodel import Session

import db_service.db
# from db_service.db import engine
# from db_service.models import Part
# import pandas as pd
# import numpy as np


# file = 'Данные_для_базы.xlsx'

# def read_excel_file(file_path: str):
#     table = pd.ExcelFile(file)
#     return table.sheet_names, table 

# def parse_table_sheet(table)
#     df =  table.parse(table.sheet_names[2])
#     print(df.columns.tolist())
#     df = df.replace({np.nan: None})
#     print(df.head())

# with Session(engine) as session:
#     for row in df.itertuples():
#         print(list(row))
#         row = list(map(lambda item: str(item) if item is not None else None,row[1:]))
#         part = Part()
#         attrs = list(part.__dict__.keys())[2:]
#         for atr, value in zip(attrs, row):
#             setattr(part, atr, value)
#         print(part.__dict__)
        
#         session.add(part)
#     session.commit()

