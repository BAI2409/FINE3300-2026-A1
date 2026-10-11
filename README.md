# FINE3300-2026-A1
FINE3300 Assignment 1 - Exchange Rates

This program uses Bank of Canada exchange rate data to convert between USD and CAD.

The program reads the exchange rate data from the CSV file and uses the latest USD/CAD exchange rate to perform the conversion.

### Files

- `ExchangeRates.py` - My Part 1 Python program
- `ExchangeRatesAI.py` - AI-generated version for Part 2
- `BankOfCanadaExchangeRates.2026.csv` - Bank of Canada exchange rate data

## How to Run

Run `ExchangeRates.py` using Python.

The program asks the user to enter:

1. The amount
2. The currency to convert from
3. The currency to convert to

The supported currencies are USD and CAD.

## Example

USD to CAD:

$100,000.00 USD = $139,780.00 CAD

CAD to USD:

$100,000.00 CAD = $71,540.99 USD

## Part 2: Vibe Coding

For Part 2, I used ChatGPT.

### Comparison


Both programs complete the same task, but they use different methods to read the exchange rate data.

In Part 1, the program uses basic Python commands such as open(), for loops, and split() to read the CSV file. This approach follows the basic programming concepts I learned in class. It also helps me understand how the program reads each line and finds the exchange rate.

In Part 2, the AI-generated program uses pandas to read the CSV file. This makes the code shorter. However, initially pandas was not installed and installing pandas was a hassle, also the AI version initially selected the wrong row, which resulted in an incorrect conversion. I had to check the output and correct the code.

I do believe that AI can make programming faster and provide useful suggestions, but it is still important to understand the code and test the results. The assignment helped me practise using Python classes and methods while also learning how to identify and correct programming errors.


## GitHub Repository
https://github.com/BAI2409/FINE3300-2026-A1.git


