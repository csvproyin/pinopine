from storage import load_data, save_data

portfolio = load_data("portfolio.json")


def save_portfolio():

    save_data("portfolio.json", portfolio)