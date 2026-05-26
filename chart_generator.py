import yfinance as yf
import mplfinance as mpf
import pandas as pd


def generate_chart(stock):

    try:

        data = yf.download(
            stock + ".NS",
            period="1mo",
            interval="1d",
            auto_adjust=False
        )

        if data.empty:
            return None

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.droplevel(1)

        filename = f"{stock}_chart.png"

        mpf.plot(
            data,
            type="candle",
            mav=(5, 10),
            volume=True,
            style="yahoo",
            title=f"{stock.upper()} Stock Chart",
            savefig=filename
        )

        return filename

    except Exception as e:

        print("CHART ERROR:", e)

        return None