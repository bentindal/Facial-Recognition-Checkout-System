    H446 – 03 Computer Science Project
Facial Recognition Canteen Checkout System

 

   Analysis of my Program
What does this software do and what makes this solvable by a computer? (3.1.1 A)
Current canteen systems are slow and require someone to individually calculate how much something costs and return change. This leads to great long queues at peak times. The software will allow users to self-checkout using a combination of facial recognition and barcode scanning to ensure a fast and efficient checkout process that will minimise queues and provide canteens with security and speed. Although it may be used for wider purposes for example, a supermarket checkout, my particular software will be targeted at a canteen, more specifically in this case a school canteen.
Problem Why is a computer suited to solving this?
      Canteen queues are long and slow, how can a computer help this?
     Computers can solve billions of calculations a second, far greater and faster than any human can do, therefore the software is amenable to a computational approach as the software will handle all the checking out which will save customers lots of time as it will be able to do it far faster than any human could.
  People get charged incorrect amounts/given incorrect change, how will this help?
  Another benefit of a computer is that it can perform calculators with 100% accuracy, as long as the correct data is inputted into it will never be incorrect hence users will be always charged the correct amount.
Customers will be given digital balances so change will not need to be given hence as long as customers are correctly charged there will be no incorrect change.
   People steal from canteens, surely with a digital program with no physical presence this problem will get worse?
     The software will be able to see what customer have/have not payed. Because of its facial recognition software it can easily log user’s faces/names that have not payed.
1) The software will act as a deterrent,
 1
 
          customers will be made aware of the above so will be put off.
2) Customers that do steal will have their details logged and will make it obvious who did steal, it will also block them out of the system.
  What if I forget to bring in money?
     With a digital balance there will be no need to carry around money, it will simply use an online balance and adjust that digital balance appropriately per transaction.
   Will this software be expensive to run? What other devices are needed to get this to run?
   The software requires low-spec computational power along with a simple webcam that is typically embedded in most computer systems nowadays anyway meaning it is low- cost.
 Why is this suited to a computational approach? (3.1.1 B)
Abstraction and a Graphical User Interface (GUI) will be used to create a simple, easy-to-use GUI that will only contain information that the user will need to utilise it. It will be used to mask the code that will be needed to run it. This will be done through the use of two python libraries, OpenCV and Tkinter. OpenCV will provide the utilisation of imaging and Tkinter will provide the basis of the GUI.
Storing/Retrieving data using an SQLite database will be used to; store all the users of the software including their passwords, balances, a log of all purchases made using the software along with a timestamp and the user that made the purchase, store a log of all products that can be purchased using the system and finally store all the users of the software’s face encodings/pictures so that they can be individually recognised using the software. Data will be moved back and forth from these by importing an SQLite library to python that is capable of executing SQL commands from within the code.
Decomposition will be used to break down the software into multiple ‘problems’ that will need to be solved, for example, scanning the products will need to be done using a barcode scanner along with its appropriate software and recognising each student via facial recognition are two separate tasks that need to be completed through the use of procedures and functions.
2
 
   Who are the Stakeholders Involved? (3.1.2)
The end user/stakeholders involved in my software will primarily be the customers of a canteen style checkout system meaning anyone who would like to purchase something from the canteen. The customers will take products and checkout using the software, it will also record their faces and their online balance. The customer will be the primary operator of the software. They will be the ones to top-up their balance in order to make purchases on the system. It is appropriate to their needs as it will save them time compared to a typical checkout system and make it so they do not need to carry money on them reducing the risk significantly of money being lost/stolen.
The other secondary stakeholder will be the canteen workers/staff that will initially setup users on the system by running the given setup program. They will setup each product on the database using the program and will overlook the operation of the software. They will be interested as the software once setup will save them lots of time off the checkout and will allow them to focus more on other tasks for example, keeping the area clean & cooking the food.
The other secondary stakeholder in the context of a school would be the administration at the school as they are the ones who will invest in the software and if needed an external webcam. They will be interested to invest in this as it is firstly, cheap because of the low- spec requirements needed to run it and the fact that it simply uses a webcam rather than a specialised camera system that can be expensive and secondly and secondly, will save the administration time/effort dealing with food being stolen and time lost spent counting up money.
What is the Problem & What Solutions already exist? (3.1.3 A)
The main problem and need for this software is the fact that current checkout systems are outdated and need to undergo change. They are slow leading to long queues, prone to human counting errors and are susceptible to people shoplifting.
Here are some solutions that already exist:
Current Modern Checkout System (specifically looking at Morrison’s Checkout) My local branch of Morrisons contains several
generic checkout systems, they each use a
conveyer belt that moves any item that has
been manually placed on it towards the cashier who has to manually scan in each item, then after scanning each item asks the customer to pay. This whole process takes around 5-10 minutes which is very lengthy and something that I hope to cut down on using my software.
 3
A picture of a typical supermarket checkout system.
Wolfmann [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)]
  
   Current Modern Self-Checkout System (Using Morrison’s as the example)
Bigger branches of supermarkets/shops tend to have their own self-checkout systems, despite being expensive they provide customers with a way to make cashier-free purchases buy scanning their item themselves, putting it on a weight censor that checks that the item has been placed on it before allowing the next item to be scanned and then allowing the customer to pay for their item on the same digital screen. This sounds amazing and all but as we all know when actually implemented it constantly messes up and thus requires a member of staff to be on duty overlooking the machines constantly heading back and forth between self- checkouts dealing with errors. These machines are expensive so smaller branches cannot afford to use them, my software is very cheap in comparison and ideally will not keep breaking down in errors like current self-checkout systems.
The diagram below has been adapted to show the inputs and outputs of a typical self-checkout system.
   Output: Digital Display shows scanned items, cost and gives me the ability to manually add items e.g fruit that doesn’t have a barcode
 Input: Put in money/card in order to pay for goods
  Input: Allows the user to scan the barcodes of their item they wish to buy
  Input: Sends weight data to the processor to allow it to decide whether the correct product has been placed there or not for security
 https://www.toshibacommerce.com/wps/portal/marketing/?urile=wcm:path:/en/home/products/hardware/self-checkout/self-checkout-6
Amazon’s Surveillance Powered no-checkout convenience store
 4
 
   The first store was setup in Seattle that allowed users to scan a code upon entry on the ‘Amazon Go App’ on their phone and then enter a store. Using a network of around a hundred cameras combined with pressure sensors all connected to a central server, customers are able to pick up individual products and simply walk out of the store. They are consequently then billed for the items that they picked up upon leaving via their amazon account.
In the diagram (figure 5) above you can see the immense network of cameras all connected to a central processor set up all over the ceiling to allow the system to monitor each of the customers.
This approach does not use facial recognition like my software but instead focuses on recognition of a whole. It looks at factors such as what you entirely look like (for example clothes) along with watching what you pick up/sensing the weight changes in real time whereas my approach would simply require you to scan the items you want to check out and allow you to leave. Despite being the first major public release of a hands-free checkout system, it has many flaws such as the hundred cameras being a poor business model due to the immense cost of them all. My software will instead aim to be cheap so that it can be
   5
Figure 5 – Image of the Amazon store’s entrance in Seattle adapted to highlight its network of cameras
Source: https://www.bbc.co.uk/news/business-42769096
  
   implemented nationally without being too much of a money-drain on businesses. The store has also been apparently seen to fail by being tricked by simply two customers wearing similar clothes, whether true or not it makes you questions the reliability of this system. Although as a working concept it is very impressive.
Features of my Computational Solution (3.1.3 B)
My solution will feature facial recognition software making use of a camera. It will also feature an embedded barcode scanner that will identify items that are to be bought. A computational solution for this is vital as computers can complete billions of calculations per second, no human could manually compare the huge numerical encodings of two people’s faces and identify them from a database and map it onto an image from the cameras output in mere milliseconds therefore a computer is essential for this. Having a computer do this will ensure that the software runs efficiently, smoothly and fast enough for it to be a viable solution to improving the current checkout system. Upon scanning the barcode of a product, it will then subtract the cost of the product from the user’s balance found on a database. Having a computer do the maths/processing of payments will eliminate human error which is an essential point of using a computer for the software.
Limitations of my Software (3.1.3 C)
My proposed solution will be limited by all users that use it will have to be manually added to the face recognition database, this is why it is better suited to a school’s canteen as all students are on record/data is stored of all of them whereas in a public supermarket, not all the customers are known so the face recognition will simply render them as unknown and will be unable to get their balance which prevents any purchases from being made using the software. All customers of that supermarket will have to be individually added to the software.
Another limitation is that all products that are to be bought using the software must have had their appropriate barcode added to the product database, if not the software cannot work out the product’s price/title so customers will be unable to purchase said item.
Another limitation is that customers may wish to not have their photos taken and/or be monitored by cameras that will recognise their face utilising the software. If so, the software will be unable to recognise them so the software will not work for them and consequently due to the nature of the program monitoring all people who walk in front of the camera will be unable to block out individuals who do not wish to have their photo taken therefore will not be suited to an area in which a high number of people do not want their photo taken.
Requirements of my Solution (3.1.4 A)
- All users of the software must be manually added to the database using the “New User” program.
6
 
   - All products in the canteen must be manually added to the database using the “New Product” program.
- Balances must be topped up via the “Top-up” program or users of the software will be unable to make purchases.
Software Requirements:
o ForPython,acomputerneeds3.4to4.2GHzofprocessorspeedand1GBofRAM o TheprogramwasdesignedonMacOSsomaynotbecompatiblewithWindows
without extra assistance on installation.
o Computermusthaveawebcamofgoodenoughqualitytobeabletodistinguish
facial body parts, for example, nose/mouth and to be simultaneously be used as a barcode scanner so must be able to distinguish the entire barcode otherwise the software will not be able to function correctly.
o Computermustbepowerfulenoughtosupportlivevideooutputbeingdisplayed from the webcam on a screen.
Success Criteria (3.1.4 B)
The software must be able to individually distinguish users. Without this, it may not recognise students so will not be able to bill them for their purchase which is fundamental for the software to work. If it were to incorrectly identify students, incorrect people may be charged for other student’s purchases, therefore it must be able to individually identify each user of the software. I will measure this by adding 10 different users to the User database and attempt to see if the software can still separately identify each individual student. Ideally, I would add a thousand as that would be more realistic for an entire school, however the computing power that I have available to me would not allow this. If the software can identify each individual user, then I will accept that it meets this particular criterion.
The software must only allow one customer at a time to make said purchase. The software must not get confused when two people enter the camera, it must only allow one user to make said purchase before the other and not bill the other person in the camera. I will measure the success of this criteria by attempting to ‘stress’ test the software by having multiple users in frame with one person attempting to buy something. If the software completes the purchase and bills the correct person with the correct purchases, then I will accept that it meets this particular criterion.
The software must not allow a customer to leave with unpaid items due to a negative balance. If a customer did not have enough money to pay for the item, then if they were to leave, they would have essentially got the item for free causing the school to lose money. This would defeat the entire point of this software being cheap to install as they would have to pay for lost money. I will test this by having multiple users attempt to make a purchase with varying balances, one that is extreme (above the cost of the item so the purchase should go through), normal (one that is below the cost of the item so should result in not allowing the purchase to go through) and erroneous (a balance that is non-numerical for example, a
7
 
   balance of £hello) so should result in error and not allow the purchase to go through.
The software must be able to correctly recognise barcodes stored on the product database.
The software must allow the administrators of the software to be able to add/remove products.
The software must be able to run/work for a sustained period without crashing. The software must be able to log errors and work around them to keep the
software working.
The GUI must be easy to understand and use so that users of all ages can use it. If it were too complicated to use, queues would build up defeating the entire point of minimising queues using the software. I will test this by carefully monitoring strangers to the software by looking at how they use the software and whether they are able to complete a purchase without extra assistance.
8
 
   Designing my Solution
Decomposing the Problem (3.2.1 A)
In the diagram below (Figure 1) I will decompose my problem using an abstracted version of my software in the form of a hierarchal diagram.
   Facial Recognition Canteen System
 File System
 GUI
 Figure 1 – Summary of the three main parts of my software
Code
 The software itself will consist of three main parts (Figure 2) listed below:
• The File system which consists of four tables along with user images for facial recognition.
• The graphical user interface (GUI) which provides the interface that users will interact with
in order to use the program, these will be made using Tkinter (an embedded Python Library).
• The code which includes various functions/procedures, variables & classes that will allow
these tables and images to interact with each other through set algorithms that I will design throughout my coding of the software using Python.
9
 
   File System (3.2.2 A)
First of all is the file system which includes three databases that will contain key information such as product information and students’ data (as abstracted in Figure 3 below).
tbl_Photos
Figure 2
My software will make use of three separate tables using an SQLite 3 database which supports a built-in library (called sqlite3) on Python that can be used to send/retrieve data from the tables using SQL commands (Structured Query Language).
Below I will explain what each table is used for and how it will help me create my facial recognition-based canteen system.
Table 1 tbl_Photos (example of what it looks like)
tbl_Photos
1 12416 51282 92138
3 67124
The columns GroupID and PhotoID will have a one-to-many relationship as one GroupID can have multiple Photos to ensure that it gets each user’s varying appearances to be able to correctly identify them, as without this the software may be unable to recognise the user if they were to wear makeup/alter their appearance
GroupID
  File System
   tbl_Products
tbl_UserData
tbl_UserPhoto
    GroupID
   PhotoID
   2
   34125 12345
   4
   14215 12589
    PhotoID
  10
 
   facially. The collection of photos is assigned a GroupID number that will be assigned a UserID in another table.
One GroupID can have many PhotoIDs so they have a “One-to-Many” relationship Both GroupID and PhotoID will be strings, this is to prevent the data being modified if it were stored as an integer. For example, a GroupID of 00124 stored as an integer would be converted to 124.
The table is important as it is accessed upon initially loading the software. The algorithm shown below for each UserID loads each photo for that particular user’s GroupID and breaks it down into a numerical encoding and assigns it to the user’s ID corresponding with the table. The software then loads that encoding up into the software so that it can be used later. When it comes to the software working out who is who, it can simply compare the camera snapshot to each photo’s face encoding. If it receives a match it gets the user’s ID and then the rest of their data stored that is needed, for example their balance. Below (Figure 4) is a pseudocode example of the algorithm that accesses this table and loads it up into the software.
Figure 4 – Pseudocode Example of the Algorithm to sort through the database and load the face encodings of each user
Figure 4 shows the pseudocode of the algorithm that accesses the Users table and gets each user’s ID, First Name and Surname. For each user the software gets all of its appropriate photos, generates its encodings and adds that to the software’s temporary storage along with each user’s First Name and Surname.
  for every user in the userdata table: get the id of that user
for every photo in the photo table that matches that user’s id: convert photo to a set of encodings and
store it along with the user’s id
11
 
   Table 2 tbl_Products (example of what it looks like)
 tbl_Products
1 13511125125123561
BarcodeNumber
Box of Chocolates
2.99 A standard 10 pack of
chocolates
Product
  ProductID
   BarcodeNumber
   Title
   Cost
   Description
         One Barcode Number can only have one Product assigned to it so they have a one to one relationship
One barcode number is used to link one single product together along with its title, cost and description. If this were not the case then multiple products would be loaded per barcode scanned, which would not work.
ProductID, BarcodeNumber, Title and Description will all be stored as strings whereas Cost will be stored as an integer due to it being numerical (quantitative) data.
Table 3 tbl_UserData (example of what it looks like)
tbl_UserData
1 Ben Tindal 15.25
One UserID can have one FirstName, one Surname and one Balance, therefore all have a one-to-one relationship. Balance will be stored as an integer due to money being numerical (quantitative) and UserID, FirstName and Surname are strings for if a UserID was an integer then, for example, the UserID 0023 would be changed to just 23 which would cause an error in the software.
   UserID
   FirstName
   Surname
   Balance
     12
 
   Table 4 tbl_UserPhoto (example of what it looks like)
tbl_UserPhoto
14
Both UserID and GroupID are strings and have a one to one relationship as one UserID can only have one GroupID, the GroupID then can have multiple PhotoIDs assigned to it.
   UserID
   GroupID
      tbl_Products
    13
tbl_UserData
 tbl_UserPhoto
tbl_Photos
 The tbl_UserData table has its primary key which is the UserID, this UserID is assigned one single GroupID in the tbl_UserPhoto table. This GroupID is then assigned many PhotoIDs in the tbl_Photos table hence why the tbl_UserPhoto table has a one to many relationship with the table tbl_Photos. The table tbl_Products exists on its own and does not share keys with the other tables.
 
   Graphical User Interface (GUI) (3.2.2 C/D)
    GUI
   Setup Screen
Top-up/Balance Screen
Checkout Screen
 Allow Customer to login and make a purchase
 Allow User to check and add to their balance
    Add Product Screen
 Add User Screen
The GUI is important to the overall software as it makes the software interactive and provides an abstracted view of the code created to make it functional so that the user can look straight at the software and know how to use it whilst the software looks visually attractive to use.
As stated in the success criteria, “The GUI must be easy to understand and use”. Each and every part of my GUI will therefore be simplistic and straight to the point to allow the user to understand what to do upon using the software.
In the following parts of this document I will show examples of each of the screens shown above and then below each example will describe the usability features of each screen.
14
 
     Abstracted Setup Screen Example
    Would you like to?
Add new Start Add new
   Product
Program User
Setup Screen
   Button that links to Add Product screen
Button that links to the main checkout screen
Button that links to Add User screen
   This abstracted view of my setup screen is good because it is very simplistic and easy to recognise how to use it without complicated instructions. This is great as it meets one of my setup criteria “The GUI must be easy to understand and use” (Page 8). It is simple to understand and use as it only has two large buttons on the page which clearly state what they do as well as text that clearly states the name of the page along with clearly hinting at what the buttons will do.
When one of the buttons are clicked the user will be branched to the corresponding page associated with that button.
15
Plain text in a box
 
   Abstracted Add Product Screen Example
 5
6 1
Name: Barcode: Cost:
  Back
Add Product Screen
2
  Example Product
 901257591279
3
    £ 3.99 Description:
4
Scan ?cod e:
5
  An example of a product’s description and what it might contain
 Submit
 These will display text
3
4 5
6
1 2
 This is a text-input box that will allow the user to input information such as the product name, cost and a description.
 The scan button will allow the user to scan a barcode and the software will load the barcode into the input-text box to the right of it. This will save the user having to manually type out each barcode. If the camera is not working then the user can still manually type out the barcode.
 This is a text-input box that will only allow the user to add numerical values and will reject any non-numerical data that is put into it.
 This is the submit button, one all the data above has been entered the button is pressed, it will then run an algorithm that will verify that the data that has been entered is correct, for example it will check that the value entered for the cost is numerical and positive. If it returns ‘True’ (hence the information is correct) then it will add the new product to the tbl_Products table.
 16
This is the back button, once pressed the user will be branched back to the setup screen.
 
   1 v
Abstracted Add User Screen Example
  Back
Webcam Output
1
First name: Surname:
2
Photo:
Submit
  Jeff
 Smithers
    Take Photo
3
  Remember to look straight at the camera and ensure your entire face is in the frame when taking your photo!
4
 This will be a constant output of the webcam’s output ideally showing the user that is currently being added. This will also help them look at the camera ready for their photo by adjusting the hint box in [4].
 2 The take photo button will take a photo using the webcam. v
3 v
 The submit button will verify that data has been entered correctly. It will verify that the image has been taken correctly by firstly checking that A) there is at least one face in the frame that can be recognised and B) that there is no more than 1 face in the frame. Once verified will then add all the data to tbl_UserData and the photo that was taken to tbl_Photo linked to their userID that was generated automatically.
17
 
    This is static text that will be used as a hint to the user to let them know various information in the form of a prompt such as the example that is stated below:
“Remember to look straight at the camera when taking your photo!
“
  18
4
 
    1
2
3
4
Abstracted Top-Up/Balance Screen Example
  1
First name:
Surname:
Top-Up/Balance Screen
2
Search User
  Jeff
 Smithers
   Welcome Jeff, Balance: £12.32
 Purchase History:
4
0
Pay
3
 Add more?
  30/09 – TOPUP (+£10.00)
 01/10 – Yogurt (-£0.60) 03/10 – Coffee (-£1.50) 03/10 – Sweets (-£1.00)
 06/10 – Orange (FREE)
Checkout Screen Example 07/10 – Bacon Sandwich (-£2.50)
 –
Amount: £
 10.0
  Abstracted
08/10 Apple (FREE)
This will be a combination of static text and text-input boxes that will be linked to the purple button on the right.
 This button will allow the user to search through the database of users and retrieve an individual user’s balance & purchase history.
 Once a user’s records have been retrieved, this box will load in their purchase history and the corresponding balance for each payment, it will be green for a top-up, and red for any minus payment. The colouring will be to help meet my success criteria “The GUI must be easy to understand and use”.
 This will allow the user to input an amount to top-up into their account and then make a payment (as this software will not actually be used the pay button will simply just add the amount specified and not ask for a real payment).
19
 
      This will be a constant output of the webcam’s output ideally showing the user that is currently being added. This will also help them look at the camera ready for their photo.
1
2
3 4
4
5
 Once a face has been recognised the user’s information will be accessed in the User Data table and will load in their username, balance & purchase history.
  This will update as soon as the user has made a purchase allowing the user to see their last 3 purchases, this is useful as the user can see if they have purchased the correct item and see what their balance has been spent on. Once a user’s records have been retrieved, this box will load in their purchase history and the corresponding balance for each payment, it will be
        green
for any minus payment. The colouring will be to use”.
for a top-up, and
help meet my success criteria “The GUI must be easy to understand and
red
     This will be a dynamically updating text hint box that will update depending on the situation, for example, if there are more than one faces in the webcam output it will display “Please ensure only one face is present in the camera to make your purchase!”. This will be used to display messages to the user whenever necessary to prompt them to do certain things required by the software.
 20
  4 1
Balance £12.99
  Webcam Output
5
Last 3 Purchases
02/10 BLT Sandwich (- £1.10)
04/10 Chips (-£0.99) 09/10 Yogurt (-£0.80)
3
4
   Make sure you show your face & the barcode clearly in the camera!
Welcome
Ben Tindal
2
  
   Coding
     Key Variables (3.2.2 D)
Here I will showcase some of the key variables for my software, I will state what they are called, what data type they are and how they help the software to function.
Main Variables
Name: Data Type: ndarray (from ‘numpy’ library) face_encoding
       The variable ‘face_encoding’ will hold the face encodings of each user, it will be a local variable as it is only needed temporarily as each one is loaded up into the memory. The data here will be stored as an ‘ndarray’ which is a composite data type from the library ‘numpy’ which allows for complex mathematical manipulation of data. The data type ndarray is a “multi-dimensional container of items of the same specified data type and size”. It is useful to store face encodings as this type as it will contain a fixed size set of numbers (6) in a string around a hundred times to generate encodings for each part of the face, the generation of the encoding will be handled by a facial recognition library that will be imported over.
(End quote taken from https://docs.scipy.org/doc/numpy- 1.13.0/reference/arrays.ndarray.html).
 21
Variables
Coding
 Functions/Procedures
Classes
 
     Name: userdata Data Type: record (although implemented in python using a class)
     The variable ‘userdata’ will be a record consisting of information loaded from the tbl_UserData table. For each user, userdata will represent:
1. The first column, their first name.
2. The second column, their surname.
3. The third column... etc...
userdata
Table 1 - abstracted view of the record data type for the variable userdata
I will create the record in python making use of the class function. The pseudocode below shows how the data structure (shown in table 1) will be constructed.
Once the data structure has been created, values can be assigned through code like the code below:
The variable ‘userdata’ will be a global variable so that each user’s data can be accessed outside of the function so values will not have to be reassigned each time the function is run saving processor time. It will be stored as an array so that each bit of information can easily be accessed instead of using complex data locations e.g userdata[0][1][2].
A record is the ideal data type as it is immutable so therefore has a set size structure which is great as I will only need a set amount of fields in the record and each field (being a variable) can be whatever data type I want which is useful as balance is stored as a float whereas firstname is a string.
   Firstname (string)
   Surname (string)
   Balance (float)
    Userid (string)
  class userdatastructure:
firstname = (get from database) “Ben” as
string
surname = (get from database) “Tindal” as
string
balance = (get from database) 15.59 as float
userid = (get from database) “0” as string userdata = userdatastructure
 print(userdata.Firstname)
>> Ben
print(userdata.Balance)
>> 15.59
 22
 
   Other Key Variables
Variable Data Purpose Type
      whatScreen
      String
     Holds the name of the screen the program is currently running, allows the code to do certain functions depending on what screen is running. Changed when a new screen is switched to.
For example, if whatScreen is set to ‘main’ then the faceScan (the facial recognition algorithm) is run on each frame of the camera output.
   Example Below whatScreen = ‘Setup’
   known_face_encodings
     List of arrays
    Holds a list of ndarrays (Numpy Library’s version of an array) with each ndarray holding a unique user’s encoding so essentially known_face_encodings is a list of each user’s encodings.
By default this list of empty but once the loadUser algorithm is run on setup each user is accessed in the database and has its encodings individually added to this list.
When a face is found to match one of these encodings, the position of that encoding in this list is used in the list below to find the user’s ID, then that userID is fed into the other umbrella algorithms that make up the program.
   Example Below
known_face_encodings = [(‘12349, 124901, 12490’, etc...), (‘36112, 12516, 64211, etc...)]
 23
 
      known_face_names
      List of strings
     Similar to known_face_encodings but instead of holding encodings it holds each user’s ID in order of the encodings added to known_face encodings.
When a face is recognised it gets the location of the encoding, for example, third along in the list and accesses this list and finds the matching userID, this is what is fed into the other algorithms that make up the program.
   Example Below known_face_names = [“0”, “1”]
   delay
    Integer
   Delay holds the number of operations to complete before returning labels to default values. Defaults to 50.
This value is set to 50 whenever a face is recognised and the value begins to decrease when no face is recognised.
If less than or equal to 0 the values on the checkout screen will be returned to their default value of being blank and the loaded in user’s information will be wiped to prevent a transaction going through without them being there. This ensures the user has to constantly show their face in order to use the program thus increasing the security of the program by decreasing the number of false transactions.
   Example Below delay = [50]
    switchDelay
     Integer
   switchDelay holds the number of operations to complete before the camera output can be initialised on the checkout screen. (Defaults to 5).
This value is decreased as soon as the screen switches to the checkout screen (whatScreen = “Main”).
This is to prevent the program attempting to display the camera output before it has initialised which would result in an error.
 24
 
              Example Below switchDelay = [5]
   repeatDelay
     Integer
    repeatDelay holds the number of frames to complete before allowing a new purchase, without this delay a new transaction would go through in every single frame of the camera output, instead this adds a short delay ~1.5 seconds to prevent multiple purchases going through by mistake. Defaults to 30.
This value begins to decrease straight after a purchase has been made and is reset for each successive purchase has been made.
   Example Below repeatDelay = [25]
 25
 
   Key Stages & Outline of Development
My development will follow the Rapid Application Development (RAD) model which includes making lots of prototypes of the program, followed by evaluation and maintenance (if deemed not sufficient) of the program until has been completed. Each prototype will have increased functionality.
 START
 Stage 1 Stage 2
Stage 3
 Create Outlines of Screens Create Database
Add Camera into Checkout Screen
Implement Facial Recognition without use of database initially
 FIRST REVIEW OF PROGRESS
 Stage 4 Stage 5
Stage 6 Stage 7
 Load Database into the program for Facial Recognition
Add recognised users information into the checkout screen’s labels
Add the correctly delays
Implement Barcode recognition through products listed on the database
Create algorithm to allow the user to make transactions deducting the cost from their balance
 SECOND REVIEW OF PROGRESS
 Stage 8 Stage 9
Stage 10
 Allow the user to add new users on the add user screen
Allow the user to add new products on the add product screen
Add logging system in console to monitor the running of the program & test the program, fixing any resulting errors & ultimately fine tune the program so it is ready for the end-user.
 THIRD & FINAL REVIEW OF PROGRESS
 FINISH
To do this, I outlined 10 key stages of my development with three reviews where I will test and evaluate the program, if deemed sufficient I will continue, if not I will modify/improve it and repeat the review process again until ready to continue.
The reviews were place at each stage as they followed a significant step of a function of the program being completed.
First review is after the program visually has had the GUI finished and can recognise a face.
26
 
   The second review is after all the database information has been implemented within the program and can correctly recognise users on it along with products allowing the user to make transactions using the software.
The third and final review stage is after the ability to add new users and products within the program.
The process of testing each stage will be outlined below.
Testing my Software
Testing an individual Algorithm “load_user(id)”
To test the algorithm “load_user (id)” I will be inputting various values as the id to see if the program handles it correctly, currently, the algorithm above will only handle errors for non-numerical data, not extreme or erroneous numerical IDs so I will expect the program to halt unless further data validation is added when the software is developed.
Test Table for “load_user(id)” where id is the variable being changed.
     Type of Data
    Example Data
    Ideal response
    Expected Response if implemented like the code above
    How does the code need to be adapted to prevent this occurring?
   Extreme
 ‘Dog’ ‘Cat’ ‘m61c’
 Program captures the TypeError and responds with a print statement stating that the ID must be a valid numerical ID.
 Error – program will crash with a TypeError as the ID needs to be a number.
 ID needs to be attempted to be converted to an integer, if this returns an error, capture the error and output a print statement, if the ID can be converted to an integer then the ID is numerical and should be processed appropriately.
    Normal
    ‘1’ ‘0’ ‘5’
    Loads the appropriate user’s information as these IDs are valid.
    Success – program should work correctly as the data is valid.
       Erroneous
  -983517 1023481
  Program realises that the ID is less than 0 or higher than the maximum ID on the database so prints an error statement suggesting that the ID value is invalid.
  Error – program will crash as the IDs do not exist, ID cannot also be negative, only positive IDs exist.
  When the algorithm is run the ID must be checked to see if it is greater than 0 but less than the maximum id (equal to the number of users on the database), if the value of ID is the the program can proceed, else, the program must return a printed error statement.
 27
 
   28
 
   How will I test my program at each review stage?
Each review will require testing to ensure that the program functions correctly and can handle the test data outlined before.
   Review Number
   What Stages need to be reviewed?
   How will these stages be tested?
If all answers to the questions are yes then I will be ready to move on to the next stage of development.
    Review 1
   Stage 1 Stage 2 Stage 3
   - Navigate between the screens, do they navigate smoothly and direct the user to the correct screens?
- Does the database prevent incorrect data being added, does it save/function correctly?
- Does the camera initialise correctly and display smoothly?
- Does the facial recognition algorithm recognise a test user correctly?
   Review 2
 Stage 4 Stage 5 Stage 6 Stage 7
 - Does the algorithm load every user into the correct variables without fail?
- Can the facial recognition algorithm correctly recognise users from the database?
- Can it display the user’s information from the database in the correct format?
- Do the added delays function correctly?
- Can the program correctly recognise and
extract information from barcodes?
- Can the program look up a barcode’s
information in the database and retrieve the appropriate data from it if it finds a match?
- Can the user make a transaction with their face and a valid barcode?
- Does the program correctly deduct the correct amount from a user’s balance when a transaction is made?
- Are all changes saved correctly to the database without fail?
  Review 3
   Stage 8 Stage 9 Stage 10
   - Can the software prevent the following new users from being added:
 29
 
               i) If the First Name and/or Surname text box is blank
ii) If a photo has not been taken
iii) If the First Name & Surname is
not unique to the database
(already exists)
- Can the software add a new user onto
the database and save the changes?
- Can the software prevent the following
new products from being added?
i) If the Product Name,
Description, Cost and/or Barcode
Number text box is blank
ii) If a barcode has not been
scanned in (so the value is blank)
iii) If the Barcode Number is not
unique to the database (already
exists)
- Can the software add a new product
onto the database and save the
changes?
- Does the software refresh the loaded
faces every time a new user is added so
that they can be recognised?
- Does the software output a log of all
interactions the user has with the software so that any errors/problems with the software can be solved?
 30
 
   Outline of Key Algorithms
Purpose of Psuedocode Example Algorithm
      To charge the user for a transaction
    Function charge(userid, amount)
// UserID of user to make the transaction, amount being the cost of item the user is attempting to buy
Open new connection to the database if closed
Get balance of the User with the ID passed to this function (userid) Round the balance to two decimal places using the inbuilt python function If balance minus amount is greater than or equal to 0:
// User has enough money
User’s balance updated to its previous value minus the cost of the item Save changes to the database
Close database connection
return True // Successful transaction Else if balance minus amount is less than 0
// User does not have enough money
Close database connection return False // Failed Transaction
      Why is this algorithm needed? (Charge algorithm)
This algorithm will allow the program to charge the user for a product, it is the algorithm that decides whether or whether not a transaction should go through. Without this algorithm, transactions could be allowed to go through regardless of whether the user has enough money in their balance for the product. This algorithm is called through the buyProduct algorithm, if this algorithm returns True then the buyProduct algorithm will go ahead with the transaction and will stop it if it returns False.
    To allow the user to start a transaction
    Procedure buyProduct(product) // Product is an array of the database rows
If there is a user and product both loaded in the variables together:
if product’s cost > 0:
Set local variable ‘term’ to “+ £” in the colour green
if product’s cost <= 0:
Set local variable ‘term’ to “- £” in the colour red
if charge(current loaded user’s ID, currently loaded product) is True: // Calls the charge function, if it returns True then branches
Update past purchases label to show newly bought products cost with
the local variable term as a prefix to it along with its colour. else:
inform the user that the transaction was not successful
    Why is this algorithm needed? (buyProduct algorithm)
This algorithm calls the charge algorithm, if it returns True then it is in charge of updating all of the labels to display the correct information, if it returns False then the algorithm will display text to inform the user that the transaction was not successful. This algorithm is called by the barcodeLookup algorithm whenever a product match is found.
 31
 
       Allow the software to lookup a scanned barcode in the database
    Procedure barcodeLookup(decodedObjects) // passed list of raw scanned barcode data get global variables last barcode scanned, product, repeatDelay
for object in decodedObjects: // runs through each barcode located
raw_barcode = obj.data
raw_barcode = string raw_barcode
// set local variable raw_barcode to be the raw data of that scanned barcode // this looks like b’123456789’ so needs to be cleaned
raw_barcode = raw_barcode.substring[2:raw_barcode.length - 1] // now this variable will just be the set of numbers ‘123456789’
if repeatDelay <= 0: repeatDelay = 25 last_barcode = “”
// Resets last_barcode & repeatDelay to allow the same barcode to be scanned again if raw_barcode is not last scanned barcode: // Begin looking up of barcode
last_barcode = raw_barcode
// Update last barcode so that this barcode will not be repeatedly looked up
Open database cursor
execute SQL statement (“SELECT * FROM tbl_Products WHERE BarcodeNumber = raw_barcode”):
Product = retrieved product // Set the global variable Product to be this retrieved product if found
buyProduct(Product) // Run the procedure buyProduct passing the Product to it
           Why is this algorithm needed? (barcodeLookup algorithm)
This algorithm is key to linking the program to the database. This algorithm looks up raw barcode data by firstly formatting the barcode data then executing an SQL command to search for a match in the database. It also handles the delays between searching for barcodes to prevent a barcode being repeatedly scanned in every frame of the camera output, if it finds a match then the algorithm runs the buyProduct algorithm with that matched product.
 32
 
   Algorithm to load Facial Data from the Database
Function load_user(id)
The below algorithm showcases how the software will load each user’s information into the record userdata where it can be used later in the program. Starting with the data structure for the record (created using a class as that is how it is made in python).
 class userdatastructure(first, sur, bal, uid): firstname = first as string
surname = sur as string
balance = bal as float
userid = uid as string userdata = ‘empty’
def load_user(id):
try: int(id)
global userdata
for column in tbl_UserData.executeSql(“SELECT * WHERE UserID =”, id, “ FROM tbl_UserData”): userdata = userdatastructure(column[0], column[1], column[2], column[3])
except TypeError:
print(“UserID must be a numerical ID, cannot contain letters”)
-----------------------------------------------------------------------------------------------------------------------
   load_user(0) userdata.firstname >> Ben userdata.balance >> 15.59 load_user(1) userdata.firstname >> Jeff
The class above sets out the structure of the record’s fields including the name and data type of each.
The function load_user(id) first opens into a ‘try’ function that will capture any errors which can be handled in the except function below, the use of this is necessary as it prevents the program from quitting and allows the error to be processed later on. E.g algorithm attempts to turn the variable ‘id’ into an integer, if the data is erroneous like contains any non-numerical data then the algorithm will return an error which will be captured in the ‘except TypeError’ function which will print the statement “UserID must be a numerical ID, cannot contain letters” and the program will not be halted.
The for loop will assign each column of data from the database table to the array column which the consequently assigns them to the userdata record.
    Here I demonstrate some real time use of this algorithm:
load_user(0)
Causes UserID 0’s information to be loaded up into the record userdata where it can be accessed.
userdata.balance & userdata.firstname
Accesses the record userdata which houses userid 0’s information and retrieves the variable floating point number balance & string firstname which are Ben & 15.59 respectively.
load_user(1)
Replaces UserID 0’s information with UserID 1’s information which is loaded up into the record userdata where it can be accessed.
userdata.firstname
Accesses the record userdata which houses userid 1’s information and retrieves the string firstname which is now Jeff
33
 
   Validation
Why is Data Validation Needed?
Data validation is required so that only data that is wanted is allowed in the program, for example data that meets set criteria such as is numerical. If incorrectly formatted data is used then the program will be unable to handle it resulting in errors and potentially cause the program to ‘crash’, therefore it is important that all the data is regulated.
Validating User Inputs
Most of the user inputs will be validated by the GUI itself, the lack of text entry for the majority of the program prevents the user from being able to input their own data. The user is limited to being able to interact with the buttons (to navigate the GUI) and interact with the camera (by showing their face and barcodes to the camera), because of this little validation is needed for the main function of the program (the checkout system) and only for the ‘add user’ and ‘add product’ pages.
Input Type Why it needs to be How will it be validated? validated
       Button
(for window navigation)
    Needs to navigate the user to the correct screen, otherwise the user will not be able to navigate the program preventing the user from evening accessing parts of the program.
    A button in Tkinter already strongly limits what the user can do, the user only has the choice of either pressing the button, or not so there is no risk of sending incorrect data when navigating the pages. The button only needs to be tested to see if it navigates to the correct page.
   Webcam Output (on the checkout screen)
  The webcam has two states it can be in once running, it can either recognise a face or not recognise a face. Once a face is recognised the data that is retrieved needs to be correctly validated and meet the criteria for each type (for example, money retrieved from the database must be rounded to 2 decimal places, numerical and put into the form £XX.YY)
  The camera output is already strongly validated as the user is strongly limited as to what they can do, the act of the data being retrieved from the database once the webcam has recognised a face will need to be validated as mentioned previously with money along with other factors. The act of making a purchase with the program will similarly need to be validated to only permit a transaction going through if a face has been recognised along with a valid barcode within X amount of time of each other, each transaction must only go through once so a set delay must be added.
 34
 
       Text Boxes
(for adding users or products)
     A text box needs to be validated as it allows the user to input any text they wish, not all inputs put in here are correct and thus need to be validated to ensure they meet given criteria.
    When adding a new user,
- the input of a First Name and Surname, must both together be looked up in the database so see if it is unique, if it is then the data meets the validation, if not then it must be rejected and a suitable message must be shown stating that this record already exists in the database.
- It must be checked that none of the text boxes should be left empty.
   When adding a new product,
- The Name textbox must be unique, cannot be blank
- The barcode textbox must be unique and has to be scanned in via the program.
- Cost must be numerical, cannot be text
- Description does not need validation, ideally should be a short sentence of text
    Button
(for submitting the data form for a new user or product)
    As mentioned on the previous button, the button in Tkinter limits the user’s actions to either pressing the button or not. However, upon press the button on the add user or product screens it will run the validation on the previous text boxes together as a form.
    Once pressed the button will check the following:
- That each of the previous text boxes are not empty
- That each box meets the data type it should be e.g Cost must be numerical
- That each text box that needs to be is
unique e.g BarcodeNumber MUST be unique and so must the combination of a First Name and Surname.
 Validating my Database
It was important that I designed my database along with the program to ensure that the database meets the ACID rules (Atomicity, Consistency, Isolation and Durability) to prevent any incorrect usage of the database.
Atomicity means ensuring either all the transactions go through or none at all and Consistency means either a transaction completes or the previous state is returned (no changes will be made). To ensure my database complies with these rules, I will make changes to the database by modifying a cached version of the database (stored as a .journal file by the SQLite library) and once all the transactions have completed I will attempt to commit (save) this modified database over the original, this will either result in a success (the file has been updated) or will fail meaning the
35
 
   original file will remain the same, only the cached file that was not saved had been updated. This will ensure that no partially completed jobs will go through.
Isolation means that transactions are done in isolation from each other, to ensure this my program will open the database and lock it to a read-only state whilst it is being used to prevent any other programs accessing the database, once the transaction(s) has/have been completed the software will then save and release the database back into a read/write state. This will ensure that those transactions will be carried out in isolation by my software. For example, whilst completing a transaction, the whole database will be locked and the records for that user will be updated and once completed the database will be released, this will also aid the Atomicity and Consistency of the database.
Durability means that committed data would not be lost, even after power failure. To ensure this I made sure that the cached database file that is created then the software is ran is saved on non-volatile (will not be lost when power is disconnected) storage which in this case is the hard drive of my computer and not its memory which is volatile (will remain permanently saved until deleted, not lost when power is disconnected) so that if the event of a power failure or crash the cached database will remain saved and can be committed at a later date, for example, when power is restored.
36
 
   What Test Data will be used to develop the Program?
What is the test data Test Data itself for?
      UserData Table, will contain 2 unique Users so that the program can be tested.
      First User (myself):
ID FirstName Surname Balance 1 Ben Tindal £40
          Second User:
ID FirstName Surname Balance 2 Will Coleman £30
            Justification for this test data
I have chosen two users to be used so that the program can be tested if it can distinguish between the two users.
The number of users will be increased once the ‘add user’ procedure has been created so that the procedure can be tested.
   Photos Table, will contain a photo for each of the Users on the software.
    First User (myself): PhotoID UserID 11234.jpg 1
11234.jpg – A photo centred on the user’s face
        Second User: PhotoID UserID 56312.jpg 2
11234.jpg – A photo centred on the user’s face
       Justification for this test data
The number of users will be increased once the ‘add user’ procedure has been created so that the procedure can be tested later in post-development, initially only two users will be used so that the program can be tested for function, thorough testing will occur in post-development testing.
  Products Table, will contain 3 unique products, this will be expanded once the ‘add product’ procedure has been created so that the procedure can be tested.
        BarcodeNumber Title Cost Description
2125125631 Orange £0.60 an orange
           BarcodeNumber Title Cost Description
5374135331 Gum £2.00 Mint chewing gum
          BarcodeNumber Title Cost Description 6315135122 Apple £0.50 an apple
       Justification for this test data
This will contain 3 unique products; this will be expanded once the ‘add product’ procedure has been created so that the procedure can be stress-tested in post-
 37
 
    development testing, initially only three products will be used to test the program for function, more thorough testing will occur in post-development testing after the iterative development phase.
This test data is necessary so the program can be tested on an actual functional data set to see if it would work in the real world. The program will be used by an actual user using the camera of my laptop rather than doing it on static images, if the program were to be purely tested on digital static images then it would not be realistic of the real world were the lighting would not be perfect/the face may be slanted or at an angle.
What Post-Development Test Data will be Used?
What will my post-development testing consist of?
My post-development testing will consist of three tests. Firstly, there will be a test of 10 users to see if each can be recognised and then 5 different products (under a variety of types) and then finally I will test the usability of my program by allowing users to use the program and carry out some set tasks to see how they handle them.
What Test Data will be used?
My post-development test data will be a larger version of test data outlined earlier. Originally, I decided that the test data will contain 10 different users including fellow students and members of my household, however, due to current issues (Coronavirus) I will have to use 10 different faces found on the internet (shown below) as I do not have access to 10 different people.
Justification for that test data?
I will need to test 10 different users as this will allow me to truly test the program if it can distinguish a considerable number of people without fail. This will also test the program to see if it can handle 10 different encodings all at once without dramatically slowing down the computer.
  38
 
   What Test Data will be used?
I will also have a variety of products to test my program with, this will contain 5 different products including various household items I have around my house.
The products that will be tested are as follows:
- Two Xbox One games (with barcode on back), one that is on the database and one that is not
- Can of Drink (barcode on back)
- Barcode off of phone’s screen
- Random barcode not on the database from phone’s screen
Justification for that test data?
The two barcodes off of my phone’s screen will act as a barcode in perfect lighting to compare the results of the other products to as the lit-up barcode on the screen will have the perfect lighting conditions for the program to scan it with.
An Xbox game case will be used as it represents a common object that contains a barcode that will be scanned in in normal lighting conditions. Items like this will be the most commonly scanned in item on the program. I have chosen one that is on the database as it will see whether the software can recognise it and secondly check whether its on the database, the second Xbox game that is not on the database will allow the program to realise that the item is not on the database and not allow a transaction to go through.
The can of drink with a barcode on the back represents another common object that will scanned in using normal lighting conditions.
   39
 
   Developing the Program
Stages of Development
My iterative development will roughly follow the stages outlined below.
  START
 Stage 1 Stage 2
Stage 3
 Create Outlines of Screens Create Database
Add Camera into Checkout Screen & Implement Facial Recognition without use of database
 FIRST REVIEW OF PROGRESS
 Stage 4 Stage 5
Stage 6 Stage 7
 Load Database into the program for Facial Recognition
Add recognised users information into the checkout screen’s labels
Implement Barcode recognition through products listed on the database
Create algorithm to allow the user to make transactions deducting the cost from their balance
 SECOND REVIEW OF PROGRESS
 Stage 8 Stage 9
Stage 10
 Allow the user to add new users on the add user screen
Allow the user to add new products on the add product screen
Add logging system in console to monitor the running of the program
 THIRD & FINAL REVIEW OF PROGRESS
 FINISH
At each review stage a series of tests must be conducted to check that the stages function correctly.
I will also be sure to link each stage back to the analysis section at the review sections.
40
 
   At each review stage I will conduct the following tests:
   Review Number
   What Stages need to be reviewed?
   How will these stages be tested?
If all answers to the questions are yes then I will be ready to move on to the next stage of development.
    Review 1
   Stage 1 Stage 2 Stage 3
   - Navigate between the screens, do they navigate smoothly and direct the user to the correct screens?
- Does the database prevent incorrect data being added, does it save/function correctly?
- Does the camera initialise correctly and display smoothly?
- Does the facial recognition algorithm recognise a test user correctly?
   Review 2
 Stage 4 Stage 5 Stage 6 Stage 7
 - Does the algorithm load every user into the correct variables without fail?
- Can the facial recognition algorithm correctly recognise users from the database?
- Can it display the user’s information from the database in the correct format?
- Do the added delays function correctly?
- Can the program correctly recognise and
extract information from barcodes?
- Can the program look up a barcode’s
information in the database and retrieve the appropriate data from it if it finds a match?
- Can the user make a transaction with their face and a valid barcode?
- Does the program correctly deduct the correct amount from a user’s balance when a transaction is made?
- Are all changes saved correctly to the database without fail?
    Review 3
    Stage 8 Stage 9 Stage 10
    - Can the software prevent the following new users from being added:
iv) If the First Name and/or
Surname text box is blank
v) If a photo has not been taken
 41
 
               vi) If the First Name & Surname is not unique to the database
(already exists)
- Can the software add a new user onto
the database and save the changes?
- Can the software prevent the following
new products from being added?
iv) If the Product Name,
Description, Cost and/or Barcode
Number text box is blank
v) If a barcode has not been
scanned in (so the value is blank)
vi) If the Barcode Number is not
unique to the database (already
exists)
- Can the software add a new product
onto the database and save the
changes?
- Does the software refresh the loaded
faces every time a new user is added so
that they can be recognised?
- Does the software output a log of all
interactions the user has with the software so that any errors/problems with the software can be solved?
 42
 
   Stage 1 - Designing the Setup Screen
Firstly, I began by designing each of the screens that will act as the graphical user interface for my program.
The Setup Screen
Each screen will be coded using a built-in library to Python called Tkinter. Initially I had issues with creating the layout through ‘packing’, a method taught by my school, as it proved inefficient as I had to repeat large amounts of code stating where it should locate itself on the GUI. After a quick bit of research, I decided that Labels and buttons will be inserted onto the screen in the form of a grid making use of the ‘grid’ function on tkinter where the GUI is split up into columns and rows.
Column Column Column
        01
Row
1
Row
2
Row
3
2
   Row 0
         The image above shows how the setup screen has been divided up into a grid with the main contents of the screen being in the central column (column 1). You can see that the “Start Program” button has been mapped into Column 1, Row 1 and has been moved to the middle top of that box (in tkinter we do this by inserting a “sticky” flag start_button.configure(sticky=N). This has similarly been done for the other two buttons.
43
 
   After quickly mapping out all of the labels and buttons I came out with a rough screen that looked like the one I had designed previously. As I had not yet created another screen or the algorithm to go to that screen, I set the buttons to run a ‘test’ function that would print “Test function called” so that I could test the screen to see if it was working.
 Upon clicking each button, the python console outputted the following:
There were no errors outputted and the buttons each ran the test procedure cleanly without any issues, so I labelled the test a success.
 44
 
    Figure 36 – first prototype code of the setup screen
I first created the code shown above in figure 36, however, I decide that when creating more screens the code here would look messy, and if I wanted to re-call this page again I would have to rewrite out the code again so I decided to change it all into a class where the code here is reusable (Thinking Ahead).
 45
 
    Figure 47 – Final code for the setup screen
Now the code is all neatly contained within a class, I assigned the code that creates all the buttons and labels to be initialised with the class and assigned two procedures to add functionality into the screen, the loop variable is just a simplified self.window.mainloop expression that can be called simply by self.loop() where self is the name of the class. The procedure self.destroy() will change the variable is_wanted to False which will end a while self.is_wanted is True loop which will contain the mainloop of the screen. Because the code is within a class, the code above acts like a template for creating the screen. Whenever the screen needs to be used, the class can be called by assigning a variable to it e.g current_screen = setup_Screen() where the screen itself will then be initialised along with its appropriate procedures.
I assigned the self.destroy() procedure to the second button for adding a new user just to check that the code was indeed working, upon pressing the button the screen closed with zero errors so I can conclude that the screen is indeed functional.
 46
 
   New Product & User Screen
These screens both followed a similar pattern to the previous screen, all the code for the screen was held within a single class with a destroy and loop function associated with it. Once I had created the add product screen, I simply copied across the other screen and renamed the title of it to add Users Screen, I would go back to this later in development and update it.
  47
 
   To switch between screens, I created the procedures by creating unique numbers for each screen I create:
Screen Screen Name What does switching to it do? Number
2 Add Product Screen - Releases previous screen and loads this screen
     1
   Setup Screen
   - Releases previous screen and loads this screen
     3
    Add User Screen
    - Releases previous screen and loads this screen
- Runs an algorithm that fetches the highest
used ID so that if a new user were to be added it would be assigned an unique ID (as UserID has a one to one relationship with the rest of the table).
   4
  Checkout Screen
  - Releases previous screen and loads this screen
- Starts a switchDelay of 5 operations of the faceScan procedure, this will prevent faces
being scanned prior to the camera loading up
which would result in an error.
- Returns User & Product variables their default
values so that all no purchases can be made using previous values that were assigned to these variables. (These variables hold the data of the user currently recognised along with the product that they desire to buy, if not cleared then a transaction could be incorrectly made).
- Leaving this screen also will release the camera, preventing it being used when not needed freeing up memory space and also preventing people being paranoid that a computer is ‘watching’ them without them knowing.
 48
 
   Step 2 - Creating the Database
Upon reflection of my earlier design, I decided to merge the tbl_Photos and tbl_UserPhoto tables together as it was simply overcomplicating the loading process for the software. Instead, one table can simply go through each record row by row and add each PhotoID directly to a UserID instead of a GroupID loading each photo for each UserID.
This SQL code would generate the tbl_Photos table with columns, PhotoID and UserID which are both text that cannot be empty and must be unique to the table. PhotoID was assigned as the Primary Key for this table so that the table can be indexed correctly.
This SQL code would generate the tbl_Products table with the following columns:
- BarcodeNumber that is stored as text, cannot be empty and is unique to that table.
- Title that is text and cannot be empty. Because it is unique it will also be assigned to be the Primary Key.
- Cost that is stored as a real number, cannot be empty and defaults to a value of 0.
- Description that is stored as text and cannot be empty.
The WITHOUT ROWID means that each record will not be automatically assigned an ID by the database and will instead use the Primary Key as the ID.
This SQL code would generate the tbl_UserData table creating the following columns:
- UserID would be stored as plain text, that cannot be empty and is unique to that table so will consequently be the Primary Key.
- FirstName would be similarly stored as plain text that cannot be left empty.
- Surname would also be stored as plain text that cannot be left empty.
- Balance will be stored as a real number that cannot be empty
The SQL command “WITHOUT ROWID” will also be used here the same as how it was used in the previous SQL command.
I then inserted the test data into the database, as shown in the following images.
 CREATE TABLE "tbl_Photos" ( "PhotoID" TEXT NOT NULL UNIQUE, "UserID" TEXT NOT NULL UNIQUE,
PRIMARY KEY("PhotoID") )
 CREATE TABLE "tbl_Products" ( "BarcodeNumber" TEXT NOT NULL UNIQUE,
"Title" TEXT NOT NULL, "Cost" REAL NOT NULL DEFAULT 0, "Description" TEXT NOT NULL, PRIMARY KEY("BarcodeNumber")
) WITHOUT ROWID
 CREATE TABLE "tbl_UserData" ( "UserID" TEXT NOT NULL UNIQUE,
"FirstName" TEXT NOT NULL, "Surname" TEXT NOT NULL, "Balance" REAL NOT NULL, PRIMARY KEY("UserID")
) WITHOUT ROWID
49
 
      50
 
   Step 3 - Adding Camera & Implementing Facial Recognition
Setting up the Camera Module
To insert the camera output into the checkout screen window, I needed to create a ‘canvas’ object in Tkinter and assign a static image to it. This static image would be updated for every frame that the camera records making it look like a live camera feed.
To get the camera output I had to design a class that would constantly refresh the image and run the facial recognition on it.
After experimenting with the class, I came up with the following code.
 The code essentially means, on initialisation of the class, the class will generate the variables:
vid – the video capture itself
width – the width of the camera output
height – the height of the camera output
The function get_frame attached to the class will retrieve a static image of the current camera output and return it, this returned value will be important when it comes to adding this into the class of the screen.
Next, I moved onto the checkout screen and inserted the following:
51
 
    This would add a canvas which would lately house the camera output and added labels to the screen that would act as housing for the data retrieved from the database
These values would be set to the default values shown above. I then had to insert the following into the screen. Including an update function that would repeatedly call itself once the screen was ran with a delay of 1ms and would get the image frame from the class CameraOutput and insert the image into the canvas object.
  52
 
    This is what the screen looked like when first run. The labels on the right showed correctly however the image canvas did not displaying on the top right of the image. I decide to change the colour schemes and change the size of the labels to be larger after reflecting on the abstracted screens I designed earlier, and I managed to get the screen to function correctly with it now looking more visually appealing.
 53
 
   Implementing Facial Recognition to the Camera Module
Now it was time to add the facial recognition part of the program in, firstly I needed to locate a time in my program where the image was first generated, this was in the CameraOutput class. I inserted the line “faceScan(frame)” into the get_frame function. Now it was time to design the faceScan(xxx) function.
The library face_recognition would be used for this section which handles taking an image and translating it into an encoding format where I can manually compare these values as decide whether a face matches another or not.
Before coding the face_Scan function I quickly implemented some test data in so I could test the procedure before implementing the database into it.
known_face_encodings.append(face_encoding)
After implementing the lines above the program would now load the image “testimage.jpg” into the program and encode it and store this encodings in the variable known_face_encodings where the faceScan procedure can compare other encodings to it.
Firstly, the faceScan procedure would have to resize the image to a quarter of the original image size, this is because the library can still recognise the fact but save a quarter of the processing power needed to scan through the entirety of the original image thus saving processing time and power. Next, the library will run its built-in function on the image to extract all the locations of faces in the image. If more than one face is detected, then the function will stop and will not go any further as only one person can use the program at any given time. Next the program will encode the located face.
Now the program will need to do a variety of checks, if there are no face encodings generated, the program will return the labels to their default parameters.
 known_face_encodings = []
known_face_names = [“Test User”]
user_image = face_recognition.load_image_file("testimage.jpg) face_encoding = face_recognition.face_encodings(user_image)
    54
 
   Next up I created a loop that would go through each of the face encodings found and would compare each one to the list of face encodings that are stored in the list known_face_encodings that for now just contains one encoding that is of me so that I can test the algorithm before implementing full database usage, if it finds a match it will save the location of that face, if the loop finds more than one match (due to an error?) it will get the most likely match (handled by the library).
Now the algorithm will look at the most likely match, get the name of the match and will adjust the labels on the screen as appropriate, for now only the name is known so the name will be updated.
  55
 
   Review 1 - Testing of Stages 1 to 3
Analysis Problem Breakdown Link
First of all, I will look back at the breakdown of the problem in my analysis.
Justification of How I Solved the Problems
In the “Why is this suited to a computational solution?” section I stated that I would make use of abstraction in the form of a GUI so that the program is simple to use, I have met this by creating an interface for my program using Tkinter in Python.
I also stated that I would make use of an SQL database that only a computational solution could use. In stages 1-3 I setup this database and will integrate it within my program later on in the iterative development.
Decomposition of this problem has been attained by splitting the problem down into the 10 stages for my development of which I am working through now.
Testing
Now I have finished the first three of my stages I will look back at the testing I came up with for my software.
 Review What Stages need How will these stages be tested?
 Number to be reviewed?
If all answers to the questions are yes then I will be ready to move on to the next stage of development.
 Review 1
 Stage 1 Stage 2 Stage 3
- Navigate between the screens, do they navigate smoothly and direct the user to the correct screens?
- Does the database prevent incorrect data being added, does it save/function correctly?
- Does the camera initialise correctly and display smoothly?
- Does the facial recognition algorithm recognise a test user correctly?
“Navigate between the screens, do they navigate smoothly and direct the user to the correct screens?”
The screens navigate smoothly and direct the user to the correct screen; however, I was not happy with the fact that every time I changed screen, the new screen would open up slightly to the right and would continue to move slightly right every time. To fix this, I added a location flag to each of the screens so that they would snap to the top right of the computer screen.
56
 
   This involved the line below being added to each of the screens, setting the dimensions of the window and secondly snapping it to the coordinate (0, 0) of the screen (Top right).
self.window.geometry('1024x612+0+0')
 57
 
   “Does the database prevent incorrect data being added, does it save/function correctly?”
I attempted to input the following into the database:
   Input
Expected Outcome
Actual Outcome
  Blank input
   Rejected, cannot be blank
   Was rejected, success
   Non-numerical data inputted for cost and balance
“awrh”
 Rejected, data must be numerical
 Was rejected, success
    String entered for name and surname
“Ben”, “Tindal”
    Accepted, name and surname should both be strings
    Data was accepted and allowed to save into the database
 A repeated barcodenumber was inputted
Rejected, barcodenumber must be unique
Was rejected, success
   “Does the camera initialise correctly and display smoothly?”
For the most part the camera would initialise correctly, however occasionally it would crash upon loading up, this was due to the program attempting to recognise a face before the camera had fully loaded.
To fix this I created a variable named switchDelay which would be used to delay the running of the faceScan algorithm whilst the camera initialises.
To implement it I set the variable switchDelay to be set to equal 5 every time the screen is switched to the checkout screen, this would then be decremented by 1 for each frame of the camera whilst it is greater than 1, when this delay is less than or equal to 0 the faceScan algorithm can be ran.
Now it was implemented the program opened the checkout screen smoothly and correctly without errors.
58
 
   “Does the facial recognition algorithm recognise a test user correctly?”
To test this, I used it on myself, the photo I added earlier was loaded into the program and this was the outcome.
 The test was a success, the program correctly recognised my face (image slightly blurred as censorship). Thus, the program managed to recognise a test user correctly.
59
 
   Summary of First Review and Testing
  Test Question
   Was the test a success?
   (if applicable)
Did the problem get fixed?
    Navigate between the screens, do they navigate smoothly and direct the user to the correct screens?
  Partial Success
   Success
     Does the database prevent incorrect data being added, does it save/function correctly?
  Success
    Does the camera initialise correctly and display smoothly?
   Partial Success
    Success
     Does the facial recognition algorithm recognise a test user correctly?
   Success
 60
 
   Stage 4 – Implementing Usage of Database for Facial Recognition
Creating the loadUser algorithm
To implement the database into my program I would first have to import sqlite3 which is a library that is built into Python.
I next have to connect to the database then create a pointer to it so I can send SQL commands to it.
Next I would have to create the loadUser(id) algorithm explained previously in my design section. This would open a database connection and send the SQL command:
'SELECT * FROM tbl_UserData WHERE UserID == id’
The command would then retrieve the information for a given user and set it to the list User where data can be retrieved from it when needed, it would go through each column and append it to the User list. For example, User[0] would retrieve the first column of the database result for that User. Once done the algorithm will then close the database connection to prevent any changes to it.
For example: loadUser(1) would load the following, [“1”, “Ben”, “Tindal”, “40.0”]
 database = sqlite3.connect('checkout_data.db') db = database.cursor()
  # Looks up the userID specified in the tbl_UserData table.
def loadUser(id):
global User
db = database.cursor()
for column in db.execute('SELECT * FROM tbl_UserData WHERE UserID ="{}"'.format(str(id))):
User = []
for i in range(len(column)):
User.append(column[i]) db.close()
61
 
   Creating the loadFaces Algorithm
First the algorithm will need to load the global variables known_face_encodings and known_face_names and reset them to be empty values. Next it will need to open a connection to the database and access the tbl_Photos.
The following SQL command will be executed:
'SELECT * FROM tbl_Photos'
This will retrieve all of the photos in the database table tbl_Photos, line by line in the
 form of a list where:
(Step 1)
Photo = [‘Photo Location’, ‘UserID’]
 Photo[0] the Photo Location, will be used to find the location of the image and convert it to encodings then append it into the known_face_encodings list.
(Step 2)
Secondly, Photo[1] the UserID that photo is of will be appended into the known_face_names list.
(Step 3)
This process will be repeated for all of the photos in the database.
Once completed, the algorithm will close the database to make it free for other parts of the program to access the database.
 def loadFaces(): # Algorithm to load faces into the program global known_face_encodings, known_face_names
# Create arrays of known face encodings and their names known_face_encodings = []
known_face_names = []
db = database.cursor()
for photo in db.execute('SELECT * FROM tbl_Photos'):
user_image = face_recognition.load_image_file("Photos/" + photo[0] + ".jpg") # get directory from db face_encoding = face_recognition.face_encodings(user_image)[0] known_face_encodings.append(face_encoding)
known_face_names.append(photo[1]) # UserID as name
db.close()
The load user algorithm will be ran upon initialising the program to populate the variables known_face_encodings and known_face_names.
62
 
   Stage 5 – Updating Screen Labels
Now the faceScan algorithm will have to be updated, the algorithm will already access the updated known_face_encodings and known_face_names variables so will simply need a way of recognising the UserID the program will output when a face is correctly recognised. This will make use of the loadUser(id) algorithm we created earlier.
Heading back to the faceScan algorithm, I visited the block of code that is executed once a match is found. I inserted the line loadUser(name) that will look up the UserID associated with the discovered face, now I have access to the list User of the face so the labels on the screen need to be updated, the name_label should hold both the FirstName and Surname of the user and the balance must be updated of the user.
As the past_purchases part of the program had not been designed yet I left a message to remind me later to add it.
 if matches[best_match_index]: # If match has been found:
name = known_face_names[best_match_index] # Looks up the name
loadUser(name)
current_screen.db_name_label.configure(text=User[1] + ' ' + User[2]) current_screen.db_balance_label.configure(text='£' + bal)
# Once past purchases have been created, edit the current_screen past purchase label here
63
 
   Step 6 – Implement Barcode Recognition of Products Listed on the Database
To implement Barcode Recognition into my program I had to make use of an external library called “pyzbar” which allowed me to input a frame into it and it would extract the raw data from that barcode in a string format. The diagram below visualises how the library handles an image (frame) of a barcode.
pyzbar.decode(frame)
Output: C”A1234567890A”
   64
 
   Creating the barcodeLookup Algorithm
Much of the algorithm was discussed earlier on in the design section so it will be summarised quickly.
Algorithm is fed the raw data from the scanned barcode, it checks whether the barcode is the same as the last scanned barcode, if they match then it will check if the delay is less than 0, if it is then the program will allow the barcode to be looked up (to prevent the barcode being looked up every single frame of the video) and then will look it up in the database via the SQL command:
'SELECT * FROM tbl_Products WHERE BarcodeNumber = Barcode‘
If a result is found, the delay will be reset (so the same barcode will not be looked up for a set period) and it will then append each line of the product into the list Product so that it will look like the following:
Product = [‘BarcodeNumber’, ‘Title’, ‘Cost’, ‘Description’]
If no match is found, then the algorithm will stop. The database connection will be closed at the end of the algorithm.
 # Takes scanned barcode data from image
def barcodeLookup(decodedObjects):
global last_barcode, Product, repeatDelay for obj in decodedObjects:
raw_barcode = obj.data if repeatDelay <= 0: repeatDelay = 25
last_barcode = ''
if raw_barcode != last_barcode: # Prevents 'spam' of checking
last_barcode = raw_barcode
raw_barcode = str(raw_barcode)
barcode = raw_barcode[2:len(raw_barcode) - 1]
# Now we have a new barcode, let’s look it up in the product table
db = database.cursor()
for column in db.execute('SELECT * FROM tbl_Products WHERE BarcodeNumber
="{}"'.format(str(barcode))): Product = column
#buyProduct(Product)
return
db.close()
else:
last_barcode = raw_barcode
65
 
   Inserting the Barcode Recognition into the Camera Output
The following lines were inserted into the end of the faceScan algorithm:
This will cause the pyzbar library to scan the current frame for any barcodes and will add them to the variable decodedObjects, if only 1 barcode is found then the variable decodedObjects will be passed to the algorithm barcodeLookup and will cause that barcode to then be looked up resulting (if there is a match) in the list Product to be updated to that product’s information from the database.
 decodedObjects = pyzbar.decode(frame) if len(decodedObjects) == 1:
barcodeLookup(decodedObjects)
66
 
   Step 7 - Create Algorithm to Allow the User to make Transactions Deducting the Cost from their Balance
buyProduct Algorithm
This algorithm was needed to make a purchase using the program. First the algorithm would check whether there was a valid product and user loaded in the program by checking the length of the two lists, if there is no product or user loaded in the list then the list will be empty and the algorithm will stop, if there is a product or user loaded then the list will have a length of 4 (one for each of the columns of the database table) and the algorithm will continue.
Next I wrote an algorithm to check whether the cost of the product was positive or negative so that it can be formatted (green for a positive amount, for example, a top- up, or red for a negative amount). Now the program will run the charge algorithm (yet to be coded but will return a True or False value depending on whether the transaction was allowed to go through):
- If the transaction completes then the past purchases label will be updated with the name of the product followed by its cost (plus the format decided earlier).
- If the transaction fails then the past purchases label will display grey text stating that the user cannot afford the product and will exit the algorithm.
  # Buy the actual product
def buyProduct(product):
if len(User) == 4 and len(
product) == 4: # checks that there is a valid user/product located, if so item can be bought! if product[2] > 0:
term = '(-£', 'RED' # Determines whether the bought product is a xpositive or negative value assigning an appropriate colour
elif product[2] < 0:
term = '(+£', 'GREEN'
else:
term = '( £', 'GREY'
if charge(User[0], product[2]) is True: database.commit() current_screen.db_purchases_label.configure(
text=(product[1] + term[0] + str(product[2]) + ')\n' + current_screen.db_purchases_label.cget('text')),
bg=term[1]) # Adds the newly bought product with the text background colour of term[2] else:
current_screen.db_purchases_label.configure(
text=(str(product[2]) + ' CANNOT AFFORD\n' + current_screen.db_purchases_label.cget('text')), bg='GREY') # Adds the newly bought product with the text background colour of term[2]
return
67
 
   Charge Algorithm
The algorithm will have a “userid” passed to it of the user that that is being charged and will have the “amount” passed to it.
First the algorithm will open a connection to the database and will run the following SQL statement to extract the balance of the userid passed:
'SELECT Balance FROM tbl_UserData WHERE UserID = userid’
The balance will then be rounded appropriately and converted into a float data type. Next, the amount the item costs will be taken away from the balance, if this value is positive then the transaction will be allowed to go through, and the following SQL command will be executed:
‘UPDATE tbl_UserData SET Balance = bal + 'WHERE UserID = userid'
This SQL command will update the balance column for the specified user to be the post-transaction balance. The program will now commit the changes and close the database connection and return True.
If the amount of the balance minus the cost is negative, then the algorithm will close the database connection and return False.
   # Charge function
def charge(userid, amount):
db = database.cursor()
for bal in db.execute('SELECT Balance FROM tbl_UserData WHERE UserID ="{}"'.format(str(userid))):
bal = float(bal[0])
bal = round(bal, 2)
amount = float(amount) amount = round(amount, 2) if bal - amount >= 0:
bal = bal - amount bal = round(bal, 2) db.execute(
'UPDATE tbl_UserData SET Balance ="{}"'.format(str(bal)) + 'WHERE UserID ="{}"'.format(str(userid))) db.close()
return True
else: db.close()
return False
68
 
   Review 2 - Testing of Stages 4 to 7
Analysis Problem Breakdown Link
First of all, I will look back at the analysis section of my project.
Justification of How I Solved the Problems
The problem to be addressed was that in traditional checkout systems, “People get charged incorrect amounts/given incorrect change”, the program so far automates the transaction process and will not make any errors regarding charging users. The balance is digital so no physical change will be given.
The traditional problem of “What if I forget to bring in money?” (mentioned in the breakdown of the problem in the analysis section) will be solved as all balances are digital and can be topped up digitally. There is no need to bring in any physical change as your digital balance will be used assigned to your face. The program so far can recognise you and extract your balance and can allow you to checkout an item with just your face and a valid product.
Testing
Now I have finished seven of my stages I will look back at the testing I came up with for my software for stages 4 to 7.
   Review Number
   What Stages need to be reviewed?
   How will these stages be tested?
If all answers to the questions are yes, then I will be ready to move on to the next stage of development.
    Review 2
   Stage 4 Stage 5 Stage 6 Stage 7
   - Does the algorithm load every user into the correct variables without fail?
- Can the facial recognition algorithm correctly recognise users from the database?
- Can it display the user’s information from the database in the correct format?
- Do the added delays function correctly?
- Can the program correctly recognise and
extract information from barcodes?
- Can the program look up a barcode’s
information in the database and retrieve the appropriate data from it if it finds a match?
- Can the user make a transaction with their face and a valid barcode?
 69
 
               - Does the program correctly deduct the correct amount from a user’s balance when a transaction is made?
- Are all changes saved correctly to the database without fail?
 70
 
   “Does the algorithm load every user into the correct variables without fail?”
To test this, I inserted a print statement into the loadFaces algorithm that would print out the contents of known_face_names and known_face_encodings after the algorithm had been ran.
This ran without any errors and produced the following:
If the program were to be tested later on it would be with a much larger data set to see if it would load a large number of faces into the program correctly.
 known_face_names = [“1”, “2”] known_face_encodings = [“user1encodings”, “user2encodings”] *
* - Encoding abbreviated for convenience
71
 
   “Can the facial recognition algorithm correctly recognise users from the database?”
Now having removed the test data from the variables known_face_encodings and known_face_names, it is only the algorithm loadFaces that will populate those variables.
Upon running the program, it managed to recognise each of the users in my test data and so this test can be labelled a success.
   72
 
   “Can it display the user’s information from the database in the correct format?”
  If we look at the screen once a user has been recognised, the balance is displayed correctly along with the correct name, however the balance is not in the correct format that I would like. I want it rounded to 2 decimal places.
For example, £30 should be £30.00, £3.2 should be £3.20.
So, I needed to code a short algorithm that would round these valued correctly and if needed insert a dot in the correct place.
I came up with the following:
- First, get the user’s balance and round it to 2 decimal places using the built-in python
function (this does not put it into the correct format as it would round a value like 3.20 to
3.2 which is not correct, it must be 3.20).
- Next, the balance is converted to a string and the character 1 back from the last digit is
recorded
- Finally, the recorded character is checked, if it is a dot then an extra zero is inserted, if not
then the balance is printed as is.
- All values will now be in the format of £XX.xx
 bal = User[3]
bal = round(bal, 2) bal = str(bal)
dot_check = bal[len(bal) - 2]
if dot_check == '.': bal = bal + '0'
current_screen.db_balance_label.configure(text='£' + bal)
73
 
   Upon restarting the program, the balance values now displayed correctly as I had envisioned. Thus, this test can be labelled a success.
  74
 
   “Do the added delays function correctly?”
The following delays were added into the program and were tested by adding print statements into the program at strategical locations when each delay is updated to observe how the delays changed as the program was ran.
switchDelay – The delay before the faceScan algorithm is ran on the camera output to prevent crashing from running the algorithm on a camera output that has not fully initialised. This delay functioned perfectly and prevented any errors arriving during the running of the program.
repeatDelay – The delay before allowing a new purchase to be made to prevent transactions being rapidly repeated whilst a barcode is in shot. This delay functioned perfectly and allowed the user enough time to decide whether to make a repeated transaction or abort the transaction.
After observing the running of the program, I decided that a third delay would be needed, this would simply be named ‘delay’. This delay would count down for every frame that a face is not recognised for, once it hits zero it would return the labels to their default (empty) values. This was so that a purchase could be made for a limited time without a face being shown to make the program easier to use as without this you would have to fit your face plus a barcode in a small camera frame which proved difficult.
All three delays now functioned perfect and thus this test can be labelled a success.
75
 
   “Can the program correctly recognise and extract information from barcodes?”
I decided the best way to test this part, was to try out the program on various barcodes from the test data discussed earlier and as shown in the images below the program recognised all of them as barcodes and ran the consequent algorithms and so the test can be labelled a success.
  76
 
   “Can the program look up a barcode’s information in the database and retrieve the appropriate data from it if it finds a match?”
The program correctly identified the barcode, looked in up in the database and discovered what it was and outputted the correct data (name of product followed by its cost) for each item outlined in my test data and so this test can be concluded as a success.
  77
 
   “Can the user make a transaction with their face and a valid barcode?”
The program allowed a transaction to go through listing the purchase in the recent purchase box under the correct user’s name so the transaction worked with their face and a valid barcode (from the test data) and thus this test can be concluded as a success.
  78
 
   “Does the program correctly deduct the correct amount from a user’s balance when a transaction is made?”
To test this, I scanned various products from the test data (totalling £5.20) and the consequent balance for user 1 (me) was £34.80 (down £5.20 from £40 start) which was the correct amount and so this test can be called a success.
 79
 
   “Are all changes saved correctly to the database without fail?”
The changes that should have been made in the previous test were carried over to the database correctly as the record for user 1 (test data) had its balance correctly updated after the transaction had gone through.
and thus, the test can be labelled a success and the second review was a success.
 80
 
   Summary of Second Review and Testing
  Test Question
   Was the test a success?
   (if applicable)
Did the problem get fixed?
    Does the algorithm load every user into the correct variables without fail?”
   Success
    Can the facial recognition algorithm correctly recognise users from the database?
  Success
    Can it display the user’s information from the database in the correct format?
   Partial Success, balance wasn’t correctly formatted
   Success
    Do the added delays function correctly?
    Partial Success, extra delay was to be added
    Success
    Can the program correctly recognise and extract information from barcodes?
   Success
    Can the program look up a barcode’s information in the database and retrieve the appropriate data from it if it finds a match?”
  Success
    Can the user make a transaction with their face and a valid barcode?
    Success
    Does the program correctly deduct the correct amount from a user’s balance when a transaction is made?
  Success
    Are all changes saved correctly to the database without fail?
    Success
 81
 
   Stage 8 - Allow the User to Add New Users on the Add User Screen
To allow the user of the program to add a new user I needed the following 4 points of information from them inputted into the program:
- The next free UserID
- A First Name
- A Surname
- An Image of the user’s face
To get the next available UserID I came up with the following algorithm.
This algorithm would sort the list known_face_names in ascending numerical order which holds all the UserIDs currently loaded into the program, it would then get the highest value and store this in the last_id and so all that is needed is that the last_id is incremented by one and that value is used as the next available UserID.
This algorithm would be run every time the new user screen is opened.
The inputting of a First Name and Surname would be done using a text box (this would need to be validated).
   # Gets highest ID being used so that new users can be assigned correct IDs
def get_highest_id():
global last_id
last_id = sorted(known_face_names) # Sorts the known face names list and sorts it in ascending order last_id = last_id[len(last_id) - 1] # and gets the highest value to be used when adding new users to the
database
last_id = int(last_id)
82
 
   The image would need to be taken using the webcam output, to do this I developed the following algorithm.
This would quickly initialise the camera and get a frame then write this image to the directory “Screenshots/frame.jpg” and display the text “Photo Taken” in place of the button.
Now all the data can be inputted by the user, now all that is left is to validate the data entered and save it to the database.
I needed to code a new algorithm that would validate all the inputs so I created a new sub-procedure in the new user screen class called add_record
- First the program would grab the text inputting in the first name and surname text boxes
- Next, the program would grab the text of the photo button, if the text is in its default state
then the program will update the button’s text to display the error message “You need to
take a photo first!” and would stop the procedure.
- Now it would check to see if the first name or surname boxes were empty, if they were then
the button’s text would be updated to display the error “Text boxes cannot be empty” and
would stop the procedure.
- Now the procedure will attempt to search for a user in the database that matches the first
name and surname given as these values must be unique to the database, if a user already exists of those inputs then the algorithm will be halted and the button’s text will display “User already exists”.
- If all the data meets the requirement, then the following SQL command will be executed on the UserData table using the number last_id + 1 as the UserID, the command would save all the data inputted into the database:
- Next, the photo taken would be copied across and stored with the other photos of users, the name of the file would be a randomly generated number between 1 and 999999 as the probability of getting two numbers the same would be very low, then the user_id would be added to the end of the file name to make it unique.
- Finally, the following SQL command would be executed on the Photos table to save the location of the photo along with the UserID associated with the photo:
'INSERT INTO tbl_Photos VALUES ("{}"'.format(photoid) + ', "{}"'.format(next_id)’
 def quickScanFace():
vid = CameraOutput(0)
frame = vid.get_frame()[1]
cv2.imwrite("Screenshots/frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)) current_screen.imageScan.configure(text='Photo Taken')
 'INSERT INTO tbl_UserData VALUES ("{}"'.format(next_id) + ', "{}"'.format(firstname) + ', "{}"'.format(surname) + ', "5"
  def add_record(self):
firstname = self.firstName_entry.get()
surname = self.surname_entry.get()
if self.imageScan.cget('text') == 'Click to take a photo!':
self.user_button.configure(text='You need to take a photo first!') print('(' + get_date() + ') Failed to meet New User criteria')
83
 
    return
if firstname == '':
self.user_button.configure(text='First name cannot be blank') print('(' + get_date() + ') Failed to meet New User criteria') return
if surname == '':
self.user_button.configure(text='Surname cannot be blank') print('(' + get_date() + ') Failed to meet New User criteria') return
for line in db.execute('SELECT Firstname, Surname FROM tbl_UserData WHERE Firstname = "{}"'.format( firstname) + 'AND Surname = "{}"'.format(surname)):
self.user_button.configure(text='User Already Exists', bg='RED')
print('(' + get_date() + ') Product did not meet one or more requirements') return
next_id = str(last_id + 1)
random_number = str(random.randint(0, 999999)) photoid = random_number + next_id
# Information accepted, now insert data into the database
db.execute(
'INSERT INTO tbl_UserData VALUES ("{}"'.format(next_id) + ', "{}"'.format(firstname) + ', "{}"'.format(
surname) + ', "5")')
copy('Screenshots/frame.jpg', 'Photos/' + str(photoid) + '.jpg') db.execute(
'INSERT INTO tbl_Photos VALUES ("{}"'.format(photoid) + ', "{}"'.format(next_id) + ')') database.commit()
self.user_button.configure(text='User Added')
print('(' + get_date() + ') User successfully added to the UserData table!')
loadFaces()
84
 
   Stage 9 – Allow the User to add new Products on the add Product Screen
 To allow the user of the program to add a new product I needed the following 4 points of information from them inputted into the program:
- The product name
- A valid barcode (to be scanned in via the program)
- The cost of the product
- A short description of the product
Getting the product name, cost and description inputs are simple as the user will simply input them into the given text box, however, to scan a barcode the program will need a separate algorithm. I came up with the algorithm below.
 # Quick scan, take a quick snapshot to analyse barcode
def quickScanCode():
# Load camera output
print(‘(‘ + get_date() + ‘) Scanning for barcode...’) for I in range(0, 11):
vid = CameraOutput(0)
ret, frame = vid.get_frame() decodedObjects = pyzbar.decode(frame) if len(decodedObjects) == 1:
result = decodedObjects[0].data
result = result # [1:len(result) – 1] current_screen.barcode_entry.configure(text=result)
print(‘(‘ + get_date() + ‘) Barcode “’ + result + ‘” found in scan!’)
The algorithm would repeat 10 times, taking a single frame in each loop and checking it for a valid barcode, if one is found then the algorithm stops repeating and the value of the barcode is stored in the text of the button.
Now it was time to add the validation for the submit button.
- First the data would be extracted for each text box and the text in the scan barcode button. 85
 
   - If the scan barcode button’s text is the same as the default values, then the algorithm is halted, and an appropriate error message is displayed in the submit button.
- Next, the cost will be turned into a floating-point value, if this results in an value error (because the value is not numerical) then the value error will be captured in the try loop and the algorithm will be halted and an appropriate error message will be displayed in the submit button.
- The values will be checked that none are empty, if a text box is blank then the algorithm will be halted, and an appropriate message will be displayed in the submit button.
- Now the barcodenumber will be looked up in the database to see if it is unique, if it is not then the algorithm will be halted, and an appropriate error message will be displayed in the submit button.
- If the inputs pass all the checks then the following SQL command will be executed that will add the new product into the database:
- Finally, the button text will be updated to display an appropriate message that instructs the user that the product has been successfully added.
 ‘INSERT INTO tbl_Products VALUES (“{}”’.format(barcode) + ‘, “{}”’.format(name) + ‘, “{}”’.format(cost) + ‘, “{}”’.format(description) + ‘)’
 def add_record(self):
name = self.name_entry.get()
barcode = str(self.barcode_entry.cget('text'))
barcode = barcode[2:len(barcode) - 1]
cost = self.cost_entry.get()
description = self.description_entry.get()
print('(' + get_date() + ') The following product was attempted to be added to the
database: "' + name + '"',
'"' + barcode + '"', '"' + cost + '"', '"' + description + '"')
if name == '' or barcode == 'ick to Sca' or cost == '' or description == '': self.user_button.configure(text='Boxes above cannot be blank!', bg='RED') print('(' + get_date() + ') Product did not meet one or more requirements') return
try: float(cost)
except ValueError:
self.user_button.configure(text='Cost must be a valid number\ne.g 1.99',
bg='RED')
print('(' + get_date() + ') Product did not meet one or more requirements') return
db = database.cursor()
for line in db.execute('SELECT BarcodeNumber, Title FROM tbl_Products WHERE BarcodeNumber = "{}"'.format(
barcode) + 'OR Title = "{}"'.format(name)): self.user_button.configure(text='Already Exists', bg='RED')
print('(' + get_date() + ') Product did not meet one or more requirements') return
db.execute('INSERT INTO tbl_Products VALUES ("{}"'.format(barcode) + ', "{}"'.format(name) + ', "{}"'.format(
86
 
    cost) + ', "{}"'.format(description) + ')')
database.commit()
print('(' + get_date() + ') Product successfully added to the Products table!') db.close()
self.user_button.configure(text='Product Successfully Added!', bg='GREEN')
87
 
   Stage 10 - Add logging system in console to monitor the running of the program
My idea for this logging system is that each decision the program makes will be ‘logged’ in the Python console so that the program can be monitored to understand where any (if any) errors may occur.
The logs will take the following format:
Upon adding these ‘logs’ into the program, the loading sequence of the program looked like the following in the Python console:
 (todaysdate, time) UserName made a successful transaction totalling £X.XX (12/24/01 09:17:06) Ben Tindal made a successful transaction totalling £2.99, it was successful!
 (17/03/2020 09:18:12) Loading imports... 0%
(17/03/2020 09:18:17) Loading Screens... 25%
(17/03/2020 09:18:17) Encoding faces... 50%
(17/03/2020 09:18:21) The following UserIDs were loaded correctly ['1', '2', '3']
(17/03/2020 09:18:21) Loading completed, initialising GUI... 100%
When interacting with the program the python console looked like the following:
(17/03/2020 09:19:53) Screen switched to "Add Product Screen"
(17/03/2020 09:19:55) The following product was attempted to be added to the database: "" "ick to Sca" "" "" (17/03/2020 09:19:55) Product did not meet one or more requirements
(17/03/2020 09:19:56) Screen switched to "Home Screen"
(17/03/2020 09:19:57) Screen switched to "Add User Screen"
(17/03/2020 09:20:00) Screen switched to "Home Screen"
(17/03/2020 09:20:00) Screen switched to "Checkout Screen"
(17/03/2020 09:20:03) Screen switched to "Home Screen"
88
 
   Review 3 – Testing of Stages 8 to 10
Analysis Problem Breakdown Link
First of all, I will look back at the analysis section.
Justification of How I Solved the Problems
The issue of “Canteen queues are long and slow; how can a computer help this?” has been solved by creating an easy-to-use interface for the program that works quickly and efficiently. A user can make a transaction using the program within seconds and so a canteen queue would be sped up drastically if the canteen made use of this program.
“Will this software be expensive to run? What other devices are needed to get this to run?” The program is not expensive to run, it requires a decent quality camera along with a computer that can run Python. Unlike other systems mentioned before such as Amazon’s hands-free checkout system that required hundreds of cameras/scanners to function, this program requires one camera and does the equivalent job and so is a much cheaper and economical method that is also viable in smaller shops too.
My usage of a SQL database integrated with the program means all the data required (user encodings, product cost & barcodenumbers) can all be accessed within seconds making this solution fast and efficient.
89
 
   Testing
Now I have finished all of my stages I will look back at the testing I came up with for my software.
   Review Number
   What Stages need to be reviewed?
   How will these stages be tested?
If all answers to the questions are yes, then I will be ready to move on to the next stage of development.
    Review 3
   Stage 8 Stage 9 Stage 10
   - Can the software prevent the following new users from being added?
i) If the First Name and/or Surname text box is blank
ii) If a photo has not been taken
iii) If the First Name & Surname is not
unique to the database (already
exists)
- Can the software add a new user onto
the database and save the changes?
- Can the software prevent the following
new products from being added?
i) if the Product Name, Description,
Cost and/or Barcode Number text
box is blank
ii) If a barcode has not been scanned in
(so the value is blank)
iii) If the Barcode Number is not unique
to the database (already exists)
- Can the software add a new product
onto the database and save the
changes?
- Does the software refresh the loaded
faces every time a new user is added so
that they can be recognised?
- Does the software output a log of all
interactions the user has with the software so that any errors/problems with the software can be solved?
 90
 
   “Can the software prevent the following new users from being added”
I decided that the best way to test these would be to insert data into the program to see how it handles it.
All three of these conditions should result in an appropriate error message being shown in the button’s text and the user not being added into the database.
If the First Name and/or Surname text box is blank
  91
 
   92
If a photo has not been taken
  
   If the First Name & Surname is not unique to the database (already exists)
 The program successfully blocked all these conditions and thus the test can be labelled a success.
93
 
   “Can the software add a new user onto the database and save the changes?”
 The program correctly recognised that this new user was inputted correctly and was unique so was added into the program.
Upon checking the database, the new user was added correctly into the UserData table and their photo was copied and linked to the Photos table.
The data had been successfully and correctly added to the database and so this test can be labelled a success.
  94
 
   “Can the software prevent the following new products from being added?”
I decided that the best way to test these would be to insert data into the program to see how it handles it.
All three of these conditions should result in an appropriate error message being shown in the button’s text and the user not being added into the database.
If the Product Name, Description, Cost and/or Barcode Number text box is blank
The program has rejected the null/empty values and displayed an appropriate error message.
  95
 
   If a barcode has not been scanned in (so the value is blank)
All values have been inputted apart from a barcode being scanned in by the program.
If the Barcode Number is not unique to the database (already exists)
  The program rejected the barcode that matches another value on the database.
In conclusion, the program rejected all the conditions that it should have and so the test can be labelled a success.
96
 
   “Can the software add a new product onto the database and save the changes?”
  The product was correctly saved to the database and the program submitted a success message and thus the test can be concluded and called a success.
97
 
    Once I added this new user, the program froze for a few seconds as it refreshed the faces by running the loadFaces algorithm. Once I went to the checkout screen the newly added face was correctly recognised.
 98
 
   “Does the software output a log of all interactions the user has with the software so that any errors/problems with the software can be solved?”
Upon initialisation of the program the console outputted the following:
 As the program continued to run and I attempted to add a new product into the database, the following was outputted in the console.
When the program was closed, the following was outputted in the console.
The logs all outputted correctly so the test can be concluded and called a success.
  99
 
   Summary of Third & Final Review and Testing
   Test Question Was the test a success? (if applicable)
Did the problem get
fixed?
    Can the software prevent incorrect new users from being added?
     Success
   Can the software add a new user onto the database and save the changes?
 Success
    Can the software prevent incorrect new products from being added
   Success
   Can the software add a new product onto the database and save the changes?
   Success
    Does the software output a log of all interactions the user has with the software so that any errors/problems with the software can be solved?”
   Success
 100
 
   Evaluation of my Program
Post-Development Testing for Function
I will recap my previous function testing.
    Review Number
   What Stages need to be reviewed?
   How will these stages be tested?
If all answers to the questions are yes then I will be ready to move on to the next stage of development.
    Review 1
   Stage 1 Stage 2 Stage 3
   - Navigate between the screens, do they navigate smoothly and direct the user to the correct screens?
- Does the database prevent incorrect data being added, does it save/function correctly?
- Does the camera initialise correctly and display smoothly?
- Does the facial recognition algorithm recognise a test user correctly?
   Review 2
 Stage 4 Stage 5 Stage 6 Stage 7
 - Does the algorithm load every user into the correct variables without fail?
- Can the facial recognition algorithm correctly recognise users from the database?
- Can it display the user’s information from the database in the correct format?
- Do the added delays function correctly?
- Can the program correctly recognise and
extract information from barcodes?
- Can the program look up a barcode’s
information in the database and retrieve the appropriate data from it if it finds a match?
- Can the user make a transaction with their face and a valid barcode?
- Does the program correctly deduct the correct amount from a user’s balance when a transaction is made?
- Are all changes saved correctly to the database without fail?
  Review 3
   Stage 8 Stage 9 Stage 10
   - Can the software prevent the following new users from being added?
 101
 
               vii) If the First Name and/or Surname text box is blank
viii) If a photo has not been taken
ix) If the First Name & Surname is
not unique to the database
(already exists)
- Can the software add a new user onto
the database and save the changes?
- Can the software prevent the following
new products from being added?
vii) If the Product Name,
Description, Cost and/or Barcode
Number text box is blank
viii) If a barcode has not been
scanned in (so the value is blank)
ix) If the Barcode Number is not
unique to the database (already
exists)
- Can the software add a new product
onto the database and save the
changes?
- Does the software refresh the loaded
faces every time a new user is added so
that they can be recognised?
- Does the software output a log of all
interactions the user has with the software so that any errors/problems with the software can be solved?
 102
 
   “Navigate between the screens, do they navigate smoothly and direct the user to the correct screens?”
The screens navigate smoothly and direct the user to the correct screen; however, I was not happy with the fact that every time I changed screen, the new screen would open up slightly to the right and would continue to move slightly right every time. To fix this, I added a location flag to each of the screens so that they would snap to the top right of the computer screen.
This involved the line below being added to each of the screens, setting the dimensions of the window and secondly snapping it to the coordinate (0, 0) of the screen (Top right).
self.window.geometry('1024x612+0+0')
“Does the database prevent incorrect data being added, does it save/function correctly?”
 I attempted to input the following into the database:
   Input
Expected Outcome
Actual Outcome
  Blank input
   Rejected, cannot be blank
   Was rejected, success
   Non-numerical data inputted for cost and balance
“awrh”
 Rejected, data must be numerical
 Was rejected, success
    String entered for name and surname
“Ben”, “Tindal”
    Accepted, name and surname should both be strings
    Data was accepted and allowed to save into the database
 A repeated barcodenumber was inputted
Rejected, barcodenumber must be unique
Was rejected, success
   “Does the camera initialise correctly and display smoothly?”
For the most part the camera would initialise correctly, however occasionally it would crash upon loading up, this was due to the program attempting to recognise a face before the camera had fully loaded.
To fix this I created a variable named switchDelay which would be used to delay the running of the faceScan algorithm whilst the camera initialises.
To implement it I set the variable switchDelay to be set to equal 5 every time the screen is switched to the checkout screen, this would then be decremented by 1 for each frame of the camera whilst it is greater than 1, when this delay is less than or equal to 0 the faceScan algorithm can be ran.
103
 
   Now it was implemented the program opened the checkout screen smoothly and correctly without errors.
104
 
   “Does the facial recognition algorithm recognise a test user correctly?”
To test this, I used it on myself, the photo I added earlier was loaded into the program and this was the outcome.
 The test was a success, the program correctly recognised my face (image slightly blurred as censorship). Thus, the program managed to recognise a test user correctly.
105
 
   “Does the algorithm load every user into the correct variables without fail?”
To test this, I inserted a print statement into the loadFaces algorithm that would print out the contents of known_face_names and known_face_encodings after the algorithm had been ran.
This ran without any errors and produced the following:
known_face_names = [“1”, “2”]
known_face_encodings = [“user1encodings”, “user2encodings”] *
* - Encoding abbreviated for convenience
If the program were to be tested later on it would be with a much larger data set to see if it would load a large number of faces into the program correctly.
106
 
   “Can the facial recognition algorithm correctly recognise users from the database?”
Now having removed the test data from the variables known_face_encodings and known_face_names, it is only the algorithm loadFaces that will populate those variables.
Upon running the program, it managed to recognise each of the users in my test data and so this test can be labelled a success.
  107
 
   “Can it display the user’s information from the database in the correct format?”
  If we look at the screen once a user has been recognised, the balance is displayed correctly along with the correct name, however the balance is not in the correct format that I would like. I want it rounded to 2 decimal places.
For example, £30 should be £30.00, £3.2 should be £3.20.
So, I needed to code a short algorithm that would round these valued correctly and if needed insert a dot in the correct place.
I came up with the following:
- First, get the user’s balance and round it to 2 decimal places using the built-in python function (this does not put it into the correct format as it would round a value like 3.20 to 3.2 which is not correct, it must be 3.20).
- Next, the balance is converted to a string and the character 1 back from the last digit is recorded
- Finally, the recorded character is checked, if it is a dot then an extra zero is inserted, if not then the balance is printed as is.
- All values will now be in the format of £XX.xx
 bal = User[3]
bal = round(bal, 2) bal = str(bal)
dot_check = bal[len(bal) - 2]
if dot_check == '.': bal = bal + '0'
current_screen.db_balance_label.configure(text='£' + bal)
108
 
   Upon restarting the program, the balance values now displayed correctly as I had envisioned. Thus, this test can be labelled a success.
  109
 
   “Do the added delays function correctly?”
The following delays were added into the program and were tested by adding print statements into the program at strategical locations when each delay is updated to observe how the delays changed as the program was ran.
switchDelay – The delay before the faceScan algorithm is ran on the camera output to prevent crashing from running the algorithm on a camera output that has not fully initialised. This delay functioned perfectly and prevented any errors arriving during the running of the program.
repeatDelay – The delay before allowing a new purchase to be made to prevent transactions being rapidly repeated whilst a barcode is in shot. This delay functioned perfectly and allowed the user enough time to decide whether to make a repeated transaction or abort the transaction.
After observing the running of the program, I decided that a third delay would be needed, this would simply be named ‘delay’. This delay would count down for every frame that a face is not recognised for, once it hits zero it would return the labels to their default (empty) values. This was so that a purchase could be made for a limited time without a face being shown to make the program easier to use as without this you would have to fit your face plus a barcode in a small camera frame which proved difficult.
All three delays now functioned perfect and thus this test can be labelled a success.
110
 
   “Can the program correctly recognise and extract information from barcodes?”
I decided the best way to test this part, was to try out the program on various barcodes from the test data discussed earlier and as shown in the images below the program recognised all of them as barcodes and ran the consequent algorithms and so the test can be labelled a success.
  111
 
   “Can the program look up a barcode’s information in the database and retrieve the appropriate data from it if it finds a match?”
The program correctly identified the barcode, looked in up in the database and discovered what it was and outputted the correct data (name of product followed by its cost) for each item outlined in my test data and so this test can be concluded as a success.
  112
 
   “Can the user make a transaction with their face and a valid barcode?”
The program allowed a transaction to go through listing the purchase in the recent purchase box under the correct user’s name so the transaction worked with their face and a valid barcode (from the test data) and thus this test can be concluded as a success.
  113
 
   “Does the program correctly deduct the correct amount from a user’s balance when a transaction is made?”
To test this, I scanned various products from the test data (totalling £5.20) and the consequent balance for user 1 (me) was £34.80 (down £5.20 from £40 start) which was the correct amount and so this test can be called a success.
 114
 
   “Are all changes saved correctly to the database without fail?”
The changes that should have been made in the previous test were carried over to the database correctly as the record for user 1 (test data) had its balance correctly updated after the transaction had gone through.
and thus, the test can be labelled a success and the second review was a success.
 115
 
   “Can the software prevent the following new users from being added”
I decided that the best way to test these would be to insert data into the program to see how it handles it.
All three of these conditions should result in an appropriate error message being shown in the button’s text and the user not being added into the database.
If the First Name and/or Surname text box is blank
  116
 
   117
If a photo has not been taken
  
   If the First Name & Surname is not unique to the database (already exists)
 The program successfully blocked all these conditions and thus the test can be labelled a success.
118
 
   “Can the software add a new user onto the database and save the changes?”
 The program correctly recognised that this new user was inputted correctly and was unique so was added into the program.
Upon checking the database, the new user was added correctly into the UserData table and their photo was copied and linked to the Photos table.
The data had been successfully and correctly added to the database and so this test can be labelled a success.
  119
 
   “Can the software prevent the following new products from being added?”
I decided that the best way to test these would be to insert data into the program to see how it handles it.
All three of these conditions should result in an appropriate error message being shown in the button’s text and the user not being added into the database.
If the Product Name, Description, Cost and/or Barcode Number text box is blank
The program has rejected the null/empty values and displayed an appropriate error message.
  120
 
   If a barcode has not been scanned in (so the value is blank)
All values have been inputted apart from a barcode being scanned in by the program.
If the Barcode Number is not unique to the database (already exists)
  The program rejected the barcode that matches another value on the database.
In conclusion, the program rejected all the conditions that it should have and so the test can be labelled a success.
121
 
   “Can the software add a new product onto the database and save the changes?”
  The product was correctly saved to the database and the program submitted a success message and thus the test can be concluded and called a success.
122
 
    Once I added this new user, the program froze for a few seconds as it refreshed the faces by running the loadFaces algorithm. Once I went to the checkout screen the newly added face was correctly recognised.
 123
 
   “Does the software output a log of all interactions the user has with the software so that any errors/problems with the software can be solved?”
Upon initialisation of the program the console outputted the following:
 As the program continued to run and I attempted to add a new product into the database, the following was outputted in the console.
When the program was closed, the following was outputted in the console.
The logs all outputted correctly so the test can be concluded and called a success.
  124
 
   Post Development Testing for Robustness
“the ability to withstand or overcome adverse conditions or rigorous testing”
Stress Test (as described in success criteria point 1)
To rigorously test my program, I decided that I would have to add many users and many products to the program to see if it could handle all the added information.
The idea here was that if I added lots of faces to the program, it could become overloaded with information and misidentify faces.
However, due to current events at the time of my development (Coronavirus) I did not have access to a large sample of people in person so instead I decided to use images of people from the internet. However, these would not simulate real-life photo conditions, for example, varying indoor lighting conditions, but would allow me to see if the program could individually identify each user correctly.
I scraped the following 10 faces in the image below from the internet and loaded them into the program one by one using the add user screen.
  125
 
   The new users were added in the following format:
First name: User
Surname: Number of faces, for example, 7 UserID: Number of face
Once they were all added the database looked like the following:
  126
 
   Now it was time to run the checkout screen on the faces. The table below shows the results.
Face Outcome Success? Number
       1
       Yes
   2
     Yes
    3
         Yes
 127
 
      4
       Yes
    5
    Yes
   6
       Yes
 128
 
       7
         Yes
   8
   Yes
    9
         Yes
 129
 
      10
       Yes
 The program successfully recognised all ten different users with no issues whatsoever! The ‘stress-test’ can therefore be concluded a success as the program could handle lots of people loaded into the program and still function correctly as normal.
130
 
   Mass-Test of Products
I will now test all of my products outlined in the post-development test data in the design section.
I have a variety of products to test my program with, this will contain 5 different products including various household items I have around my house.
The products include:
- Two Xbox One games (with barcode on back), one that is on the database and one that is
not
- Can of Drink (barcode on back)
- Barcode off of phone’s screen
- Random barcode not on the database from phone’s screen
Why this test data?
The two barcodes off of my phone’s screen will act as a barcode in perfect lighting to compare the results of the other products to as the lit-up barcode on the screen will have the perfect lighting conditions for the program to scan it with.
An Xbox game case will be used as it represents a common object that contains a barcode that will be scanned in in normal lighting conditions. Items like this will be the most commonly scanned in item on the program. I have chosen one that is on the database as it will see whether the software can recognise it and secondly check whether its on the database, the second Xbox game that is not on the database will allow the program to realise that the item is not on the database and not allow a transaction to go through.
The can of drink with a barcode on the back represents another common object that will scanned in using normal lighting conditions.
   131
 
      132
 
     The program correctly dealt with all 5 of the barcodes so this test can be considered a success. The program recognised when a product was/was not in the database and handled the product as appropriate.
Conclusion?
The program has handled the post-development product testing as desired and finished with no faults.
133
 
   Testing the Usability of my Program
Firstly, I decided to test the user interface of my program by checking for any spelling/formatting issues on the program, I had been pretty comprehensive when coding the program, so I did not find any.
To further test the usability of my program, I decided to hand over my program to other people who were members of my household due to being in lockdown and see if they could carry out a few tasks I set them.
The tasks they would have to do would consist of the following:
Task #1 – Add yourself onto the program.
Task #2 – Scan yourself to see if the program recognises you. Task #3 – Make a transaction using the program
Task #4 – Can you find the following bits of information?
o Thecostoftheitemyoujustbought o Yourbalance
Task #5 - Answer the following questions:
o Howeasydidyoufindtheprogramtouse?
o Doyouhaveanyimprovementstosuggestthatwouldhavemadetheprogram easier to use?
o Wereyouabletofigureouthowtousetheprogramwithminimalprompting?
134
 
   Susan:
Task #1
Subject Usability Tests
Upon being presented with the program the user pondered whether to click ‘start program’ or ‘add new user’ and then clicked onto the add user section and filled in the required information. They navigated through the form, took their photo and added the user, the program allowed this and added the new user.
Task #2
The user then navigated back to the opening screen and to the checkout screen where the program FAILED to recognise the user, so the remaining tasks were unable to be completed.
Review:
Upon investigating this failure, I discovered that the program had recognised the wrong face in the photo.
The program was supposed to add the face highlighted in green, however it recognised and added the face highlighted red, this is an issue that would need to be addressed in future development.
      135
 
   Archie:
Task #1
The user quickly navigated to the add user screen and filled in the form and added their photo then submitted the user into the database.
Task #2
The user then navigated onto the checkout screen but made the comment that a set of instructions would be useful. The program then recognised the user.
Task #3
The user then scanned the barcode for the product ‘Orange’ outlined in the test data section and the program correctly accepted the transaction.
Task #4
The user then pointed out the cost of the item was £0.60 and that their balance was now £4.40 which were both correct.
Task #5
The user remarked that the program was easy to use and very minimalistic, they once again suggested that a set of instructions be included with the program. They stated that they managed to figure out how to use the program with little help.
Review:
This user had a successful run of the program and offered useful advice which will be taken into consideration in further development of the program.
136
 
   Did I Meet My Success Criteria?
I will start my evaluation by going through my success criteria.
Criteria 1
The software must be able to individually distinguish users. Without this, it may not recognise students so will not be able to bill them for their purchase which is fundamental for the software to work. If it were to incorrectly identify students, incorrect people may be charged for other student’s purchases, therefore it must be able to individually identify each user of the software. I will measure this by adding 10 different users to the User database and attempt to see if the software can still separately identify each individual student. Ideally, I would add a thousand as that would be more realistic for an entire school, however the computing power that I have available to me would not allow this. If the software can identify each individual user, then I will accept that it meets this particular criterion.
This particular success criterion was tested as described in the ‘stress-test’ under the Post Development Testing for Robustness on page 116. Ten different users were added to the database and the program managed to individually distinguish all the users without fail. However, due to current events that had occurred at the time of development I did not have access to ten different people who I could test the program on in person so I had to make do with images of faces found on the internet that will be shown from my phone’s screen. These images do not resemble real-life image scenarios as the lighting on a still image is constant whereas in real-life the lighting conditions will vary as they are subject to a range of variables such as how much sunlight there is, the direction of the light on the face... and many other conditions. However, this test would still cover the core fundamental point of the program and would test whether the program could recognise each of the faces if the lighting was constant.
  User Number 1
2
3
4
5
6
7
8
9
10
Was the user recognised correctly?
Yes Yes Yes Yes Yes Yes Yes Yes Yes Yes
                      This success criterion was met perfectly as the program recognised all of the user’s faces without fail (as proved in the table above). If future development were to take place, I would redo this test with ten actual people to see if the program could still recognise each face correctly in varying light conditions.
137
 
   Criteria 2
The software must only allow one customer at a time to make said purchase. The software must not get confused when two people enter the camera, it must only allow one user to make said purchase before the other and not bill the other person in the camera. I will measure the success of this criteria by attempting to ‘stress’ test the software by having multiple users in frame with one person attempting to buy something. If the software completes the purchase and bills the correct person with the correct purchases, then I will accept that it meets this particular criterion.
Unfortunately, this criterion was not met, the program functions perfectly when one user’s face is within the camera frame, however as soon as another was introduced into the frame the program rapidly switched between the two faces as each was recognised. The software clearly displays who has made the purchase however if a purchase was attempted whilst two faces are within the camera frame then whoever will be billed for the product will be random.
Criteria 3
The software must not allow a customer to leave with unpaid items due to a negative balance. If a customer did not have enough money to pay for the item, then if they were to leave, they would have essentially got the item for free causing the school to lose money. This would defeat the entire point of this software being cheap to install as they would have to pay for lost money. I will test this by having multiple users attempt to make a purchase with varying balances, one that is extreme (above the cost of the item so the purchase should go through), normal (one that is below the cost of the item so should result in not allowing the purchase to go through) and erroneous (a balance that is non-numerical for example, a balance of £hello) so should result in error and not allow the purchase to go through.
Upon reflection of this criterion I was unable to test it as I had previously described. Data that is fed into the database already has to meet given criteria, for example, has to be numerical, so testing erroneous data and other types is not possible. The program does a lot of validation itself to prevent any data like that being added in the first place as shown in the “Can the software prevent the following new products from being added?” on page 111 so no data can be put in that is incorrectly formatted.
In conclusion, this criterion has been met as a user of the program cannot make a transaction if their balance is not higher than the cost of the item, the program puts up a grey flag on the screen if the transaction cannot go through to allow the customer realise that their balance is not high enough.
Criteria 4
138
 
   The software must be able to correctly recognise barcodes stored on the product database.
This criterion was tested in the “Can the program correctly recognise and extract information from barcodes?” test on page 102. The program managed to recognise all of the barcodes correctly without fail and so this criterion has clearly been met. Photos of the program recognising barcodes are shown below.
Criteria 5
The software must allow the administrators of the software to be able to add/remove products.
   This particular criterion has clearly been met through the development/previous testing of the add new product screen.
139
 
     The test “Can the software add a new product onto the database and save the changes?” on page 113 clearly demonstrates the program adding a new product onto the database and the program being able to recognise it.
  140
 
   Criteria 6
The software must be able to run/work for a sustained period without crashing.
 This criterion has definitely been met, since the introduction of the logging system (shown in the image above), it is clear what each user does with the program and the program has not suffered any crashes since development had been finished. If there were to be a crash, it would be logged in the console output and in future development the error could be amended/fixed by tracing through the log and seeing what action/actions led up to the error. Even if the program were to produce an error, the error would be captured, logged and the program would ignore it and continue to run so the program would still be usable and function as per normal.
Criteria 7
The software must be able to log errors and work around them to keep the software working.
This criterion has met through the logging system established in stage 10 of my development and tested in the test “Does the software output a log of all interactions the user has with the software so that any errors/problems with the software can be solved?” on page 115. Most actions the user has with the program will be logged, no errors will stop the program from running and any errors that do arise will be logged so that a developer could trace through the log to find out the series of actions that led up to the error arising and could in future development address the issue.
141
 
   Criteria 8
The GUI must be easy to understand and use so that users of all ages can use it. If it were too complicated to use, queues would build up defeating the entire point of minimising queues using the software. I will test this by carefully monitoring strangers to the software by looking at how they use the software and whether they are able to complete a purchase without extra assistance.
This criterion was partially met, the program has a lightweight design with minimal physical interaction needed to run the program. However, upon looking at the usability testing, test subject number 1 “Susan” had some deliberation before deciding on what button to press to do each task and mentioned that the buttons were not clearly signed posted as to what they do.
To meet this criterion, in future development I would rename the buttons to make them clearer to the user, for example, by renaming the “Start Program” button to, “Head to Checkout” or something similar. I could also add a splash screen to the start of the program that includes instructions on how to use the program before handing over controls to the user.
Overall Review of Success Criteria
Overall, I met most of my success criteria and in future development can address all of the criteria that I did not meet. The program can be deemed a success as it met the key criteria and the program can function correctly.
142
 
   Evaluation of Usability Features
Text on the Screens
All text on the screens was a large font to make them easy to read/understand. Minimal information was presented on each screen and the text that remained was vital for the functioning of the program.
Was it successful?
The text proved mostly successful as the users were clearly able to make out the text and see the key information on each screen, however, the text chosen to signpost each button was not entirely clear and along with the fact there were no key instructions on how to use the program.
How can future development amend this issue?
I would rename the buttons to make them clearer to the user, for example, by renaming the “Start Program” button to, “Head to Checkout” or something similar. I could also add a splash screen to the start of the program that includes instructions on how to use the program before handing over controls to the user.
Navigating Throughout the Program
Was it successful?
None of the users during the usability test using the program had issues with navigating through the program, each user instinctively knew how to make their way through the program making use of the ‘Home’ button to return back to the starting screen.
How can future development amend this issue?
No future development is essentially needed on the navigation part of the program except the buttons could be made to stand out more from the text labels and other parts of the program, for example, by assigning a colour to buttons making the program colour co-ordinated.
143
 
   General Usability of the Program
The program functions correctly, switching between windows as expected and recognising users correctly, the usability of the program is high as it is minimalistic and straight to the point in terms of what it does. Future development could add a set of instructions to the program but for the most part, the users figured out how to use the program just by using it.
The buttons in the program are well-labelled and large in size so navigation of the program is easy. To keep the program simple looking there is a consistent colour scheme/design in each window. As clearly shown in the images below.
  All of the complicated parts of the program do not require the user to run and the program masks these complex algorithms through an abstracted graphical interface.
144
 
   General Evaluation
Not Enough Checks on the New User Screen
What is the Issue/Limitation?
In the programs current state, there are no checks of the photo taken in the add new user screen. This issue means that as discussed previously in the usability test for the first subject, if a photo is taken with more than 1 face in the photo, then the face that is saved into the database will be random/whatever face is recognised first.
How can this be dealt with in future development?
To deal with this, a new algorithm would have to eb designed that would scan for all faces in the image. If it recognises more than 1 face in the image, then the image should be rejected, and a new user should not be added.
Subject 1 made the suggestion than an image preview box be added to the new user screen so that the person using the program can see if their face is recognisable before taking the photo. This would aid the user in using the program as they would be able to see if their face is fully within the image.
145
 
   Photos Taken Need to be Validated
What is the Issue/Limitation?
Because of the lack of validation in the add-user photos, photos like the one I took above were allowed by the program and added into the database despite no face being recognised due to poor lighting in the photo. This as a result took up the database space for the user’s credentials despite not being a functional photo with a recognisable face and I as the developer had to manually go into the database and delete the record for this user to fix the problem.
How can this be dealt with in future development?
To fix this problem, in future development I could edit the brightness of the taken photos to make faces more visible and add validation for the photo to check if firstly, there is at least one face visible and secondly, that there is only one face visible in the photo. If those criteria are met, then the user can be added to the database.
 146
 
   Maintenance Issues & Further Limitations of my Program
Maintenance Issues
If the program were to result in an error, the error would be logged making maintenance of the program simple as the user’s actions can be traced through the console log and the error can be fixed.
Maintenance whilst the program is running is very minimal, the program should be able to handle all the users added to it without fail once they have been added, the same goes with the products, once they are all added there should not be any issues with the maintenance of the program.
However, when it comes to adding the new users and the products in the first place, the program has been known to come up with problems that require knowledge of how databases work to fix as the user will need to go into the database to manually delete broken records that have found their way onto the software, however, issues like this should not happen regularly and only on the occasion.
Another maintenance issue/limitation could be caused by removing all users on the program. If the program has no users to load then the program will crash and it cannot function with no users, if this happened then a user would have to be manually added onto the database along with a photo of them.
How will this be fixed in future development?
As the program becomes widely used, commonly found errors can be looked at and fixed and the program will become more refined and less erroneous as the development continues thus less maintenance will be needed.
147
 
   Program only allows one user to make a transaction at a time
Currently, the program only supports one camera output that can only handle one user at a time.
How would this issue be addressed in future development?
This issue could be address in future development by allowing the program to look at multiple camera feeds at once in order to streamline the process. The program could then be running in multiple instances of itself along with each instance having access to its own camera.
A limitation of this future development is that the computer would then need to have more processing power.
Program uses a locally stored database
The program uses a database file that is stored locally on the computer’s hard drive, so if the program was run on multiple computers they would be running independently and could not share the same database file.
How would this issue be addressed in future development?
If future development was to take place, I would host the database file in the cloud where each instance of the program could remotely access this file. However, this would introduce a further limitation that the program would then need to have a stable internet connection in order to function correctly as currently it needs to internet connection.
Program is limited by number of people added to the program
As each new user is added to the program, the loadFaces algorithm is ran (same when the program is first bootup). The program will take longer and longer to run through this algorithm with more users being added to the program. This is a O(n) time complexity according to Big O Notation. The part of the algorithm that takes the longest is generating face encodings for each user.
How would this issue be addressed in future development?
In future development, this issue could be addressed by saving the encoding of each user once it has been generated in a separate file. Then, upon loading the loadFaces algorithm, the algorithm could then retrieve the encoding from the separate file thus saving having to generate encodings for every user in the database everytime the algorithm is ran.
148
 
   All Faces are Reloaded When a New User is Added
Currently, all user’s encodings will be regenerated once a new user has been added. The process takes lots of time and is inefficient.
This process could easily be made more efficient in future development if the algorithm was changed to be able to reload only the new user that has been added. The algorithm would have to be redesigned to only load 1 user at a time.
Other limitations
My proposed solution will be limited by all users that use it will have to be manually added to the face recognition database, this is why it is better suited to a school’s canteen as all students are on record/data is stored of all of them whereas in a public supermarket, not all the customers are known so the face recognition will simply render them as unknown and will be unable to get their balance which prevents any purchases from being made using the software. All customers of that supermarket will have to be individually added to the software.
Another limitation is that all products that are to be bought using the software must have had their appropriate barcode added to the product database, if not the software cannot work out the product’s price/title so customers will be unable to purchase said item.
Another limitation is that customers may wish to not have their photos taken and/or be monitored by cameras that will recognise their face utilising the software. If so, the software will be unable to recognise them so the software will not work for them and consequently due to the nature of the program monitoring all people who walk in front of the camera will be unable to block out individuals who do not wish to have their photo taken therefore will not be suited to an area in which a high number of people do not want their photo taken.
Final Comments
The project as a whole met most, if not all, of my success criteria and passed all of tests I subjected the program to. The program can successfully recognise people and allow them to ‘checkout’ with products added onto the database. If the database file is stored in the cloud, then the program becomes hugely scalable as the program can be ran on many computers all linked to the same database file.
There is plenty of development that can be done as outlined in the evaluation’s issues & limitations section, however, as a whole the program has met the components of the problem and goals outlined in the analysis section of the project.
149
 
   Appendix
Main.py
# Coded by Ben Tindal (2019-2020) – Facial Recognition Checkout System
import datetime
def get_date():
date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) return date
print('(' + get_date() + ') Loading imports... 0%')
import random
from shutil import copy from pyzbar import pyzbar from tkinter import * import PIL
from PIL import ImageTk import face_recognition import cv2
import numpy as np
import sqlite3
database = sqlite3.connect('checkout_data.db') db = database.cursor()
# Declaring Variables
whatScreen = 'Setup'
known_face_encodings = []
known_face_names = [] # Contains names of each user loaded
User = ['', '', '', '', '', '', '', '', '']
Product = ['', '', '', '', '', '', '', '']
delay = 50 # Delay between returning labels to default values
countdown = delay
switchDelay = 5 # Delay before scanning first face (at load-up) to prevent crashing last_barcode = ''
repeatDelay = 25 # Delay between allowing new purchase
# Gets highest ID being used so that new users can be assigned correct IDs
def get_highest_id(): global last_id
last_id = sorted(known_face_names) # Sorts the known face names list and sorts it in ascending order
last_id = last_id[len(last_id) - 1] # and gets the highest value to be used when adding new users to the database
last_id = int(last_id)
# Charge function
def charge(userid, amount):
db = database.cursor()
for bal in db.execute('SELECT Balance FROM tbl_UserData WHERE UserID
="{}"'.format(str(userid))): bal = float(bal[0]) bal = round(bal, 2)
amount = float(amount) amount = round(amount, 2) if bal - amount >= 0:
bal = bal - amount bal = round(bal, 2) db.execute(
'UPDATE tbl_UserData SET Balance ="{}"'.format(str(bal)) + 'WHERE UserID ="{}"'.format(str(userid)))
db.close()
print('(' + get_date() + ')', User[1], 'made a purchase of "', Product[1] + '" costing £' + str(amount))
            return True
        else:
                                                                        150
 
    print('(' + get_date() + ')', User[1], 'failed a purchase of "', Product[1] + '" costing £' + str(amount),
  'as they
db.close()
return False
# Quick scan, take a quick
def quickScanCode():
# Load camera output print('(' + get_date() for i in range(0, 11):
did not have a high enough balance.')
snapshot to analyse barcode
+ ') Scanning for barcode...')
          vid = CameraOutput(0)
ret, frame = vid.get_frame() decodedObjects = pyzbar.decode(frame) if len(decodedObjects) == 1:
result = decodedObjects[0].data
result = result # [1:len(result) - 1] current_screen.barcode_entry.configure(text=result)
print('(' + get_date() + ') Barcode "' + result + '" found in scan!')
def quickScanFace():
for i in range(0, 2):
vid = CameraOutput(0)
frame = vid.get_frame()[1]
cv2.imwrite("Screenshots/frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)) current_screen.imageScan.configure(text='Photo Taken')
# Takes scanned barcode data from image
def barcodeLookup(decodedObjects):
global last_barcode, Product, repeatDelay for obj in decodedObjects:
raw_barcode = obj.data if repeatDelay <= 0: repeatDelay = 25
last_barcode = ''
if raw_barcode != last_barcode: # Prevents 'spam' of checking
last_barcode = raw_barcode
raw_barcode = str(raw_barcode)
barcode = raw_barcode[2:len(raw_barcode) - 1]
# Now we have a new barcode, lets look it up in the product table
db = database.cursor()
for column in db.execute('SELECT * FROM tbl_Products WHERE BarcodeNumber
="{}"'.format(str(barcode))): Product = column
buyProduct(Product)
return
print('(' + get_date() + ') Barcode "' + barcode + '" not recognised!') db.close()
else:
last_barcode = raw_barcode
# Buy the actual product
def buyProduct(product):
if len(User) == 4 and len(
                                               product) == 4: # checks that there is a valid user/product located, if so item can be
 bought!
value assigning an appropiate colour
 if product[2] > 0:
term = '(-£', 'RED' # Determines whether the bought product is a positive or negative
          data in
elif product[2] < 0:
    term = '(+£', 'GREEN'
else:
    term = '( £', 'GREY'
current_recent_purchases = str(current_screen.db_purchases_label.cget('text'))
# if len(current_recent_purchases) > 0:
# current_recent_purchases = str(current_recent_purchases) + '\n' # If there's already the label then adds a newline
if charge(User[0], product[2]) is True:
database.commit() current_screen.db_purchases_label.configure(
    text=(product[1] + term[0] + str(product[2]) + ')\n' + current_screen.db_purchases_label.cget('text')),
   term[2]
bg=term[1]) # Adds the newly bought product with the text background colour of
151
 
    else: current_screen.db_purchases_label.configure(
text=(str(product[2]) + ' CANNOT AFFORD\n' + current_screen.db_purchases_label.cget('text')),
     term[2]
bg='GREY') # Adds the newly bought product with the text background colour of
 else:
print('(' + get_date() + ') There was no user present to purchase the product.') # Item
should not be bought
return
# Looks up the userID specified in the tbl_UserData table.
def loadUser(id):
    global User
db = database.cursor()
for column in db.execute('SELECT * FROM tbl_UserData WHERE UserID ="{}"'.format(str(id))):
User = []
for i in range(len(column)):
User.append(column[i]) db.close()
def loadFaces():
try:
global known_face_encodings, known_face_names
# Create arrays of known face encodings and their names known_face_encodings = []
known_face_names = []
db = database.cursor()
for photo in db.execute('SELECT * FROM tbl_Photos'): # WHERE UserID = 1'):
user_image = face_recognition.load_image_file("Photos/" + photo[0] + ".jpg") # get directory from db
face_encoding = face_recognition.face_encodings(user_image)[0] known_face_encodings.append(face_encoding) known_face_names.append(photo[1]) # UserID as name
db.close() except:
print('(' + get_date() + ') Error on loading one or more face encodings from database...') print('(' + get_date() + ') The following UserIDs were loaded correctly', known_face_names)
# Takes current frame from web-cam and scans it for known faces, if found, calls the matched ID on the loadUser function
# Sets result of loadUser function to the checkout screen parameters.
def faceScan(frame):
global switchDelay, countdown, User, Product, repeatDelay if repeatDelay > 0:
repeatDelay = repeatDelay - 1 if switchDelay > 0:
switchDelay = switchDelay - 1 if switchDelay <= 0:
frame = cv2.resize(frame, (0, 0), fx=0.25,
fy=0.25) # Shrinks the image down to the size needed for the library to
reduce memory requirements
frame = frame[:, :, ::-1] # Crops out unnecessary data from the resized image face_locations = face_recognition.face_locations(frame) # Runs the library on the image if len(face_locations) > 1:
return
face_encodings = face_recognition.face_encodings(frame, face_locations) if len(face_encodings) == 0:
if countdown <= 0: current_screen.db_name_label.configure(text=current_screen.db_name) current_screen.db_balance_label.configure(text=current_screen.db_balance) current_screen.db_purchases_label.configure(text=current_screen.db_purchases,
bg='MediumPurple1')
User = ''
                                                               current_screen
Product = ''
# revert past purchases variable back to default parameter defined in
 if countdown > 0:
countdown = countdown - 1
for face_encoding in face_encodings: # Goes through each found face and compares it to all the database faces.
# See if the face is a match for the known face(s)
matches = face_recognition.compare_faces(known_face_encodings, face_encoding) face_distances = face_recognition.face_distance(known_face_encodings, face_encoding) best_match_index: np.ndarray[int] = np.argmin(
face_distances) # Stores the location of the discovered face (if any)
        152
 
                     label here
if matches[best_match_index]: # If match has been found:
name = known_face_names[best_match_index] # Looks up the name loadUser(name)
    countdown = delay
current_screen.db_name_label.configure(text=User[1] + ' ' + User[2]) bal = User[3]
bal = round(bal, 2)
bal = str(bal)
dot_check = bal[len(bal) - 2]
if dot_check == '.': bal = bal + '0'
current_screen.db_balance_label.configure(text='£' + bal)
# Once past purchases have been created, edit the current_screen past purchase
 decodedObjects = pyzbar.decode(frame) if len(decodedObjects) == 1:
barcodeLookup(decodedObjects)
# Screen Switching
def switchScreen1():
global current_screen, whatScreen
print('(' + get_date() + ') Screen switched to "Home Screen"') whatScreen = 'Setup'
current_screen.destroy()
current_screen = setup_Screen()
def switchScreen2():
global current_screen, whatScreen
print('(' + get_date() + ') Screen switched to "Add Product Screen"') whatScreen = 'Products'
current_screen.destroy()
current_screen = product_Screen()
def switchScreen3():
global current_screen, whatScreen
print('(' + get_date() + ') Screen switched to "Add User Screen"') whatScreen = 'Users'
get_highest_id()
current_screen.destroy()
current_screen = user_Screen()
next_id = last_id + 1
next_id = str(next_id) current_screen.id_display.configure(text=next_id)
def switchScreen4():
global current_screen, switchDelay, whatScreen, User, Product
print('(' + get_date() + ') Screen switched to "Checkout Screen"') current_screen.destroy()
switchDelay = 5
current_screen = checkout_Screen()
whatScreen = 'Main'
User = ['', '', '', '', '', '', '', '', '']
Product = ['', '', '', '', '', '', '', ''] # reset current user/product parameters
print('(' + get_date() + ') Loading Screens... 25%')
# Screen Classes
class setup_Screen: # Screen ID 1 - SwitchScreen1()
def __init__(self): self.window = Tk()
# Code to create the screen
self.window.configure(bg='MediumPurple1') self.window.title('Setup') self.window.geometry('1024x612+0+0')
# Main header of the screen titled "Setup Screen"
label1 = Label(text='Setup System', font=('Calibri Bold', 90)) label1.configure(bg='MediumPurple4')
                                                            153
 
    label1.grid(row=0, ipadx=250)
        40))
30))
# Sub-title/header "Would you like to?"
label2 = Label(text='Would you like to?', font=('Calibri', 20)) label2.configure(bg='MediumPurple2')
label2.grid(row=1, pady=20)
start_button = Button(text='Start Program', command=switchScreen4, font=('Calibri Bold', start_button.configure(fg='Green', borderwidth='3', relief='solid')
start_button.grid(row=2, ipadx=150, ipady=30) # First Button linked to add new product page
product_button = Button(text='Add new Product', command=switchScreen2, font=('Calibri', product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid')
product_button.grid(row=3, pady=50, ipadx=28 + 100, ipady=10)
# Second Button linked to add new product page
user_button = Button(text='Add new User', command=switchScreen3, font=('Calibri', 30)) user_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid') user_button.grid(row=4, ipadx=51 + 100, ipady=10)
               self.is_wanted = True def loop(self):
self.window.mainloop()
def destroy(self): self.is_wanted = False self.window.destroy()
          class product_Screen: # Screen ID 2 - SwitchScreen2() def __init__(self):
self.window = Tk()
# Code to create the screen
self.window.configure(bg='MediumPurple1') self.window.title('Products') self.window.geometry('1024x612+0+0')
# Main header of the screen titled "Add Product Screen"
label1 = Label(text='Add Product Screen', font=('Calibri Bold', 90)) label1.configure(bg='MediumPurple4')
label1.grid(row=0, column=1)
# Home Button linked to add setup screen
product_button = Button(text='Home', command=switchScreen1, font=('Calibri', 30)) product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid') product_button.grid(row=0, column=0)
label2 = Label(text='Name', font=('Calibri', 20)) label2.configure(bg='MediumPurple2') label2.grid(row=1, column=1, pady=20, sticky=W)
self.name_entry = Entry(self.window) self.name_entry.grid(row=1, column=1, pady=20)
label2 = Label(text='Barcode', font=('Calibri', 20)) label2.configure(bg='MediumPurple2') label2.grid(row=2, column=1, pady=20, sticky=W)
self.barcode_entry = Button(text='Click to Scan', command=quickScanCode) self.barcode_entry.grid(row=2, column=1, pady=20)
label2 = Label(text='Cost', font=('Calibri', 20)) label2.configure(bg='MediumPurple2') label2.grid(row=3, column=1, pady=20, sticky=W)
self.cost_entry = Entry(self.window) self.cost_entry.grid(row=3, column=1, pady=20)
label2 = Label(text='Description', font=('Calibri', 20)) label2.configure(bg='MediumPurple2')
label2.grid(row=4, column=1, pady=20, sticky=W)
self.description_entry = Entry(self.window) self.description_entry.grid(row=4, column=1, pady=20)
                                             154
 
     # Second Button linked to add new product page
self.user_button = Button(text='Submit', command=self.add_record, font=('Calibri', 30)) self.user_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid') self.user_button.grid(row=7, column=1, ipadx=100, ipady=15)
self.is_wanted = True
def add_record(self):
name = self.name_entry.get()
barcode = str(self.barcode_entry.cget('text'))
barcode = barcode[2:len(barcode) - 1]
cost = self.cost_entry.get()
description = self.description_entry.get()
print('(' + get_date() + ') The following product was attempted to be added to the
database: "' + name + '"',
'"' + barcode + '"', '"' + cost + '"', '"' + description + '"')
if name == '' or barcode == 'ick to Sca' or cost == '' or description == '': self.user_button.configure(text='Boxes above cannot be blank!', bg='RED') print('(' + get_date() + ') Product did not meet one or more requirements') return
        try:
            float(cost)
except ValueError:
self.user_button.configure(text='Cost must be a valid number\ne.g 1.99', bg='RED') print('(' + get_date() + ') Product did not meet one or more requirements')
return
db = database.cursor()
for line in db.execute('SELECT BarcodeNumber, Title FROM tbl_Products WHERE BarcodeNumber =
"{}"'.format(
barcode) + 'OR Title = "{}"'.format(name)): self.user_button.configure(text='Already Exists', bg='RED')
print('(' + get_date() + ') Product did not meet one or more requirements') return
db.execute('INSERT INTO tbl_Products VALUES ("{}"'.format(barcode) + ', "{}"'.format(name) + ', "{}"'.format(
cost) + ', "{}"'.format(description) + ')')
database.commit()
print('(' + get_date() + ') Product successfully added to the Products table!') db.close()
self.user_button.configure(text='Product Successfully Added!', bg='GREEN')
def loop(self): self.window.mainloop()
def destroy(self): self.is_wanted = False self.window.destroy()
class user_Screen: # Screen ID 3 - SwitchScreen3() def __init__(self):
self.window = Tk()
# Code to create the screen
self.window.configure(bg='MediumPurple1') self.window.title('Users') self.window.geometry('1024x612+0+0')
# Main header of the screen titled "Add Product Screen"
label1 = Label(text='Add User Screen', font=('Calibri Bold', 90)) label1.configure(bg='MediumPurple4')
label1.grid(row=0, column=1)
# Home Button linked to add setup screen
product_button = Button(text='Home', command=switchScreen1, font=('Calibri', 30)) product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid') product_button.grid(row=0, column=0)
label2 = Label(text='UserID', font=('Calibri', 20)) label2.configure(bg='MediumPurple2') label2.grid(row=1, column=0, pady=20)
self.id_display = Label(text='Unknown', font=('Calibri', 20)) self.id_display.configure(bg='MediumPurple2') self.id_display.grid(row=1, column=1, pady=20)
label2 = Label(text='First Name', font=('Calibri', 20)) label2.configure(bg='MediumPurple2')
                                                                             155
 
    label2.grid(row=2, column=0, pady=20) self.firstName_entry = Entry(self.window)
self.firstName_entry.grid(row=2, column=1, pady=20)
label2 = Label(text='Surname', font=('Calibri', 20)) label2.configure(bg='MediumPurple2') label2.grid(row=3, column=0, pady=20)
self.surname_entry = Entry(self.window) self.surname_entry.grid(row=3, column=1, pady=20)
label2 = Label(text='Face Image', font=('Calibri', 20)) label2.configure(bg='MediumPurple2')
label2.grid(row=4, column=0, pady=20)
self.imageScan = Button(text='Click to take a photo!', command=quickScanFace) self.imageScan.grid(row=4, column=1, pady=20)
# Second Button linked to add new product page
self.user_button = Button(text='Submit', command=self.add_record, font=('Calibri', 30)) self.user_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid') self.user_button.grid(row=6, column=1, ipadx=100, ipady=15)
self.is_wanted = True
def add_record(self):
firstname = self.firstName_entry.get()
surname = self.surname_entry.get()
if self.imageScan.cget('text') == 'Click to take a photo!':
self.user_button.configure(text='You need to take a photo first!') print('(' + get_date() + ') Failed to meet New User criteria') return
if firstname == '':
self.user_button.configure(text='First name cannot be blank') print('(' + get_date() + ') Failed to meet New User criteria') return
if surname == '':
self.user_button.configure(text='Surname cannot be blank') print('(' + get_date() + ') Failed to meet New User criteria') return
for line in db.execute('SELECT Firstname, Surname FROM tbl_UserData WHERE Firstname =
"{}"'.format(
firstname) + 'AND Surname = "{}"'.format(surname)): self.user_button.configure(text='User Already Exists', bg='RED')
print('(' + get_date() + ') Product did not meet one or more requirements') return
next_id = str(last_id + 1)
random_number = str(random.randint(0, 999999)) photoid = random_number + next_id
# Information accepted, now insert data into the database
db.execute(
'INSERT INTO tbl_UserData VALUES ("{}"'.format(next_id) + ', "{}"'.format(firstname) +
', "{}"'.format(
surname) + ', "5")')
copy('Screenshots/frame.jpg', 'Photos/' + str(photoid) + '.jpg') db.execute(
'INSERT INTO tbl_Photos VALUES ("{}"'.format(photoid) + ', "{}"'.format(next_id) + ')') database.commit()
self.user_button.configure(text='User Added')
print('(' + get_date() + ') User successfully added to the UserData table!')
        loadFaces()
    def loop(self):
self.window.mainloop()
def destroy(self): self.is_wanted = False self.window.destroy()
class checkout_Screen: # Screen ID 4 - SwitchScreen4() def __init__(self, video_source=0):
# Code to create the screen
self.window = Tk() self.window.configure(bg='MediumPurple1') self.window.title('Products')
                                                                              156
 
    self.window.geometry('1024x612+0+0')
# Database Variables
self.db_name = ' ' # Default Parameters self.db_balance = ' '
self.db_purchases = ''
# Back to the screen
self.video_source = video_source
        # Load camera output
self.vid = CameraOutput(self.video_source)
# Home Button linked to add setup screen
product_button = Button(text='Home', command=switchScreen1, font=('Calibri', 30)) product_button.configure(bg='MediumPurple3', borderwidth='3', relief='solid') product_button.grid(row=0, column=0, sticky=W)
# Main header of the screen titled "Setup Screen"
label1 = Label(text='Checkout Screen', font=('Calibri Bold', 90)) label1.configure(bg='MediumPurple4')
label1.grid(row=0, column=1, columnspan=3, ipadx=100, sticky=E)
# Create a canvas that can fit the above video source size
self.canvas = Canvas(width=500, height=450)
self.canvas.grid(row=2, column=0, columnspan=2, rowspan=5, ipadx=0, sticky=W)
# Database Variables on screen
self.db_label = Label(text='Name:', font=('Calibri', 30, 'bold'), bg='MediumPurple3') self.db_label.grid(row=2, column=2, sticky=NW)
self.db_label = Label(text='Balance:', font=('Calibri', 30, 'bold'), bg='MediumPurple3') self.db_label.grid(row=3, column=2, sticky=NW)
self.db_label = Label(text='Recent Purchases:', font=('Calibri', 30, 'bold'), bg='MediumPurple3')
self.db_label.grid(row=4, column=2, sticky=NW)
self.db_name_label = Label(text=self.db_name, font=('Calibri', '50'), bg='MediumPurple2')
self.db_balance_label = Label(text=self.db_balance, font=('Calibri', '30'), bg='MediumPurple2')
self.db_purchases_label = Label(text=self.db_purchases, font=('Calibri', '20'), bg='MediumPurple1')
self.db_name_label.grid(row=2, column=2, sticky=SW, ipadx=50, ipady=35) self.db_balance_label.grid(row=3, column=2, sticky=SW, ipadx=50, ipady=0) self.db_purchases_label.grid(row=5, column=2, sticky=SW, ipadx=25, ipady=0, rowspan=2,
columnspan=2)
# update method called after a delay of 1ms
self.delay = 1 self.update()
self.is_wanted = True
def update(self):
# Get a frame from the video source ret, frame = self.vid.get_frame() if ret:
frame = cv2.resize(frame, (0, 0), fx=0.45, fy=0.70)
self.photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
self.window.after(self.delay, self.update) def loop(self):
self.window.mainloop()
def destroy(self): self.is_wanted = False self.window.destroy()
# Camera Output
class CameraOutput:
def __init__(self, video_source=0):
self.vid = cv2.VideoCapture(video_source)
self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH) self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
def get_frame(self):
if self.vid.isOpened():
ret, frame = self.vid.read() if whatScreen == 'Main':
faceScan(frame)
return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                                                              157
 
      print('(' + get_date() + ') Encoding faces... 50%')
loadFaces() # Loading photos of face from database and encoding them
print('(' + get_date() + ') Loading completed, initialising GUI... 100%') print('\n- LOG STARTED -')
# Start of main program
current_screen = setup_Screen() # Declares the first screen that will be loaded # print('Time Taken:', str(time.clock())) # Big O Notation of o(n) (linear) current_screen.loop() # Starts the loop of the screen
print('- LOG ENDED -')
try:
print('(' + get_date() + ') Attempting to close database...')
db.close() # Closes the database to ensure no data is changed after the program is closed. print('(' + get_date() + ') Database Closed')
except:
print('(' + get_date() + ') Closing database resulted in an error. Database may already be
closed')
quit()
                     158
 
