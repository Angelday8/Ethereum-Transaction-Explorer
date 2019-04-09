# Ethereum-Transaction-Explorer
Organizes transactions from an ethereum public key into a CSV file with respective prices


This script acquires all transactions into an ethereum wallet, looks up the price of Ethereum at the date the transaction was performed from coinmarketcap, calculates the value of that transaction for that day and exports the result into an Excell Sheet (.csv)

How to use:

 1 - Open config.json file with notepad
 
 2 - Place the ethereum address to search after the address tag. Make sure to use "" around the wallet. It should look as following:
 
  "address": "0x15C4...",
  
 3 - (Optional but recommended) - From limitations of the web3py library, the transactions for a given wallet can only be looked up by searching every block in the network. This will take a lot of type starting from block 0. In order to save many hours you may change the starting block lookup. Use ethscan to search for the first transaction done in the wallet, and place the block number for that transaction in the config file. It should look as following:
 
  "start_block": 53540
  
 4 - Run the script. When completed a csv file will be created in the folder called "transactions.csv"
 
 
