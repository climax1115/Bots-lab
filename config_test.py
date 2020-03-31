# Name of the file (without .py extension!) that contains the bot
bot_name = 'rsi'

# Example settings for backtesting engine
sim_params = {
    'capital_base': 10,      # initial capital in BTC
    'fee': {
        'Long': 0.0015,      # fee settings for Long
        'Short': 0.0015,     # fee settings for Short
    },
    'resample': False,
    'data_frequency': '4H'  # Time frame to use (see /helpers/timeframe_resampler.py for more info)
}

# Datasource is poloniex, cryptocompare or binance
datasource = 'binance'

# Example data settings historical data poloniex
# For more information: https://poloniex.com/
data_settings_poloniex = {
    'pair': 'BTC_ETH',  # Use ETH pricing data on the BTC market
    'period': 14400,       # Use 1800 second candles
    'days_history': 100,  # Collect 100 days data
}

# Example data settings historical data cryptocompare
# For more information: https://www.cryptocompare.com/
data_settings_cryptocompare = {
    'pair': ['ETH', 'BTC'],  # Use ETH pricing data on the BTC market
    'days_history': 100,  # Collect 100 days data
    'exchange': 'Bitfinex' # exchange used when datasource is Cryptocompare
}

# Example data settings historical data binance
# For more information: https://www.binance.com/
data_settings_binance = {
    'pair': 'ETHBTC',  # Use ETH pricing data on the BTC market
    'period': '4h',   # Use 30 minute candles
    'limit': 100,  # Collect 100 candles
}
