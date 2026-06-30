# analysis-aur

CLI escrita en Python (Typer) para detectar y eliminar paquetes AUR comprometidos por la campaña de malware **"Atomic Arch"** (junio 2026).

Compara los paquetes AUR instalados en tu sistema contra una lista de paquetes conocidos como infectados, usando intersección de sets sobre la salida de `pacman -Qm`.

## Instalación

```bash
git clone https://github.com/Natzix/analysis-aur.git
cd analysis-aur
# (instrucciones de entorno virtual / pip aquí según tu setup final)
```

## Uso

La CLI sigue un diseño plano estilo Unix, sin subcomandos anidados:

```bash
# Ver los paquetes "foráneos" (AUR) instalados, sin analizar
analysis-aur scan

# Analizar esos paquetes contra la lista de malware conocido
analysis-aur scan --analyze

# Desinstalar los paquetes detectados como infectados
analysis-aur uninstall
```

### `scan`

- Sin `--analyze`: lista los paquetes instalados fuera de los repositorios oficiales (`pacman -Qm`).
- Con `--analyze`: intersecta esos paquetes con la lista de malware conocido (`infected_packets.txt`, ~1935 entradas) y, si encuentra coincidencias, las guarda en `~/.cache/analysis-aur/resultados.json`.

### `uninstall`

Lee el cache generado por `scan --analyze` y ejecuta `yay -Rns` sobre los paquetes detectados como infectados.

⚠️ **Importante**: este comando ejecuta una desinstalación real. Revisa siempre el contenido de `resultados.json` antes de correrlo.

## Estructura del proyecto

```
src/analysis-aur/
└── command/
    ├── local_packet_analysis.py        # comando `scan`, cache, lógica de detección
    └── uninstall_infected_packages.py  # comando `uninstall`
```

## Autor

--- RENATO ROBINSON ---
