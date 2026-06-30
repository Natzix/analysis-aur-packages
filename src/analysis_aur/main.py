import typer

from analysis_aur.commands.local_packet_analysis import scan
from analysis_aur.commands.uninstall_infected_packages import uninstall

app = typer.Typer()

app.command()(scan)
app.command()(uninstall)

if __name__ == "__main__":
    app()
