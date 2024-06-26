from sqlmodel import Session
from  db_service.db import engine
import db_service.model
from db_service.models import Part
import pandas as pd
import numpy as np


def parse_table_sheet(table, sheet):
    df =  table.parse(table.sheet_names[2])
    df = df.replace({np.nan: None})
    print(df.head())
    return df

def read_excel_file(file_path: str) -> pd.io.excel._base.ExcelFile:
    tables = pd.ExcelFile(file_path)
    print(tables.sheet_names, type(tables))
    tables_list = []
    for table in tables.sheet_names:
        tables_list.append(parse_table_sheet(tables, table))
    print(tables_list)
    return tables_list 

def input_values_db(values: pd.DataFrame, db_engine: engine = engine, model: models) -> None:
     with Session(db_engine) as session:
            for row in values.itertuples():
                print(list(row))
                row = list(map(lambda item: str(item) if item is not None else None,row[1:]))
                part = Part()
                attrs = list(part.__dict__.keys())[2:]
                for atr, value in zip(attrs, row):
                    setattr(part, atr, value)
                session.add(part)
            session.commit()

   
if __name__ == '__main__':
    file = 'Данные_для_базы.xlsx'
    df = read_excel_file(file)    
    #for values in df:
    #   input_values_db(values)

