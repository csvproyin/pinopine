from storage import load_data, save_data

alerts = load_data("alerts.json")


def save_alerts():

    save_data("alerts.json", alerts)