'''
ExchangeRatesAI.py
FINE 3300 Assignment 1
Exchange Rate Conversion
'''

class ExchangeRates:

    def __init__(self, filename):

        # Open the exchange rate file
        file = open(filename, "r")

        # Find the USD/CAD column
        header = file.readline().strip().split(",")
        position = header.index("FXAUSDCAD")

        # Read the last row of the file
        last_line = ""

        for line in file:
            if line.strip() != "":
                last_line = line

        file.close()

        # Get the latest exchange rate
        values = last_line.strip().split(",")
        self.__rate = float(values[position])

    def convert(self, amount, from_currency, to_currency):

        # Convert USD to CAD
        if from_currency == "USD" and to_currency == "CAD":
            result = amount * self.__rate

        # Convert CAD to USD
        elif from_currency == "CAD" and to_currency == "USD":
            result = amount / self.__rate

        # Same currency
        else:
            result = amount

        return result


if __name__ == "__main__":

    # Create an ExchangeRates object
    rates = ExchangeRates("BankOfCanadaExchangeRates.2026.csv")

    # Ask the user for the amount and currencies
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency (USD or CAD): ").upper()
    to_currency = input("Enter to currency (USD or CAD): ").upper()

    # Convert the amount
    result = rates.convert(amount, from_currency, to_currency)

    # Display the result
    print("${:,.2f} {} = ${:,.2f} {}".format(
        amount, from_currency, result, to_currency))