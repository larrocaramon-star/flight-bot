def analyze_prices(prices: dict) -> str:
    total = (
        prices["MVD-JFK"]["price"] +
        prices["JFK-MIA"]["price"] +
        prices["MIA-MVD"]["price"]
    )
    report = (
        f"✈ Informe Diario\n"
        f"Montevideo → Nueva York: {prices['MVD-JFK']['price']} USD\n{prices['MVD-JFK']['link']}\n\n"
        f"Nueva York → Miami: {prices['JFK-MIA']['price']} USD\n{prices['JFK-MIA']['link']}\n\n"
        f"Miami → Montevideo: {prices['MIA-MVD']['price']} USD\n{prices['MIA-MVD']['link']}\n\n"
        f"💰 Total: {total} USD\n"
    )
    return report
