import blockchain_explorer
import cmc_explorer
import datetime
import configparser
import pandas as pd
import decimal


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Config']


if __name__ == '__main__':
    config = load_config()

    if config['address'] is None:
        print('No address set. Open config.json and set address to ethereum lookup address')
    else:
        address_transactions = blockchain_explorer.scan_transactions(config['address'], int(config['start_block']))

        print('Downloading Ethereum price history from Coinmarketcap...')
        ethereum_price_history = cmc_explorer.load_price_df()

        transaction_price_history = []
        print('address transactions:', address_transactions)
        for transaction in address_transactions:
            transaction_data = blockchain_explorer.get_transaction_data(transaction)
            print('transaction date:', transaction_data['date'])
            price_at_date = ethereum_price_history.loc[str(transaction_data['date'].date())]['Close']
            transaction_price_history.append([
                transaction_data['date'],
                transaction_data['amount'],
                price_at_date,
                transaction_data['amount'] * decimal.Decimal(str(price_at_date))
            ])
        df = pd.DataFrame(transaction_price_history, columns=['Date', 'Amount', 'Price', 'Value'])
        print(df)
        df.to_csv('transactions.csv', index=False)
