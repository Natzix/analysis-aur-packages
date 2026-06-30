# src/analysis-aur/commands/local_packet_analysis.py

import json
import subprocess
from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer()

CACHE = Path.home() / ".cache" / "analysis-aur" / "resultados.json"


@app.command()
def scan(
    analyze: Annotated[
        bool,
        typer.Option(
            help="Check to see if you have any AUR packages containing malware"
        ),
    ] = False,
):
    process = subprocess.run(["pacman", "-Qm"], capture_output=True, text=True)
    packages_aur = set(process.stdout.splitlines())

    if analyze:
        malware_detected = packages_aur & get_list_malware()  # intercepción
        if malware_detected:
            print(f"*** INFECTED PACKETS : {len(malware_detected)} ***")
            save_virus_packages(list(malware_detected))
        else:
            print("*** You don't have any infected packages ***")

    else:
        print("=== FOREIGN PACKAGES YOU HAVE INSTALLED ===\n")
        print(process.stdout)


def get_list_malware():
    aur_malwares = open("infected_packets.txt")
    return set(aur_malwares.read().strip().splitlines())


def save_virus_packages(packages: list):
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(packages))


def load_list():
    if not CACHE.exists():
        print("no existe nada")
        return []
    return json.loads(CACHE.read_text())
