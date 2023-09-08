import yfinance as yf

class Ativo():

    def __init__(self, symbol):
        self.symbol = symbol
        self.info = (yf.Ticker(str(self.symbol))).info


    # def get_info(self):
    #     data = yf.Ticker(str(self.symbol))
    #     info = data.info
    #     return info

    def get_current_price(self):
        data = self.info["currentPrice"]
        print(f"o preço da ação é  R$ {data}")
        return data #retorna o valor da acao em tempo real

    def get_stock_name(self):
        data = self.info["longName"]
        print (f"o nome da ação é {data}")
        return data

    def get_dividend_rate(self):
        data = self.info["dividendRate"]
        print(f"o valor de dividendos: R$ {data}")
        return data













