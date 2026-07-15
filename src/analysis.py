def analyze_prices(prices: dict) -> str:
    total = (
        prices["MVD-NYC"]["price"] +
        prices["NYC-MIA"]["price"] +
        prices["MIA-MVD"]["price"]
    )
    report = (
        f"✈ Informe Diario\n"
        f"Montevideo → Nueva York: {prices['MVD-NYC']['price']} USD\n{prices['MVD-NYC']['link']}\n\n"
        f"Nueva York → Miami: {prices['NYC-MIA']['price']} USD\n{prices['NYC-MIA']['link']}\n\n"
        f"Miami → Montevideo: {prices['MIA-MVD']['price']} USD\n{prices['MIA-MVD']['link']}\n\n"
        f"💰 Total: {total} USD\n"
    )
    return report
