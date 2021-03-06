# -*- coding: utf-8 -*-
"""Question1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DhADkqPrrGhYGKEPGDy4bsknIvA7lVwV

Question 1
"""

from datetime import datetime,timedelta


# A

class Customer:
    def __init__(self, name, contact):
        self._name = name
        self._contact = contact

    def get_name(self):
        return self._name

    def get_contact(self):
        return self._contact

    def set_contact(self,newContact):
        self._contact = newContact

    def __str__(self):
        return self._name +" "+ self._contact

# B

class Staycation:
    def __init__(self,hotelName, nights, cost):
        self._hotelName         = hotelName
        self._nights            = nights
        self._cost              = cost
        self._voucherAllowed    = True

    def get_hotelName(self):
        return self._hotelName

    def get_nights(self):
        return self._nights

    def get_cost(self):
        return self._cost

    def get_voucherAllowed(self):
        return self._voucherAllowed

    def set_cost(self,newCost):
        self._cost = newCost

    def set_voucherAllowed(self,allowed):
        self._voucherAllowed = bool(allowed)

    def costPerNight(self):
        return self._cost/self._nights

    def isCheaper(self,other):
        if (self._cost/self._nights < other._cost/other._nights):
            return True
        else: return False
            
    def __str__(self):

        if self._voucherAllowed == True: allowed = "Yes"
        else: allowed = "No"

        return self._hotelName +" Nights: "+ str(self._nights) +" Current Price: $"+ str(self._cost) +" or $"+ str(self.costPerNight()) +" per night Voucher allowed: "+ allowed


# C

class Booking:
    def __init__(self,customer,staycation,checkInDate):
        self._customer      = customer   
        self._staycation    = staycation 
        self._checkInDate   = checkInDate
        self._cost          = staycation.get_cost()   

    def  get_customer(self):
        return self._customer
        
    def get_stayation(self):
        return self._staycation
    
    def get_hotelName(self):
        return self._staycation.get_hotelName()

    def get_checkInDate(self):
        return self._checkInDate.strftime("%d/%b/%Y")

    def get_checkOutDate(self):
        checkOutDate = self._checkInDate + timedelta(days=self._staycation.get_nights()) 
        return checkOutDate.strftime("%d/%b/%Y")

    def get_cost(self):
        return self._cost

    def costDifferenceFromCurrent(self):
        return self._staycation.get_cost() - self._cost

    def __str__(self):
        return self._staycation.__str__() +"\n"+"Booked at: $"+str(self._cost)+" Check-in Date: "+str(self.get_checkInDate())+" Check-out Date: "+str(self.get_checkOutDate())+"\n"+self._customer.__str__()

# D

customer = Customer("peter","99998888")

customer.set_contact('99998844')
customer.__str__()

staycaution1 = Staycation('Grand Marina',2,398.00)
staycaution1.__str__()

staycaution2 = Staycation('Hotel Bugis',1,168.00)
staycaution2.set_voucherAllowed(False)
staycaution2.__str__()

booking = Booking(customer,staycaution1,datetime.strptime("30/6/2021",'%d/%m/%Y'))
print(booking.__str__())

booking._staycation.set_cost(438.00)
print(booking.get_cost())
booking.costDifferenceFromCurrent()

