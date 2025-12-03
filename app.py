import requests
import json

amq2amq.routeId = qDOSSOrder_fromNOA_toB2B_B2B

amq2amq.to-queue = weblogic.jms.qDOSSOrder_fromNOA_toB2B


questart = test
queend = test2
# Annahme: Raw-URL der config.json auf GitHub
CONFIG_URL = "https://raw.githubusercontent.com/DogukanErsungur/config-repo/main/config.json"

try:
    response = requests.get(CONFIG_URL)
    response.raise_for_status()  # Wirft eine Exception für HTTP-Fehler
    config = json.loads(response.text)

    api_url = config.get("apiUrl")
    theme = config.get("theme")
    max_results = config.get("maxResults")

    print(f"API URL: {api_url}")
    print(f"Theme: {theme}")
    print(f"Max Results: {max_results}")

except requests.exceptions.RequestException as e:
    print(f"Fehler beim Herunterladen der Konfiguration: {e}")
except json.JSONDecodeError as e:
    print(f"Fehler beim Parsen der Konfiguration: {e}")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
