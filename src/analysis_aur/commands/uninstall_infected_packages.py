import subprocess

import typer
from commands.local_packet_analysis import load_list

app = typer.Typer()


@app.command()
def uninstall():
    packages = load_list()
    if not packages:
        print("There are no infected packages")
        return
    subprocess.run(["yay", "-Rns"] + packages)
