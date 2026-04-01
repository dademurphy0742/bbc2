import typer
from rich.console import Console
from rich.table import Table

from core.programs import fetch_programs, register_helper
from core.workspace import create_workspace
from core.recon import run_recon
from core.analyzer import prioritize_targets, suggest_attacks
from core.fuzz import run_directory_fuzz
from core.payloads import get_all_payloads

app = typer.Typer()
console = Console()

@app.command()
def start():
    console.print("\n[bold red]Bug Bounty Command Center[/bold red]\n")

    programs = fetch_programs()
    if not programs:
        console.print("[!] Failed to fetch programs")
        return

    table = Table(title="Programs")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("URL")

    for i, p in enumerate(programs):
        table.add_row(str(i), p["name"], p["url"])

    console.print(table)

    idx = int(input("\nSelect program: "))
    program = programs[idx]

    register_helper(program["url"])
    ws = create_workspace(program["name"])

    domain = input("\nTarget domain: ")
    results = run_recon(domain)

    ranked = prioritize_targets(results["live_hosts"])

    table2 = Table(title="Top Targets")
    table2.add_column("Host")
    table2.add_column("Score")

    for h, s in ranked[:10]:
        table2.add_row(h, str(s))

    console.print(table2)

    if ranked:
        target = ranked[0][0].split(" ")[0]
        console.print(f"\n[green]Target:[/green] {target}")

        console.print("\n[yellow]Attacks:[/yellow]")
        for a in suggest_attacks(ranked[0][0]):
            console.print(f"→ {a}")

        fuzz = run_directory_fuzz(target)
        with open(ws / "fuzz.txt", "w") as f:
            f.write(fuzz)

        payloads = get_all_payloads()
        with open(ws / "payloads.txt", "w") as f:
            for k, v in payloads.items():
                f.write(f"{k}:\n")
                for p in v:
                    f.write(p + "\n")

    console.print("\n[bold green]Done[/bold green]")

if __name__ == "__main__":
    app()
