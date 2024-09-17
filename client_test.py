import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      price = (quote['top_bid']['price']+quote['top_ask']['price'])/2
      self.assertEqual(getDataPoint(quote),(quote['stock'] , quote['top_bid']['price'], quote['top_ask']['price'], price))
      print(f"Stock ({quote['stock']}): bid = {quote['top_bid']['price']}, ask = {quote['top_ask']['price']}, price = {price}")

  def test_getRatio_calculateRatio(self):
    quotes = [
        {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
           'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
           'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}]

    price_abc = (quotes[0]['top_bid']['price'] + quotes[0]['top_ask']['price'])/2
    price_def = (quotes[1]['top_bid']['price'] + quotes[1]['top_ask']['price'])/2
    self.assertEqual(getRatio(price_abc,price_def), (price_abc / price_def))
    print(f"Ratio {quotes[0]['stock']} / {quotes[1]['stock']} = {price_abc / price_def}")

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        price = (quote['top_bid']['price']+quote['top_ask']['price'])/2
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],price ))
        print(f"Stock ({quote['stock']}): bid = {quote['top_bid']['price']}, ask = {quote['top_ask']['price']}, price = {price}")


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
