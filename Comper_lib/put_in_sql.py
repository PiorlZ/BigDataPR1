from sqlalchemy import create_engine
import pandas as pd
from Comper_lib.settings import ENGINE, SHEET, TABLE_NAME, EXCEL_FILE

engine = create_engine(ENGINE)


def sheets(data, file):
    if data == SHEET:
        df = pd.read_excel(file, SHEET)
        df.to_sql(name=TABLE_NAME, con=engine, if_exists='append', index=False)


def write():
    with pd.ExcelFile(EXCEL_FILE) as xlsx:
        for sheet_name in xlsx.sheet_names:
            sheets(sheet_name, xlsx)
