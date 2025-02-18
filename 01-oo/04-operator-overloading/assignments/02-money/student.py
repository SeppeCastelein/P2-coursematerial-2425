class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise RuntimeError("Mismatched currencies!")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        else:
            raise ValueError("Cannot multiply money with non-numeric value.")

    def __str__(self):
        return f"{self.amount} {self.currency}"

# Example usage:
wallet = Money(20, "EUR") + Money(30, "EUR")
print(wallet)  # Output: Money(50, 'EUR')

wallet2 = Money(200, "EUR") - Money(30, "EUR")
print(wallet2)  # Output: Money(170, 'EUR')

wallet3 = Money(200, "EUR") * 2
print(wallet3)  # Output: Money(400, 'EUR')

wallet4 = Money(20, "EUR") * 5
print(wallet4)  # Output: Money(100, 'EUR')