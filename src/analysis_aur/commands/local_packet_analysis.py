import json
import subprocess
from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer()

CACHE = Path.home() / ".cache" / "analysis-aur" / "resultados.json"


def scan(
    analyze: Annotated[
        bool,
        typer.Option(
            help="Check to see if you have any AUR packages containing malware"
        ),
    ] = False,
):
    isArchLinux()
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


def get_list_malware():  # obtiene la lista de los paquetes infectados
    aur_malwares = open("infected_packets.txt")
    return set(aur_malwares.read().strip().splitlines())


def save_virus_packages(packages: list):  # persiste los nombres de paquetes en cache
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(packages))


def load_list():  # carga la lista que se persistio en cache
    if not CACHE.exists():
        print("no existe nada")
        return []
    return json.loads(CACHE.read_text())


def isArchLinux():  # comprueba si el S.O. es Arch Linux
    process = subprocess.run(["lsb_release", "-a"], capture_output=True, text=True)

    if "Arch Linux" not in process.stdout:
        raise typer.Exit(code=1)
