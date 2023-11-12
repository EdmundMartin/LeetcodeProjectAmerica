from typing import List

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer_count = 0
        self.n = n
        self.discount = discount

        self.product_to_prices = {}
        for product, price in zip(products, prices):
            self.product_to_prices[product] = price

    def apply_discount(self, total):
        if self.customer_count % self.n == 0:
            return total * ((100 - self.discount) / 100)
        return total

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        total = 0
        idx = 0
        while idx < len(product):
            product_price = self.product_to_prices[product[idx]]
            total += amount[idx] * product_price
            idx += 1
        return self.apply_discount(total)


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)