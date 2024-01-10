#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
import os
from moduli.ruoli import Villico, Lupo, Cavaliere, Veggente, Giustiziere, Insinuo, Illusionista

class Villaggio:
    def __init__(self):
        self.abitanti = []

def read_setup(setup_file):
    ### Inserire controllo N ruoli == N Giocatori!!
    with open(setup_file, 'r') as file:
        setup = yaml.safe_load(file)
    if 'Giocatori' in setup:
        lista_giocatori = setup['Giocatori']
        giocatori = {i + 1: f"{nome}" for i, nome in enumerate(lista_giocatori)}
    else:
        print('Inserisci i nomi dei giocatori nel file di setup')
    if 'Ruoli' in setup:
        lista_ruoli = setup['Ruoli']
    else:
        print('Inserisci i ruoli nel file di setup')  
        
    return lista_ruoli, giocatori
    

def inputID_init(ruolo, giocatori):
    while True:
        # Chiedi all'utente di inserire l'ID del giocatore da assegnare al ruolo
        player_id = input(f"{ruolo}: ")
        if player_id:
            player_id = int(player_id)
            # Verifica se il numero inserito è presente nella lista
            if player_id in giocatori.keys():
                return player_id
            else:
                print(f"ID non valido [{min(giocatori.keys())}-{max(giocatori.keys())}]")
        else:
            print("Inserisci l'ID di un giocatore")

def assegnazione_ruoli(giocatori, lista_ruoli):
    villaggio = Villaggio()
    ruoli = {}
    # Assegnazione ruoli
    for ruolo in lista_ruoli:
        if ruolo == 'Villico':
            pass
        else:
            while True:
                ID = inputID_init(ruolo, giocatori)
                if ID in ruoli.keys():
                    print("ID già assegnato")
                else:
                    ruoli[ID] = ruolo
                    break
    # assegnazione villici
    for ID in giocatori.keys():
        if ID not in ruoli.keys():
            ruoli[ID] = 'Villico'
    # assegnazione abitanti al villaggio
    for ID in giocatori.keys():
        if ruoli[ID] == 'Lupo':
            nuovo_ruolo = Lupo(ID, giocatori[ID])   
        if ruoli[ID] == 'Villico':
            nuovo_ruolo = Villico(ID, giocatori[ID])
        if ruoli[ID] == 'Cavaliere':
            nuovo_ruolo = Cavaliere(ID, giocatori[ID])
        if ruoli[ID] == 'Veggente':
            nuovo_ruolo = Veggente(ID, giocatori[ID])
        if ruoli[ID] == 'Giustiziere':
            nuovo_ruolo = Giustiziere(ID, giocatori[ID])
        if ruoli[ID] == 'Insinuo':
            nuovo_ruolo = Insinuo(ID, giocatori[ID])
        if ruoli[ID] == 'Illusionista':
            nuovo_ruolo = Illusionista(ID, giocatori[ID])
        villaggio.abitanti.append(nuovo_ruolo)
    return villaggio

def recap(villaggio):
    for abitante in villaggio.abitanti:
        print(f"{abitante.ID:<2} {abitante.nome:<10} {abitante.ruolo:<12} {abitante.status:<5}")

def condizioni_vittoria(villaggio):
    lupi_vivi = [lupi.status for lupi in villaggio.abitanti if lupi.ruolo == 'Lupo' and lupi.status == 'Vivo']
    solitari_vivi = [solitari.status for solitari in villaggio.abitanti if solitari.fazione == 'Solitario' and solitari.status == 'Vivo']
    altri_giocatori_vivi = [g.status for g in villaggio.abitanti if g.ruolo != 'Lupo' and g.fazione != 'Solitario' and g.status == 'Vivo']
    # condizione vittoria dei villici:
    #   sono morti tutti i lupi e tutti i personaggi solitari
    if not lupi_vivi and not solitari_vivi:
        os.system('clear')
        print('I villici vincono la partita!\n')
        return True
    # condizione vittoria dei lupi:
    #   sono morti tutti i personaggi solitari e il numero di lupi == numero altri giocatori
    elif not solitari_vivi and (len(lupi_vivi) == len(altri_giocatori_vivi)):
        os.system('clear')
        print('I lupi vincono la partita!\n')
        return True
    # condizione vittoria dei personaggi solitari:
    #   ogni personaggio solitario ha delle proprie condizioni di vittoria
    elif solitari_vivi:
        for p in solitari_vivi:
            if p.vittoria:
                print(f'Il {p.ruolo} vince la partita!\n')
                return True
    else:
        return False
