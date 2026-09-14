
def analyse_multi_trades(trades, asset):

    assets = set()
    results = {}

    for trade in trades:
        
        if not trade["asset"] in assets:
            results[trade['asset']] = {"return_volume": 0, "total_volume": 0}
        assets.add(trade["asset"])
        results[trade['asset']]["return_volume"] += trade['return'] * trade["volume"]
        results[trade['asset']]["total_volume"] += trade['volume']

    output = {}
    for asset in results:
        
        weighted_average = (results[asset]["return_volume"] / results[asset]["total_volume"])
        output[asset] = weighted_average

    best_asset = None 
    best_return = None
    for result in output:
        if best_return is None or output[result] > best_return:
            best_return = output[result]
            best_asset = result

    final_output = []
    final_output.append("The best asset is:")
    final_output.append(best_asset)
    final_output.append("With a total return of:")
    final_output.append(best_return)

    return output, final_output
