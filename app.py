"""Cliente vulnerable de laboratorio. La credencial es ficticia."""

import requests


def fetch_data(url):
    # Credencial FICTICIA para demostrar el hallazgo B105 de Bandit.
    api_token = "12345-SUPER-SECRET-KEY"
    response = requests.get(f"{url}?key={api_token}")
    return response.json()
