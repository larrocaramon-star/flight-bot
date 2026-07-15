# analysis.py
def analyze_prices(prices: dict) -> str:
    total = prices["TOTAL"]["price"]
    report = (
        f"✈ Informe Diario\n"
        f"Precio total: {total} USD\n"
        f"Link: {prices['TOTAL']['link']}\n"
    )
    return report
