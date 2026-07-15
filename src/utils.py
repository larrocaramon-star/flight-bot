# utils.py
# Funciones auxiliares

import json

def save_history(data, filename="data/history.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
