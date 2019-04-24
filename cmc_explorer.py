from cmc import coinmarketcap
from datetime import datetime


def load_price_df():
    cryptos = ['ethereum']
    start_date, end_date = datetime(2017, 6, 1), datetime.now()

    df = coinmarketcap.getDataFor(cryptos, start_date, end_date)

    return df['ethereum']