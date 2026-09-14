
data = [
    {"price": 100, "volume": 1200},
    {"price": 101, "volume": 1500},
    {"price": 103, "volume": 1800},
    {"price": 102, "volume": 1300},
    {"price": 105, "volume": 2200},
    {"price": 107, "volume": 2500},
    {"price": 106, "volume": 1900},
    {"price": 104, "volume": 1700},
]

def analyse_market_return(data):


    results = {}

    for i in range(len(data)):
        if i == 0:
            results[i] = "No result"
        else:
            current_price = (data[i]['price'])
            previous_price = (data[i - 1]['price'])
        
            results[i] = ((current_price - previous_price) / previous_price)

    average_return = 0
    for returns in results.values():
        if not returns == "No result":
            average_return += returns
    average_return = average_return / (len(data) - 1)

    average_volume = 0 
    for i in range(len(data)):
        average_volume += data[i]["volume"]
    average_volume = average_volume / len(data)


    percentage_of_positive = 0
    for result in results.values():
        if result > 0:
            percentage_of_positive += 1
    percentage_of_positive = (percentage_of_positive / (len(results) - 1)) * 100

    
    if percentage_of_positive >= 60:
        regime = "Bullish"
    elif percentage_of_positive <= 40:
        regime = "Bearish"
    else:
        regime = "Neutral"

    return  {
        "average return": average_return,
        "average volume": average_volume,
        "percentage of positive": percentage_of_positive,
        "regime": regime

    }
