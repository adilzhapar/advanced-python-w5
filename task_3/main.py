import typer
import requests

from rich import print
from typing import Any, List

from typing_extensions import Annotated

from decorators import retry
from utils import get_data, format_response

app = typer.Typer(
    pretty_exceptions_enable=False,
    pretty_exceptions_show_locals=False
)


@app.command()
@retry(requests.exceptions.HTTPError, attemtps=3, delay=8)
def get_obj_by_bin(
        biniin: Annotated[str, typer.Argument(
            help="BIN or IIN of the company",
        )],
        field_names: Annotated[List[str], typer.Argument(
            help="List of field names to return",
        )] = None
) -> Any:
    """
    Get information about company by BIN or IIN
    """
    obj = get_data(biniin)
    formatted_object = format_response(obj, field_names)
    print(formatted_object)


if __name__ == "__main__":
    app()
