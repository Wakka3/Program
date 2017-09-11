import pickle
import pandas as pd


def pickle(df, path=None):
    pickle_path = None
    with open(pickle_path, 'wb') as f:
        pickle.dump(df, f)
    return True

def exl_file_convert_obj(books):
    exlobjs = []
    for book in (books):
        exlobj = pd.ExcelFile(book)
        exlobjs.append(exlobj)
    return exlobjs

def exl_exlobj_pull_sheet_df(exlobj, sheetname, index_col="None"):
    df = exlobj.parse(sheetname, index_col=index_col)
    return df


books = ["book1"]
sheet = "sheet1"

exlobjs = exl_file_convert_obj(books)
df = exl_exlobj_pull_sheet_df(exlobjs[0], sheet, index_col="ID")

print(df)

