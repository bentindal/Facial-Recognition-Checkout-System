import datetime


def get_date():
    date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return date


print('(' + get_date() + ') Loading imports... 0%')

import random
from shutil import copy
from pyzbar import pyzbar
from tkinter import *
import PIL
from PIL import ImageTk
import face_recognition
import cv2
import numpy as np
import sqlite3

database = sqlite3.connect('checkout_data.db')
db = database.cursor()

# Declaring Variables
whatScreen = 'Setup'
known_face_encodings = []
known_face_names = []  # Contains names of each user loaded
User = ['', '', '', '', '', '', '', '', '']
Product = ['', '', '', '', '', '', '', '']
delay = 50  # Delay between returning labels to default values
countdown = delay
switchDelay = 5  # Delay before scanning first face (at load-up) to prevent crashing
last_barcode = ''
repeatDelay = 25  # Delay between allowing new purchase


# Gets highest ID being used so that new users can be assigned correct IDs
def get_highest_id():
    global last_id
    last_id = sorted(known_face_names)  # Sorts the known face names list and sorts it in ascending order
    last_id = last_id[len(last_id) - 1]  # and gets the highest value to be used when adding new users to the database
    last_id = int(last_id)


# Charge function
def charge(userid, amount):
    db = database.cursor()
    for bal in db.execute('SELECT Balance FROM tbl_UserData WHERE UserID ="{}"'.format(str(userid))):
        bal = float(bal[0])
        bal = round(bal, 2)
        amount = float(amount)
        amount = round(amount, 2)
        if bal - amount >= 0:
            bal = bal - amount
            bal = round(bal, 2)
            db.execute(
                'UPDATE tbl_UserData SET Balance ="{}"'.format(str(bal)) + 'WHERE UserID ="{}"'.format(str(userid)))
            db.close()
            print('(' + get_date() + ')', User[1], 'made a purchase of "', Product[1] + '" costing £' + str(amount))
            return True

        else:
            print('(' + get_date() + ')', User[1], 'failed a purchase of "', Product[1] + '" costing £' + str(amount),
                  'as they did not have a high enough balance.')
            db.close()
            return False


# Quick scan, take a quick snapshot to analyse barcode
def quickScanCode():
    # Load camera output
    print('(' + get_date() + ') Scanning for barcode...')
    for i in range(0, 11):
        vid = CameraOutput(0)
        ret, frame = vid.get_frame()
        decodedObjects = pyzbar.decode(frame)
        if len(decodedObjects) == 1:
            result = decodedObjects[0].data
            result = result  # [1:len(result) - 1]
            current_screen.barcode_entry.configure(text=result)
            print('(' + get_date() + ') Barcode "' + result + '" found in scan!')


def quickScanFace():
    for i in range(0, 2):
        vid = CameraOutput(0)
        frame = vid.get_frame()[1]
    cv2.imwrite("Screenshots/frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    current_screen.imageScan.configure(text='Photo Taken')


# Takes scanned barcode data from image
def barcodeLookup(decodedObjects):
    global last_barcode, Product, repeatDelay
    for obj in decodedObjects:
        raw_barcode = obj.data
        if repeatDelay <= 0:
            repeatDelay = 25
            last_barcode = ''
        if raw_barcode != last_barcode:  # Prevents 'spam' of checking
            last_barcode = raw_barcode
            raw_barcode = str(raw_barcode)
            barcode = raw_barcode[2:len(raw_barcode) - 1]
            # Now we have a new barcode, lets look it up in the product table
            db = database.cursor()
            for column in db.execute('SELECT * FROM tbl_Products WHERE BarcodeNumber ="{}"'.format(str(barcode))):
                Product = column
                buyProduct(Product)
                return
            print('(' + get_date() + ') Barcode "' + barcode + '" not recognised!')
            db.close()

        else:
            last_barcode = raw_barcode


# Buy the actual product
def buyProduct(product):
    if len(User) == 4 and len(
            product) == 4:  # checks that there is a valid user/product located, if so item can be bought!
        if product[2] > 0:
            term = '(-£', 'RED'  # Determines whether the bought product is a positive or negative value assigning an appropiate colour
        elif product[2] < 0:
            term = '(+£', 'GREEN'
        else:
            term = '( £', 'GREY'
        current_recent_purchases = str(current_screen.db_purchases_label.cget('text'))
        # if len(current_recent_purchases) > 0:
        # current_recent_purchases = str(current_recent_purchases) + '\n'  # If there's already data in the label then adds a newline
        if charge(User[0], product[2]) is True:
            database.commit()
            current_screen.db_purchases_label.configure(
                text=(product[1] + term[0] + str(product[2]) + ')\n' + current_screen.db_purchases_label.cget('text')),
                bg=term[1])  # Adds the newly bought product with the text background colour of term[2]
        else:
            current_screen.db_purchases_label.configure(
                text=(str(product[2]) + ' CANNOT AFFORD\n' + current_screen.db_purchases_label.cget('text')),
                bg='GREY')  # Adds the newly bought product with the text background colour of term[2]
    else:
        print('(' + get_date() + ') There was no user present to purchase the product.')  # Item should not be bought
    return


# Looks up the userID specified in the tbl_UserData table.
def loadUser(id):
    global User
    db = database.cursor()
    for column in db.execute('SELECT * FROM tbl_UserData WHERE UserID ="{}"'.format(str(id))):
        User = []
        for i in range(len(column)):
            User.append(column[i])
    db.close()


def loadFaces():
    try:
        global known_face_encodings, known_face_names
        # Create arrays of known face encodings and their names
        known_face_encodings = []
        known_face_names = []
        db = database.cursor()
        for photo in db.execute('SELECT * FROM tbl_Photos'):  # WHERE UserID = 1'):
            user_image = face_recognition.load_image_file("Photos/" + photo[0] + ".jpg")  # get directory from db
            face_encoding = face_recognition.face_encodings(user_image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(photo[1])  # UserID as name
        db.close()
    except:
        print('(' + get_date() + ') Error on loading one or more face encodings from database...')
    print('(' + get_date() + ') The following UserIDs were loaded correctly', known_face_names)


# Takes current frame from web-cam and scans it for known faces, if found, calls the matched ID on the loadUser function
# Sets result of loadUser function to the checkout screen parameters.
def faceScan(frame):
    global switchDelay, countdown, User, Product, repeatDelay
    if repeatDelay > 0:
        repeatDelay = repeatDelay - 1
    if switchDelay > 0:
        switchDelay = switchDelay - 1
    if switchDelay <= 0:
        frame = cv2.resize(frame, (0, 0), fx=0.25,
                           fy=0.25)  # Shrinks the image down to the size needed for the library to reduce memory requirements
        frame = frame[:, :, ::-1]  # Crops out unnecessary data from the resized image
        face_locations = face_recognition.face_locations(frame)  # Runs the library on the image
        if len(face_locations) > 1:
            return
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        if len(face_encodings) == 0:
            if countdown <= 0:
                current_screen.db_name_label.configure(text=current_screen.db_name)
                current_screen.db_balance_label.configure(text=current_screen.db_balance)
                current_screen.db_purchases_label.configure(text=current_screen.db_purchases, bg='MediumPurple1')
                User = ''
                Product = ''
                # revert past purchases variable back to default parameter defined in current_screen
            if countdown > 0:
                countdown = countdown - 1
        for face_encoding in face_encodings:  # Goes through each found face and compares it to all the database faces.
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index: np.ndarray[int] = np.argmin(
                face_distances)  # Stores the location of the discovered face (if any)
            if matches[best_match_index]:  # If match has been found:
                name = known_face_names[best_match_index]  # Looks up the name
                loadUser(name)

                countdown = delay

                current_screen.db_name_label.configure(text=User[1] + ' ' + User[2])
                bal = User[3]
                bal = round(bal, 2)
                bal = str(bal)

                dot_check = bal[len(bal) - 2]

                if dot_check == '.':
                    bal = bal + '0'
                current_screen.db_balance_label.configure(text='£' + bal)
                # Once past purchases have been created, edit the current_screen past purchase label here
    decodedObjects = pyzbar.decode(frame)
    if len(decodedObjects) == 1:
        barcodeLookup(decodedObjects)


# Screen Switching
def switchScreen1():
    global current_screen, whatScreen
    print('(' + get_date() + ') Screen switched to "Home Screen"')
    whatScreen = 'Setup'
    current_screen.destroy()
    current_screen = setup_Screen()


def switchScreen2():
    global current_screen, whatScreen
    print('(' + get_date() + ') Screen switched to "Add Product Screen"')
    whatScreen = 'Products'
    current_screen.destroy()
    current_screen = product_Screen()


def switchScreen3():
    global current_screen, whatScreen
    print('(' + get_date() + ') Screen switched to "Add User Screen"')
    whatScreen = 'Users'
    get_highest_id()
    current_screen.destroy()
    current_screen = user_Screen()
    next_id = last_id + 1
    next_id = str(next_id)
    current_screen.id_display.configure(text=next_id)


def switchScreen4():
    global current_screen, switchDelay, whatScreen, User, Product
    print('(' + get_date() + ') Screen switched to "Checkout Screen"')
    current_screen.destroy()
    switchDelay = 5
    current_screen = checkout_Screen()
    whatScreen = 'Main'
    User = ['', '', '', '', '', '', '', '', '']
    Product = ['', '', '', '', '', '', '', '']  # reset current user/product parameters


print('(' + get_date() + ') Loading Screens... 25%')


# Screen Classes
class setup_Screen:  # Screen ID 1 - SwitchScreen1()
    def __init__(self):
        self.window = Tk()

        # Code to create the screen
        self.window.configure(bg='MediumPurple1')
        self.window.title('Setup')
        self.window.geometry('1024x612+0+0')

        # Main header of the screen titled "Setup Screen"
        label1 = Label(text='Setup System', font=('Calibri Bold', 90))
        label1.configure(bg='MediumPurple4')
        label1.grid(row=0, ipadx=250)

        # Sub-title/header "Would you like to?"
        label2 = Label(text='Would you like to?', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=1, pady=20)

        start_button = Button(text='Start Program', command=switchScreen4, font=('Calibri Bold', 40))
        start_button.configure(fg='Green', borderwidth='3', relief='solid')
        start_button.grid(row=2, ipadx=150, ipady=30)

        # First Button linked to add new product page
        product_button = Button(text='Add new Product', command=switchScreen2, font=('Calibri', 30))
        product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
        product_button.grid(row=3, pady=50, ipadx=28 + 100, ipady=10)

        # Second Button linked to add new product page
        user_button = Button(text='Add new User', command=switchScreen3, font=('Calibri', 30))
        user_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
        user_button.grid(row=4, ipadx=51 + 100, ipady=10)

        self.is_wanted = True

    def loop(self):
        self.window.mainloop()

    def destroy(self):
        self.is_wanted = False
        self.window.destroy()


class product_Screen:  # Screen ID 2 - SwitchScreen2()
    def __init__(self):
        self.window = Tk()

        # Code to create the screen
        self.window.configure(bg='MediumPurple1')
        self.window.title('Products')
        self.window.geometry('1024x612+0+0')

        # Main header of the screen titled "Add Product Screen"
        label1 = Label(text='Add Product Screen', font=('Calibri Bold', 90))
        label1.configure(bg='MediumPurple4')
        label1.grid(row=0, column=1)

        # Home Button linked to add setup screen
        product_button = Button(text='Home', command=switchScreen1, font=('Calibri', 30))
        product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
        product_button.grid(row=0, column=0)

        label2 = Label(text='Name', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=1, column=1, pady=20, sticky=W)

        self.name_entry = Entry(self.window)
        self.name_entry.grid(row=1, column=1, pady=20)

        label2 = Label(text='Barcode', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=2, column=1, pady=20, sticky=W)

        self.barcode_entry = Button(text='Click to Scan', command=quickScanCode)
        self.barcode_entry.grid(row=2, column=1, pady=20)

        label2 = Label(text='Cost', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=3, column=1, pady=20, sticky=W)

        self.cost_entry = Entry(self.window)
        self.cost_entry.grid(row=3, column=1, pady=20)

        label2 = Label(text='Description', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=4, column=1, pady=20, sticky=W)

        self.description_entry = Entry(self.window)
        self.description_entry.grid(row=4, column=1, pady=20)

        # Second Button linked to add new product page
        self.user_button = Button(text='Submit', command=self.add_record, font=('Calibri', 30))
        self.user_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
        self.user_button.grid(row=7, column=1, ipadx=100, ipady=15)

        self.is_wanted = True

    def add_record(self):
        name = self.name_entry.get()
        barcode = str(self.barcode_entry.cget('text'))
        barcode = barcode[2:len(barcode) - 1]
        cost = self.cost_entry.get()
        description = self.description_entry.get()
        print('(' + get_date() + ') The following product was attempted to be added to the database: "' + name + '"',
              '"' + barcode + '"', '"' + cost + '"', '"' + description + '"')
        if name == '' or barcode == 'ick to Sca' or cost == '' or description == '':
            self.user_button.configure(text='Boxes above cannot be blank!', bg='RED')
            print('(' + get_date() + ') Product did not meet one or more requirements')
            return
        try:
            float(cost)
        except ValueError:
            self.user_button.configure(text='Cost must be a valid number\ne.g 1.99', bg='RED')
            print('(' + get_date() + ') Product did not meet one or more requirements')
            return
        db = database.cursor()
        for line in db.execute('SELECT BarcodeNumber, Title FROM tbl_Products WHERE BarcodeNumber = "{}"'.format(
                barcode) + 'OR Title = "{}"'.format(name)):
            self.user_button.configure(text='Already Exists', bg='RED')
            print('(' + get_date() + ') Product did not meet one or more requirements')
            return
        db.execute('INSERT INTO tbl_Products VALUES ("{}"'.format(barcode) + ', "{}"'.format(name) + ', "{}"'.format(
            cost) + ', "{}"'.format(description) + ')')
        database.commit()
        print('(' + get_date() + ') Product successfully added to the Products table!')
        db.close()
        self.user_button.configure(text='Product Successfully Added!', bg='GREEN')

    def loop(self):
        self.window.mainloop()

    def destroy(self):
        self.is_wanted = False
        self.window.destroy()


class user_Screen:  # Screen ID 3 - SwitchScreen3()
    def __init__(self):
        self.window = Tk()

        # Code to create the screen
        self.window.configure(bg='MediumPurple1')
        self.window.title('Users')
        self.window.geometry('1024x612+0+0')

        # Main header of the screen titled "Add Product Screen"
        label1 = Label(text='Add User Screen', font=('Calibri Bold', 90))
        label1.configure(bg='MediumPurple4')
        label1.grid(row=0, column=1)

        # Home Button linked to add setup screen
        product_button = Button(text='Home', command=switchScreen1, font=('Calibri', 30))
        product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
        product_button.grid(row=0, column=0)

        label2 = Label(text='UserID', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=1, column=0, pady=20)

        self.id_display = Label(text='Unknown', font=('Calibri', 20))
        self.id_display.configure(bg='MediumPurple2')
        self.id_display.grid(row=1, column=1, pady=20)

        label2 = Label(text='First Name', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=2, column=0, pady=20)

        self.firstName_entry = Entry(self.window)
        self.firstName_entry.grid(row=2, column=1, pady=20)

        label2 = Label(text='Surname', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=3, column=0, pady=20)

        self.surname_entry = Entry(self.window)
        self.surname_entry.grid(row=3, column=1, pady=20)

        label2 = Label(text='Face Image', font=('Calibri', 20))
        label2.configure(bg='MediumPurple2')
        label2.grid(row=4, column=0, pady=20)

        self.imageScan = Button(text='Click to take a photo!', command=quickScanFace)
        self.imageScan.grid(row=4, column=1, pady=20)

        # Second Button linked to add new product page
        self.user_button = Button(text='Submit', command=self.add_record, font=('Calibri', 30))
        self.user_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
        self.user_button.grid(row=6, column=1, ipadx=100, ipady=15)

        self.is_wanted = True

    def add_record(self):
        firstname = self.firstName_entry.get()
        surname = self.surname_entry.get()
        if self.imageScan.cget('text') == 'Click to take a photo!':
            self.user_button.configure(text='You need to take a photo first!')
            print('(' + get_date() + ') Failed to meet New User criteria')
            return
        if firstname == '':
            self.user_button.configure(text='First name cannot be blank')
            print('(' + get_date() + ') Failed to meet New User criteria')
            return
        if surname == '':
            self.user_button.configure(text='Surname cannot be blank')
            print('(' + get_date() + ') Failed to meet New User criteria')
            return
        for line in db.execute('SELECT Firstname, Surname FROM tbl_UserData WHERE Firstname = "{}"'.format(
                firstname) + 'AND Surname = "{}"'.format(surname)):
            self.user_button.configure(text='User Already Exists', bg='RED')
            print('(' + get_date() + ') Product did not meet one or more requirements')
            return

        next_id = str(last_id + 1)
        random_number = str(random.randint(0, 999999))
        photoid = random_number + next_id

        # Information accepted, now insert data into the database
        db.execute(
            'INSERT INTO tbl_UserData VALUES ("{}"'.format(next_id) + ', "{}"'.format(firstname) + ', "{}"'.format(
                surname) + ', "5")')
        copy('Screenshots/frame.jpg', 'Photos/' + str(photoid) + '.jpg')
        db.execute(
            'INSERT INTO tbl_Photos VALUES ("{}"'.format(photoid) + ', "{}"'.format(next_id) + ')')
        database.commit()
        self.user_button.configure(text='User Added')
        print('(' + get_date() + ') User successfully added to the UserData table!')
        loadFaces()

    def loop(self):
        self.window.mainloop()

    def destroy(self):
        self.is_wanted = False
        self.window.destroy()


class checkout_Screen:  # Screen ID 4 - SwitchScreen4()
    def __init__(self, video_source=0):
        # Code to create the screen
        self.window = Tk()
        self.window.configure(bg='MediumPurple1')
        self.window.title('Products')
        self.window.geometry('1024x612+0+0')
        # Database Variables
        self.db_name = '                 '  # Default Parameters
        self.db_balance = '         '
        self.db_purchases = ''
        # Back to the screen
        self.video_source = video_source

        # Load camera output
        self.vid = CameraOutput(self.video_source)
        # Home Button linked to add setup screen
        product_button = Button(text='Home', command=switchScreen1, font=('Calibri', 30))
        product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
        product_button.grid(row=0, column=0, sticky=W)

        # Main header of the screen titled "Setup Screen"
        label1 = Label(text='Checkout Screen', font=('Calibri Bold', 90))
        label1.configure(bg='MediumPurple4')
        label1.grid(row=0, column=1, columnspan=3, ipadx=100, sticky=E)

        # Create a canvas that can fit the above video source size
        self.canvas = Canvas(width=500, height=450)
        self.canvas.grid(row=2, column=0, columnspan=2, rowspan=5, ipadx=0, sticky=W)

        # Database Variables on screen
        self.db_label = Label(text='Name:', font=('Calibri', 30, 'bold'), bg='MediumPurple3')
        self.db_label.grid(row=2, column=2, sticky=NW)
        self.db_label = Label(text='Balance:', font=('Calibri', 30, 'bold'), bg='MediumPurple3')
        self.db_label.grid(row=3, column=2, sticky=NW)
        self.db_label = Label(text='Recent Purchases:', font=('Calibri', 30, 'bold'), bg='MediumPurple3')
        self.db_label.grid(row=4, column=2, sticky=NW)

        self.db_name_label = Label(text=self.db_name, font=('Calibri', '50'), bg='MediumPurple2')
        self.db_balance_label = Label(text=self.db_balance, font=('Calibri', '30'), bg='MediumPurple2')
        self.db_purchases_label = Label(text=self.db_purchases, font=('Calibri', '20'), bg='MediumPurple1')
        self.db_name_label.grid(row=2, column=2, sticky=SW, ipadx=50, ipady=35)
        self.db_balance_label.grid(row=3, column=2, sticky=SW, ipadx=50, ipady=0)
        self.db_purchases_label.grid(row=5, column=2, sticky=SW, ipadx=25, ipady=0, rowspan=2, columnspan=2)

        # update method called after a delay of 1ms
        self.delay = 1
        self.update()

        self.is_wanted = True

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            frame = cv2.resize(frame, (0, 0), fx=0.45, fy=0.70)
            self.photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.window.after(self.delay, self.update)

    def loop(self):
        self.window.mainloop()

    def destroy(self):
        self.is_wanted = False
        self.window.destroy()


# Camera Output
class CameraOutput:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if whatScreen == 'Main':
                faceScan(frame)
            return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


print('(' + get_date() + ') Encoding faces... 50%')

loadFaces()  # Loading photos of face from database and encoding them

print('(' + get_date() + ') Loading completed, initialising GUI... 100%')
print('\n- LOG STARTED -')

# Start of main program
current_screen = setup_Screen()  # Declares the first screen that will be loaded
# print('Time Taken:', str(time.clock()))  # Big O Notation of o(n) (linear)
current_screen.loop()  # Starts the loop of the screen
print('- LOG ENDED -')
try:
    print('(' + get_date() + ') Attempting to close database...')
    db.close()  # Closes the database to ensure no data is changed after the program is closed.
    print('(' + get_date() + ') Database Closed')
except:
    print('(' + get_date() + ') Closing database resulted in an error. Database may already be closed')
quit()

