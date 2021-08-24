from flask import Flask, request, render_template
import yfinance as yf

app = Flask(__name__)


@app.route("/quote")
def display_quote():
  symbol = request.args.get('symbol', default="AAPL")

  quote = yf.Ticker(symbol)

  return quote.info

if __name__ == "___main___":
  app.run(debug=True)