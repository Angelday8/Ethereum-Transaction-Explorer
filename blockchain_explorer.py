from web3 import Web3
import datetime


web3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/34af86e47c754e89bcbf63995a720ade", request_kwargs={'timeout': 60}))


def scan_transactions(address, start_block):
    address_lowercase = address.lower()
    end_block = web3.eth.blockNumber

    transactions_haxes = []

    for idx in range(start_block, end_block):
        print('Fetching block %d, remaining: %d, progress: %d%%' % (
            idx, (end_block - idx), 100 * (idx - start_block) / (end_block - start_block)))

        block = web3.eth.getBlock(idx, full_transactions=True)

        for tx in block.transactions:
            if tx['to'] == address:
                transactions_haxes.append(tx['hash'].hex())

    return transactions_haxes


def get_transaction_data(transaction):
    transaction_data = web3.eth.getTransaction(transaction)
    block_number = transaction_data['blockNumber']
    block_data = web3.eth.getBlock(block_number)
    block_timestamp = block_data['timestamp']
    dt = datetime.datetime.fromtimestamp(block_timestamp)
    print(transaction_data)
    data = {'date': dt, 'amount': web3.fromWei(transaction_data['value'], 'ether')}
    return data