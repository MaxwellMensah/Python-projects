# Currency Converter.
currency = ["GHC", "USD", "PDS", "EUR", "YEN", "CAD", "RND", "RUP"]

print(
    "----------------------------------- \n",
    "Welcome to Converter Exchange Rate!\n",
    " GHC --- Ghana Cedis \n",
    " USD --- US Dollar \n",
    " PDS --- Pound Sterling \n",
    " EUR --- Euro \n",
    " YEN --- JPY Yen \n",
    " CAD --- Canadian Dollar \n",
    " RND --- S.A Rand \n",
    " RUP --- Indian Rupee \n",
    "-----------------------------------"
)

Base = input("Enter your currency |>> ").upper()
Exchange = input("Enter the exchange currency |>> ").upper()

if Base not in currency:
    print("Follow the instructions and try again... ")
    exit()
elif Exchange not in currency:
    print("Follow the instructions and try again... ")
    exit()

cash = float(input("Enter your base amount: "))
if Base == "GHC":              # converting from Ghana Cedis to other exchange.
    if Exchange == "USD":
        rate = cash * 0.17
    elif Exchange == "PDS":
        rate = cash * 0.13
    elif Exchange == "EUR":
        rate = cash * 0.14
    elif Exchange == "YEN":
        rate = cash * 17.74
    elif Exchange == "CAD":
        rate = cash * 0.22
    elif Exchange == "RND":
        rate = cash * 2.61
    elif Exchange == "RUP":
        rate = cash * 12.52
    else:
        rate = cash

if Base == "USD":                  # USDollar$ to other exchange.
    if Exchange == "GHC":
        rate = cash * 5.86
    elif Exchange == "PDS":
        rate = cash * 0.74
    elif Exchange == "EUR":
        rate = cash * 0.81678
    elif Exchange == "YEN":
        rate = cash * 103.922
    elif Exchange == "CAD":
        rate = cash * 1.27
    elif Exchange == "RND":
        rate = cash * 15.30
    elif Exchange == "RUP":
        rate = cash * 73.38
    else:
        rate = cash

if Base == "PDS":                   # Pound Sterling to other exchange.
    if Exchange == "GHC":
        rate = cash * 7.95
    elif Exchange == "USD":
        rate = cash * 1.36
    elif Exchange == "EUR":
        rate = cash * 1.11
    elif Exchange == "YEN":
        rate = cash * 141.01
    elif Exchange == "CAD":
        rate = cash * 1.72
    elif Exchange == "RND":
        rate = cash * 20.76
    elif Exchange == "RUP":
        rate = cash * 99.56
    else:
        rate = cash

if Base == "EUR":                  # Euro to other exchange.
    if Exchange == "GHC":
        rate = cash * 7.16
    elif Exchange == "PDS":
        rate = cash * 0.90
    elif Exchange == "USD":
        rate = cash * 1.22
    elif Exchange == "YEN":
        rate = cash * 127.05
    elif Exchange == "CAD":
        rate = cash * 1.55
    elif Exchange == "RND":
        rate = cash * 18.70
    elif Exchange == "RUP":
        rate = cash * 89.71
    else:
        rate = cash

if Base == "YEN":                  # Japanese YEN to other exchange.
    if Exchange == "GHC":
        rate = cash * 0.056
    elif Exchange == "USD":
        rate = cash * 0.0096
    elif Exchange == "EUR":
        rate = cash * 0.0079
    elif Exchange == "PDS":
        rate = cash * 0.0071
    elif Exchange == "CAD":
        rate = cash * 0.012
    elif Exchange == "RND":
        rate = cash * 0.15
    elif Exchange == "RUP":
        rate = cash * 0.71
    else:
        rate = cash

if Base == "CAD":                  # Canadian Dollar to other exchange.
    if Exchange == "GHC":
        rate = cash * 4.62
    elif Exchange == "USD":
        rate = cash * 0.79
    elif Exchange == "PDS":
        rate = cash * 0.58
    elif Exchange == "EUR":
        rate = cash * 0.64
    elif Exchange == "YEN":
        rate = cash * 81.92
    elif Exchange == "RND":
        rate = cash * 12.06
    elif Exchange == "RUP":
        rate = cash * 58.38
    else:
        rate = cash

if Base == "RND":                  # South African RAND to other exchange.
    if Exchange == "GHC":
        rate = cash * 0.38
    elif Exchange == "USD":
        rate = cash * 0.065
    elif Exchange == "PDS":
        rate = cash * 0.048
    elif Exchange == "EUR":
        rate = cash * 0.053
    elif Exchange == "YEN":
        rate = cash * 6.80
    elif Exchange == "CAD":
        rate = cash * 0.083
    elif Exchange == "RUP":
        rate = cash * 4.80
    else:
        rate = cash

if Base == "RUP":                  # Indian RUPEES to other exchange.
    if Exchange == "GHC":
        rate = cash * 0.080
    elif Exchange == "USD":
        rate = cash * 0.014
    elif Exchange == "PDS":
        rate = cash * 0.010
    elif Exchange == "EUR":
        rate = cash * 0.011
    elif Exchange == "YEN":
        rate = cash * 1.42
    elif Exchange == "CAD":
        rate = cash * 0.017
    elif Exchange == "RND":
        rate = cash * 0.21
    else:
        rate = cash
print(f'Exchange amount is {rate}. Thank you for your purchase!')


# source of rate: Google [https://www.google.com/intl/en/googlefinance/disclaimer/], as of January 9, 2021.