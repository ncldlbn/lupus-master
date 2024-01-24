#!/bin/bash

# Ottieni il percorso completo del file di script
SCRIPT_PATH="$(readlink -f "$0")"

# Ottieni il percorso della cartella corrente
CURRENT_FOLDER="$(dirname "$SCRIPT_PATH")"

# Imposta il comando che desideri eseguire
COMMAND_TO_RUN="python3 lupus-master.py"

# Vai alla cartella corrente
cd "$CURRENT_FOLDER"

# Apri un terminale nella cartella corrente e avvia il comando
gnome-terminal --working-directory="$CURRENT_FOLDER" -- bash -c "$COMMAND_TO_RUN; exec bash"
