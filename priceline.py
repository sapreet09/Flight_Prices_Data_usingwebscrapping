import requests
from tkinter import *
from tkinter import ttk
import pandas as pd
from payload import payload,headers
import json
main_window=Tk()
url = "https://www.priceline.com/pws/v0/pcln-graph/"

data=json.loads(payload)
Label(main_window, text='Enter your Departure Location').grid(row=0, column=0)
Label(main_window, text='Enter your Arrival Locatiob').grid(row=1, column=0)
Label(main_window, text='Enter Date of your flying').grid(row=2, column=0)
name1=Entry(main_window, width= 50 , borderwidth = 5)
name1.grid(row=0, column=1)
name2=Entry(main_window, width= 50 , borderwidth = 5)
name2.grid(row=1, column=1)
name3=Entry(main_window, width= 50 , borderwidth = 5)
name3.grid(row=2, column=1)


def fun():
  data=json.loads(payload)
  fromd=data['variables']['input']['slices'][0]['origins'][0]['location']=name1.get()
  todes=data['variables']['input']['slices'][0]['destinations'][0]['location']=name2.get()
  ddate=data['variables']['input']['slices'][0]['departDate']=name3.get()


  response = requests.request("POST", url, headers=headers, data=json.dumps(data))

  new=response.json()
  my_tree=ttk.Treeview(main_window)
  my_tree['columns']=('Code',('Name'),('Departing Air'),('DepartingTime'),('DepartingDate'),('Arriving Air'),('ArrivingTime'),('Arriving Date'),('Price'))

  my_tree.column('#0',width=0,minwidth=0)
  my_tree.column('Code',anchor=W,width=80)
  my_tree.column('Name',anchor=CENTER,width=90)
  my_tree.column('Departing Air',anchor=W,width=150)
  my_tree.column('DepartingTime',anchor=W,width=100)
  my_tree.column('DepartingDate',anchor=W,width=120)
  my_tree.column('Arriving Air',anchor=W,width=120)
  my_tree.column('ArrivingTime',anchor=W,width=100)
  my_tree.column('Arriving Date',anchor=W,width=120)
  my_tree.column('Price',anchor=W,width=100)




  my_tree.heading('#0',text='Label',anchor=W)
  my_tree.heading('Code',text='Flight Code',anchor=W)
  my_tree.heading('Name',text='Airline Name',anchor=CENTER)
  my_tree.heading('Departing Air',text='Departing Airpot',anchor=W)
  my_tree.heading('DepartingTime',text='Departing Time',anchor=W)
  my_tree.heading('DepartingDate',text='Departing Date',anchor=W)
  my_tree.heading('Arriving Air',text='Arriving Airport',anchor=W)
  my_tree.heading('ArrivingTime',text='Arriving Time',anchor=W)
  my_tree.heading('Arriving Date',text='Arriving Date',anchor=W)
  my_tree.heading('Price',text='Price of flight',anchor=W)
 
  
  N=new['data']['airSearchResp']['listings']
  
  for i in range(0,len(N)):
         
          airline_code=new['data']['airSearchResp']['listings'][i]['airlines'][0]['marketingAirline']
          airline_name=new['data']['airSearchResp']['listings'][i]['airlines'][0]['name']       
          departing_airport=new['data']['airSearchResp']['listings'][i]['slices'][0]['departing']['airport']
          departing_time=new['data']['airSearchResp']['listings'][i]['slices'][0]['departing']['time']
          departing_datetime=new['data']['airSearchResp']['listings'][i]['slices'][0]['departing']['datetime']
          arrival_airport=new['data']['airSearchResp']['listings'][i]['slices'][0]['arrival']['airport']
          arrival_time=new['data']['airSearchResp']['listings'][i]['slices'][0]['arrival']['time']
          arrival_datetime=new['data']['airSearchResp']['listings'][i]['slices'][0]['arrival']['datetime']
          airline_price=new['data']['airSearchResp']['listings'][i]['totalPriceWithDecimal']['price']
          airline_price=airline_price*78.90
          my_tree.insert('','end',values=(airline_code,airline_name,departing_airport,departing_time,departing_datetime,arrival_airport,arrival_time,arrival_datetime,airline_price))
          my_tree.grid()

Button(main_window, text= "Search",command=fun).grid(row = 3, column=1)
main_window.mainloop()