
import finnhub


class ApiHandler:
    def __init__(self, API_KEY, stock = 'APPL'):
        self.finnhub_connection = finnhub.Client(api_key=API_KEY)
        self.stock = stock
        
    def is_valid(self):
        count = self.finnhub_connection.symbol_lookup(self.stock)['count']
        
        # If no results match, then count 0 thus not valid stock symbol.
        if count != 0:
            return True
        else:
            return False

    def get_profile(self):
        print(self.stock)
        return self.finnhub_connection.company_profile2(symbol = self.stock)

    def get_metrics(self,lastyear,today): 
        return self.finnhub_connection.earnings_calendar(symbol=self.stock, _from=lastyear, to=today, international=False)

    def get_news(self,lastyear,today):
        return self.finnhub_connection.company_news(self.stock,_from =lastyear,to=today)

    def get_candles(self, resolution, lastyear,today):
        return self.finnhub_connection.stock_candles(self.stock,resolution,lastyear,today)