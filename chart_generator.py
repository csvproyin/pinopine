import yfinance as yf
import mplfinance as mpf

def generate_chart(stock):

    data = yf.download(stock + ".NS", period="1mo", interval="1d")

    if data.empty:
        return None

    filename = f"{stock}_candles.png"

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