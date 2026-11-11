"""Cliente con credenciales externas y tiempo de espera limitado."""

import os
from urllib.parse import urlsplit

import requests


def fetch_data(url):
    """Consulta un endpoint HTTPS con una credencial del entorno."""
    parsed_url = urlsplit(url)
    if parsed_url.scheme != "https" or not parsed_url.hostname:
        raise ValueError("La URL debe usar HTTPS y contener un servidor valido")
    api_token = os.environ["API_TOKEN"]
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {api_token}"},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
