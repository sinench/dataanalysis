import pandas as pd

def format_carcteristiques(datadir, outdir):
    fn = datadir / "carcteristiques-2021.csv"
    outfn = outdir / "carcteristiques-2021.parquet"
    df = pd.read_csv(fn, sep=";", decimal=',')
    df.to_parquet(outfn)