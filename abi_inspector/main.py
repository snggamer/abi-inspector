import json
import sys
import click
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli():
    """ABI Inspector CLI"""
    pass

@cli.command()
@click.argument("abi_file", type=click.Path(exists=True))
def validate(abi_file):
    """Validate ABI JSON structure and list functions/events"""
    try:
        data = json.load(open(abi_file))
        funcs = [x for x in data if x.get("type") == "function"]
        events = [x for x in data if x.get("type") == "event"]

        table = Table(title="ABI Summary")
        table.add_column("Item")
        table.add_column("Count")
        table.add_row("functions", str(len(funcs)))
        table.add_row("events", str(len(events)))
        console.print(table)
        console.print_json(data=data)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

@cli.command()
@click.argument("abi_file", type=click.Path(exists=True))
def stats(abi_file):
    """Basic stats: selector duplicates, non-payable/payable count"""
    data = json.load(open(abi_file))
    selectors = {}
    for x in data:
        if x.get("type") == "function":
            sig = x["name"] + "(" + ",".join([i["type"] for i in x.get("inputs", [])]) + ")"
            selectors[sig] = selectors.get(sig, 0) + 1
    dups = {k: v for k, v in selectors.items() if v > 1}
    console.print({"duplicates": dups, "total_functions": len(selectors)})

if __name__ == "__main__":
    cli()
