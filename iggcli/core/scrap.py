from typer import Exit
from rich import print

from bs4 import BeautifulSoup
from requests import Response, get as requests_get

from iggcli.values.web import BASE_URL

def parse(router: list[str] = [], params: dict = {}) -> BeautifulSoup:
    res: Response = requests_get(BASE_URL + "/".join(router), params=params)

    if res.status_code != 200:
        print("[red]> Offline service[/]")

        raise Exit(code=1)

    return BeautifulSoup(res.text, "html.parser")