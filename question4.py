from tkinter import *
from tkinter.scrolledtext import ScrolledText
from datetime import datetime


class gui:
    def __init__(self):
        self.root = Tk()

        # TITLE
        self.root.title('Hakeem Staycation and Booking Management')

        # STAYCAUTIONS AND BOOKINGS INITIALIZATIONS
        self.staycations = {'GM1' : ['Grand Marina', 1, 238], 'GM2' : ['Grand Marina', 2, 398],
                        'HB1' : ['Hotel Bugis', 1, 168], 'HB2' : ['Hotel Bugis', 2, 300],
                        'HB3' : ['Hotel Bugis', 3 , 400]}
        self.bookings=[]

        # PREPARE FRAMES
        headerFrame = Frame(self.root)
        topFrame = Frame(headerFrame)
        buttonFrame = Frame(headerFrame)
        textFrame = Frame(self.root)

        # RADIO BUTTONS AND VARIABLE
        var = StringVar()
        enableStaycautionRadioButton = Radiobutton(topFrame, text="Booking", variable=var, value="0", command=lambda: self.enableStaycaution())
        enableBookingRadioButton = Radiobutton(topFrame, text="Staycation", variable=var, value="1", command=lambda: self.enableBooking())

        # LABELS FOR BOOKING
        StaycationCodeLabel = Label(topFrame, text='Staycation code: ')
        CustomerLabel = Label(topFrame, text='Customer ID')

        # LABELS FOR STAYCAUTION
        StaycationCodeLabel2 = Label(topFrame, text='Staycation code: ')
        HotelNameLabel = Label(topFrame, text='Hotel Name: ')
        NightsLabel = Label(topFrame, text='Nights: ')
        CostLabel = Label(topFrame, text='Cost: $')
        
        # INPUT FOR BOOKING
        self.StaycationCodeText = Entry(topFrame)
        self.CustomerIdText = Entry(topFrame)

        # INPUT FOR STAYCAUTION
        self.StaycationCodeText2 = Entry(topFrame)
        self.HotelNameText = Entry(topFrame)
        self.NightsText = Entry(topFrame)
        self.CostText = Entry(topFrame)

        # OUTPUT AREA
        self.textArea = ScrolledText(textFrame, height=10, width=90)

        
        # BUTTON AREA
        self.addBtn = Button(buttonFrame, text='Add', command=lambda: self.add(var.get()))
        self.removeBtn = Button(buttonFrame, text='Remove', command=lambda: self.remove(var.get()))
        self.displayBtn = Button(buttonFrame, text='Display', command=lambda: self.display(var.get()))

        # ALIGNMENT/POSITIONING OF ELEMENTS
        enableStaycautionRadioButton.grid(row=0,column=0)
        enableBookingRadioButton.grid(row=0,column=2)

        StaycationCodeLabel.grid(row=2)
        self.StaycationCodeText.grid(row=2, column=1)
        CustomerLabel.grid(row=3)
        self.CustomerIdText.grid(row=3, column=1)

        StaycationCodeLabel2.grid(row=1,column=2)
        self.StaycationCodeText2.grid(row=1, column=3)
        HotelNameLabel.grid(row=2,column=2)
        self.HotelNameText.grid(row=2, column=3)
        NightsLabel.grid(row=3,column=2)
        self.NightsText.grid(row=3, column=3)
        CostLabel.grid(row=4,column=2)
        self.CostText.grid(row=4, column=3)

        

        self.addBtn.grid(row=1,column=0)
        self.removeBtn.grid(row=1, column=2)
        self.displayBtn.grid(row=1, column=4)

        self.textArea.grid()

        topFrame.pack(side=TOP)
        buttonFrame.pack(side=BOTTOM)
        # enableStaycautionRadioButton.pack(anchor=W)
        # enableBookingRadioButton.pack(anchor=W)
        
        headerFrame.pack(pady=(0, 10), padx=(5, 20))
        textFrame.pack()
        mainloop()

    # BUTTONS FUNCTIONALITIES

    def add(self,selected):

        if selected == "": self.textArea.insert(END, 'Select either Booking or Staycation first.\n')

        elif selected == "0":
            staycautionCode = self.StaycationCodeText.get()
            CustomerId = self.CustomerIdText.get()

            if staycautionCode=="" or CustomerId=="": self.textArea.insert(END, 'Please complete all the fields.\n')
            else:
                try: booking = self.staycations[staycautionCode]
                except: self.textArea.insert(END, 'Invalid staycation code.\n')
                else:
                    self.bookings.append([staycautionCode,CustomerId])
                    self.textArea.insert(END, 'Added a booking.\n')
                    self.StaycationCodeText.delete(0, END)
                    self.CustomerIdText.delete(0, END)

        elif selected == "1":
            staycautionCode2 = self.StaycationCodeText2.get()
            hotelName = self.HotelNameText.get()
            nights = self.NightsText.get()
            cost = self.CostText.get()

            print(staycautionCode2,hotelName,nights,cost)


            if staycautionCode2=="" or hotelName=="" or nights=="" or cost=="": self.textArea.insert(END, 'Please complete all the fields.\n')
            else:
                try: booking = self.staycations[staycautionCode]
                except: pass
                else: self.textArea.insert(END, 'This code belongs to an existing staycation. Check the input.\n')
                self.staycations.update({staycautionCode2 : [hotelName, int(nights), int(cost)],})
                self.textArea.insert(END, 'Added a staycation.\n')


    def remove(self,selected):
    
        if selected == "": self.textArea.insert(END, 'Select either Booking or Staycation first.\n')

        elif selected == "0":
            staycautionCode = self.StaycationCodeText.get()
            CustomerId = self.CustomerIdText.get()

            if staycautionCode=="" or CustomerId=="": self.textArea.insert(END, 'Please complete all the fields.\n')
            else:
                try: booking = self.staycations[staycautionCode]
                except: self.textArea.insert(END, 'Invalid staycation code.\n')
                else:

                    # remove matching booking
                    i = 0
                    length = len(self.bookings)
                    init_lenght = len(self.bookings)

                    while i < length:
                        if self.bookings[i][0] == staycautionCode:
                            self.bookings.remove(self.bookings[i])
                            break
                        i += 1

                    if len(self.bookings) == init_lenght:
                        self.textArea.insert(END, 'No matching booking to remove. Check the input.\n')
                        
                    else:
                        self.textArea.insert(END, 'Removed a booking.\n')
                        self.StaycationCodeText.delete(0, END)
                        self.CustomerIdText.delete(0, END)

        elif selected == "1":
            staycautionCode2 = self.StaycationCodeText2.get()
            hotelName = self.HotelNameText.get()
            nights = self.NightsText.get()
            cost = self.CostText.get()

            if staycautionCode2=="" or hotelName=="" or nights=="" or cost=="": self.textArea.insert(END, 'Please complete all the fields.\n')
            else:
                try: booking = self.staycations[staycautionCode2]
                except Exception as e: 
                    self.textArea.insert(END, 'This code does not belongs to an existing staycation. Check the input.\n')
                else: 
                    if hotelName!=booking[0] or int(nights)!=booking[1] or int(cost)!=booking[2]:
                        self.textArea.insert(END, 'No matching staycation to remove. Check the input.\n')
                    else:   
                        del self.staycations[staycautionCode2]
                        self.textArea.insert(END, 'Removed a staycation.\n')
                        self.StaycationCodeText2.delete(0, END)
                        self.HotelNameText.delete(0, END)
                        self.NightsText.delete(0, END)
                        self.CostText.delete(0, END)

        
        
    def display(self,selected):
    
        if selected == "": self.textArea.insert(END, 'Select either Booking or Staycation first.\n')

        elif selected == "0":
            if self.bookings != []:
                for booking in self.bookings:
                    self.textArea.insert(END, "staycation code: "+str(booking[0])+" customer id: "+str(booking[1])+"\n")
            else:
                self.textArea.insert(END, "No booking currently.\n")

        elif selected == "1":
            if self.staycations != {}:
                for key,value in self.staycations.items():
                    self.textArea.insert(END, "staycation code: "+str(key)+" "+str(" ".join([str(x)for x in value]))+"\n")
            else:
                self.textArea.insert(END, "No staycation currently.")

    
    # RADIO BUTTONS FUNCTIONS            
    
    def enableStaycaution(self):
        self.StaycationCodeText.configure(state="normal")
        self.StaycationCodeText.update()
        self.CustomerIdText.configure(state="normal")
        self.CustomerIdText.update()

        self.StaycationCodeText2.delete(0, END)
        self.StaycationCodeText2.configure(state="disable")
        self.StaycationCodeText2.update()

        self.HotelNameText.delete(0, END)
        self.HotelNameText.configure(state="disable")
        self.HotelNameText.update()

        self.NightsText.delete(0, END)
        self.NightsText.configure(state="disable")
        self.NightsText.update()

        self.CostText.delete(0, END)
        self.CostText.configure(state="disable")
        self.CostText.update()

    def enableBooking(self):
        self.StaycationCodeText2.configure(state="normal")
        self.StaycationCodeText2.update()
        self.HotelNameText.configure(state="normal")
        self.HotelNameText.update()
        self.NightsText.configure(state="normal")
        self.NightsText.update()
        self.CostText.configure(state="normal")
        self.CostText.update()
        
        self.StaycationCodeText.delete(0, END)
        self.StaycationCodeText.configure(state="disable")
        self.StaycationCodeText.update()
        self.CustomerIdText.delete(0, END)
        self.CustomerIdText.configure(state="disable")
        self.CustomerIdText.update()
        
ui = gui()
