import pandas as pd
import numpy as np


def df_format(df):
    #Changer les types object en category
    obj_cols = list(df.select_dtypes("object").columns)
    for c in obj_cols:
        df[c] = df[c].astype("category")
    
    #Changer les types int64 en int64, int32, int16 ou int8 suivant le max

    
    int_cols = list(df.select_dtypes("integer").columns)
    encodings = [np.int8, np.int16, np.int32]
    for c in int_cols:
        m = np.abs(df[c]).max()
        for e in encodings:
            if m < np.iinfo(e).max:
                df[c] = e(df[c])
                break
    
    #Changer les types float64 en float32
    float_cols = list(df.select_dtypes("float").columns)
    for c in float_cols:
        df[c] = np.float32(df[c])


def format_carcteristiques(datadir, outdir):
    fn = datadir / "carcteristiques-2021.csv"
    outfn = outdir / "carcteristiques-2021.parquet"

    df = pd.read_csv(fn, sep=";", decimal=',', parse_dates= [['an','mois','jour','hrmn']],infer_datetime_format=True)
    df = df.rename(columns={"lum":"luminosity", "int":"intersection", "agg":"agglomeration", "atm":"weather", "col":"collision"})
    df_format(df)
    df.to_parquet(outfn)


    #Pour run : python -m src.data.make_dataset data\raw data\interim