# src/analysis-aur/main.py
import typer
from commands.local_packet_analysis import scan
from commands.uninstall_infected_packages import uninstall

app = typer.Typer()

app.command()(scan)
app.command()(uninstall)

if __name__ == "__main__":
    app()
