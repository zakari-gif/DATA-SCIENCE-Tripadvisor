#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:10:54 2021

@author: abdoumahamadouzakariyaou
"""
import requests
from bs4 import BeautifulSoup
def parcours(url='https://www.tripadvisor.fr/Attraction_Review-g45963-d110193-Reviews-or865-The_Neon_Museum-Las_Vegas_Nevada.html#REVIEWS',compteur=[0],liste=[]):
    reponse=requests.get(url)
    if reponse.ok:
        soup=BeautifulSoup(reponse.text)
        reviews=soup.find_all('div',{'class':'Dq9MAugU T870kzTX LnVzGwUB'})
        for rv in reviews:
            b=rv.find_all('div',{'class':'_310S4sqz'})
            for bx in b:
                profil=bx.find('a')
                commentaire=bx.find('q',{'class':'IRsGHoPm'}).find('span')
                linkprofil=profil['href']+'='+str([commentaire])
                compteur[0]=compteur[0]+1
                liste.append('' + linkprofil)
        liensuivant=soup.find('div',{'class':'ui_pagination is-centered'})
        liensuivant=liensuivant.find('a',{'class':'ui_button nav next primary'})
        try:
            liensuivant=liensuivant['href']
        except TypeError:
            print("FinParcours")
            print(compteur)
            print(liste)
            return 0
        linkfollowing=str('https://www.tripadvisor.fr')+liensuivant
        print(linkfollowing)
        traitementliensuivant=parcours(linkfollowing)
test=parcours()
