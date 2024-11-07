import re

import requests

PYPAS_CLI_PYPI_URL = 'https://pypi.org/project/pypas-cli/'
PYPAS_CLI_VERSION_PLACEHOLDER = '{{pypas_cli_version}}'


def on_page_markdown(markdown, **kwargs):
    def get_pypas_cli_version() -> str:
        NOT_AVAILABLE = 'NA'
        try:
            response = requests.get(PYPAS_CLI_PYPI_URL)
        except Exception:
            return NOT_AVAILABLE
        if m := re.search(r'pypas-cli (\d+\.\d+\.\d+)', response.content.decode()):
            return m.group(1)
        return NOT_AVAILABLE

    return markdown.replace(PYPAS_CLI_VERSION_PLACEHOLDER, get_pypas_cli_version())
