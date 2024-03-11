import datetime
from stock import Stock
from stocks_list import StocksList

if __name__ == '__main__':
    # Create stock objects
    someStock = Stock('POP', 'Common', 8)
    otherStock = Stock('GIN', 'Preferred', 8, 2, 100)

    # Print dividend yield and P/E ratio for each stock
    print(f'{someStock.symbol} Dividend Yield: {someStock.calculate_dividend_yield(10)}')
    print(f'{otherStock.symbol} Dividend Yield: {otherStock.calculate_dividend_yield(4)}')
    print(f'{someStock.symbol} P/E Ratio: {someStock.calculate_pe_ratio(10)}')
    print(f'{otherStock.symbol} P/E Ratio: {otherStock.calculate_pe_ratio(4)}')

    # Record trades for each stock
    someStock.record_trade(10, 'Buy', 5)
    someStock.record_trade(6, 'Sell', 3)
    otherStock.record_trade(5, 'Buy', 2)
    otherStock.record_trade(4, 'Sell', 4)

    # Record a trade with a timestamp from ten minutes ago
    ten_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
    otherStock.record_trade(10, 'Buy', 3, ten_minutes_ago)

    # Print volume-weighted stock price for someStock
    print(f'{someStock.symbol} Volume Weighted Stock Price: {someStock.calculate_volume_weighted_stock_price()}')

    # Create a StocksList object and add stocks to it
    stock_list = StocksList()
    stock_list.add_stock(otherStock)
    stock_list.add_stock(someStock)

    # Print GBCE All Share Index
    print(f'GBCE All Share Index: {stock_list.calculate_gcb_all_share_index()}')

# output:
# POP Dividend Yield: 0.8
# GIN Dividend Yield: 0.5
# POP P/E Ratio: 1.25
# GIN P/E Ratio: 0.5
# POP Volume Weighted Stock Price: 4.25
# GBCE All Share Index: 3.504
