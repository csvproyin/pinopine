from storage import load_data, save_data

watchlist = load_data("watchlist.json")


def save_watchlist():

    save_data("watchlist.json", watchlist)