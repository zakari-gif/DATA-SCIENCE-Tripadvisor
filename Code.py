#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:01:34 2021

@author: abdoumahamadouzakariyaou
"""
from unidecode import unidecode


import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
import csv

def open_graven_channel():
    webbrowser.open_new("https://www.tripadvisor.fr/")
    

def parcours(url,compteur=[0],liste=[]):
    reponse=requests.get(url)
    if reponse.ok:
        soup=BeautifulSoup(reponse.text)
        reviews=soup.find_all('div',{'class':'Dq9MAugU T870kzTX LnVzGwUB'})
        #for rv in reviews:
            #b=rv.find_all('div',{'class':'oETBfkHU'})
        

        for rv in reviews:
            profil=rv.find('div',{'class':"_310S4sqz"}).find('div',{'class':"_2uYWQXeO"}).find('div',{'class':"_2fxQ4TOx"})
            date=profil.find().text
            profil=profil.find('a',{'class':"ui_header_link _1r_My98y"}).text
            commentaire=rv.find('q',{'class':'IRsGHoPm'}).find('span').text
            lieuderesidence=rv.find('div',{'class':'_1EpRX7o3'}).text
            NombreDavis=rv.find('div',{'class':'_1EpRX7o3'}).find('span',{'class':'_1fk70GUn'}).text
            #print(NombreDavis)
            NombreVoteutile=rv.find('div',{'class':'_1EpRX7o3'}).find_next('span',{'class':'_3fPsSAYi'}).find_next().find('span',{'class':'_1fk70GUn'}).text
            #print(NombreVoteutile)
            linkprofil=profil+str([lieuderesidence])+str([NombreDavis])+str([NombreVoteutile])+str([date])+str([commentaire])
            compteur[0]=compteur[0]+1
            liste.append('' + linkprofil)
               
        liensuivant=soup.find('div',{'class':'ui_pagination is-centered'})
        liensuivant=liensuivant.find('a',{'class':'ui_button nav next primary'})
        try:
            liensuivant=liensuivant['href']
        except TypeError or ConnectionError or gaierror:
            print("FinParcours")
            print(compteur)
            return liste
        linkfollowing=str('https://www.tripadvisor.fr')+str(liensuivant)
        print(linkfollowing)
        return parcours(linkfollowing)
   




def concatenation(liste1): 
    Liste=[]
    l=[]
    for review in liste1:
        l=review.split('[')
        Liste.append(l[:])
    print(Liste)
    return Liste

def generate_lien():
    lien=lien_entry.get()
    a=parcours(lien,compteur=[0],liste=[])
    test2=concatenation(a)
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nom","Lieu de residence","Nombre Davis","Nombre Vote de Utile","Date", "commentaire"])
        for k in range(len(test2)) : 
            writer.writerow([(test2[k][0].capitalize()),
                             (test2[k][1].split("'"))[1].split(",")[0],
                             (test2[k][2].split("'")[1]),
                             (test2[k][1].split('contributions')[1]).split(" ")[0],
                             (test2[k][4].split('('))[1].split(')')[0],
                             (test2[k][5]).split(']')[0]])
#(test2[k][1].split("'"))[1].split(",")[1].split('contributions')[1].split(" ")[0]
#(test2[k][4].split('('))[1].split(')')[0],(test2[k][2]).split("'")[1]
#.split('contributions')[0]
Window =Tk()
Window.iconbitmap('logo.ico')
Window['bg'] = '#41B77F'
Window.title("Trip Advisor Data Extractor & Analysis")
Window.geometry("500x300")
Window.maxsize(800, 500)
frame=Frame(Window,bd=1,relief=SUNKEN)
label_title=Label(frame,text="WELCOME TO TRIP DATA",font=("Courrier",20))
label_title.pack()

label_subtitle=Label(frame,text="This tool Generates You a Data File in csv Format",font=("Courrier",20),bg="#41B77F",fg="white")
label_subtitle.pack()
frame.pack(expand=YES)

button=Button(frame,text="Access the site",font=("Courrier",15),fg='#41B77F',bg="#41B77F",command=open_graven_channel)
button.pack()
label_subtitle1=Label(frame,text="Enter the site link",font=("Courrier",10),bg="#41B77F",fg="white")
label_subtitle1.pack()
frame.pack(expand=YES)
lien_entry=Entry(frame,font=("Courrier",15),fg='#4878E6',bg="white")
lien_entry.pack()
button1=Button(frame,text="Generate",font=("Courrier",20),fg='#41B77F',bg="#41B77F",command=generate_lien)
button1.pack()
Window.mainloop()



#https://www.tripadvisor.fr/Attraction_Review-g45963-d110193-Reviews-or850-The_Neon_Museum-Las_Vegas_Nevada.html#REVIEWS

