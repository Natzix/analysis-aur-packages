import subprocess

import typer

from analysis_aur.commands.local_packet_analysis import load_list

app = typer.Typer()


def uninstall():
    packages = load_list()
    if not packages:
        print("There are no infected packages")
        return
    subprocess.run(["yay", "-Rns"] + packages)
