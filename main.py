import typer
from rich.console import Console
from rich.table import Table
from core.recon import run_recon

app = typer.Typer()
console = Console()


def display_results(results):
    # Subdomains
    table = Table(title="Subdomains")
    table.add_column("Subdomain", style="cyan")

    for sub in results["subdomains"]:
        table.add_row(sub)

    console.print(table)

    # Live Hosts
    live_table = Table(title="Live Hosts")
    live_table.add_column("Host Info", style="green")

    for host in results["live_hosts"]:
        live_table.add_row(host)

    console.print(live_table)

    # Ports
    console.print("\n[bold yellow]Port Scan Results:[/bold yellow]")
    console.print(results["ports"])


@app.command()
def hunt(domain: str):
    console.print(f"\n[bold red]Starting recon on:[/bold red] {domain}\n")

    results = run_recon(domain)

    display_results(results)

    console.print("\n[bold green]Recon Complete.[/bold green]")


if __name__ == "__main__":
    app()
