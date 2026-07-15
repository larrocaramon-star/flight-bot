# analysis.py
# Inteligencia y variaciones de precios

def analyze_prices(prices: dict) -> str:
    total = sum(prices.values())
    report = (
        f"✈ Informe Diario\n"
        f"Montevideo → Nueva York: {prices['MVD-JFK']} USD\n"
        f"Nueva York → Miami: {prices['JFK-MIA']} USD\n"
        f"Miami → Montevideo: {prices['MIA-MVD']} USD\n"
        f"💰 Total: {total} USD\n"
    )
    return report
