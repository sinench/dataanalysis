import pandas as pd

def format_carcteristiques(datadir, outdir):
    fn = datadir / "carcteristiques-2021.csv"
    outfn = outdir / "carcteristiques-2021.parquet"
    df = pd.read_csv(fn, sep=";", decimal=',', parse_dates= [['an','mois','jour','hrmn']],infer_datetime_format=True)
    df = df.rename(columns={"lum":"luminosity", "int":"intersection", "agg":"agglomeration", "atm":"weather", "col":"collision"})
    df.to_parquet(outfn)