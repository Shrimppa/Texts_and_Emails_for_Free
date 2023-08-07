import smtplib
import csv
import os

# This program is able to send texts, and emails for free, and it uses a csv file to do so, you can create a google form to collect data that can then be used to update sending list.

"""
content of the message = Hello there!
sender = From Jelloman

Example output in text, and email form

Text:
From Jelloman
Hey James Bond, Hello there!

Email:
From Jelloman
Hey James Bond, Hello there!  :)


During sending the last 3 characters of text are deleted from texts, so there is a placeholder smile that is seen in emails.

UPDATE: This may have been fixed at some point so results do vary.
"""

def read_dict(csv_file_name, unused_variable_to_pass_pytest=0):
        """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
        with open(csv_file_name) as product:
            next(product)
            file_reader = csv.reader(product)
            product_dict = {}
            value = 1
            for i in file_reader:
                if i != None:
                    a, b, c, d, e, f, g = i
                    a = value
                    product_dict[a] = [b, c, d, e, f]
                value +=1
        return product_dict

def send_messages(product_dictionary, sender_address, sender_pass, subject):

    message_input = input("\n\nEnter the content of the message: ")
    

    for key in product_dictionary:

        first_name, last_name, email, phone_number, carrier = product_dictionary[key]

        first_name = first_name.capitalize()

        last_name = last_name.capitalize()


        if email != "" or phone_number != "":
            if first_name != "" and last_name == "":
                mail_content = "Hey " + first_name + ", " + message_input + "  :)"
                if phone_number != "" and carrier != "":

                    if carrier == "Verizon":
                        carrier = "@vzwpix.com"
                    elif carrier == "T-mobile":
                        carrier = "@tmomail.net"
                    elif carrier == "AT&T":
                        carrier = "@mms.att.net"
                    elif carrier == "Boost Mobile":
                        carrier = "@myboostmobile.com"
                    elif carrier == "Cricket Wireless":
                        carrier = "@mms.cricketwireless.net"
                    elif carrier == "UScellular":
                        carrier = "@mms.uscc.net"

                    phone_number = str(phone_number)
                    
                    if carrier != "@mms.att.net":
                        phone_number = "1" + phone_number + carrier
                    else:
                        phone_number = phone_number + carrier

                    from email.mime.multipart import MIMEMultipart
                    from email.mime.text import MIMEText
                    #The mail addresses and password
                    receiver_address = phone_number
                    #Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = subject   #The subject line
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit()

                if email != "":

                    from email.mime.multipart import MIMEMultipart
                    from email.mime.text import MIMEText
                    #The mail addresses and password
                    receiver_address = email
                    #Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = subject   #The subject line
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit()
            else:
                mail_content = "Hey " + first_name + " " + last_name + ", " + message_input + "  :)"
                if phone_number != "" and carrier != "":


                    if carrier == "Verizon":
                        carrier = "@vzwpix.com"
                    elif carrier == "T-mobile":
                        carrier = "@tmomail.net"
                    elif carrier == "AT&T":
                        carrier = "@mms.att.net"
                    elif carrier == "Boost Mobile":
                        carrier = "@myboostmobile.com"
                    elif carrier == "Cricket Wireless":
                        carrier = "@mms.cricketwireless.net"
                    elif carrier == "UScellular":
                        carrier = "@mms.uscc.net"

                    phone_number = str(phone_number)

                    if carrier != "@mms.att.net":
                        phone_number = "1" + phone_number + carrier
                    else:
                        phone_number = phone_number + carrier

                    from email.mime.multipart import MIMEMultipart
                    from email.mime.text import MIMEText
                    #The mail addresses and password
                    receiver_address = phone_number
                    #Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = subject   #The subject line
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit()

                if email != "":

                    from email.mime.multipart import MIMEMultipart
                    from email.mime.text import MIMEText
                    #The mail addresses and password
                    receiver_address = email
                    #Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = subject   #The subject line
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit() 

    print('\n\nMail has been successfuly sent! Be aware, some messages might not make it through, you will see emails in your inbox for the email you provided, and that is normal. Afterall this is free.\n\n')
    quit = input("\n\nPress any button to quit.")

def send_message(sender_address, sender_pass):

    os.system('cls')

    csv_file_name = input("\nEnter the directory information to the csv file: ")

    csv_file_name = csv_file_name.replace('"', '')

    subject = input("\n\nPlease enter what you want the subject line to be: ") # I.E. The reason you are writing this message

    try:
        file = open(csv_file_name, 'r')
    except FileNotFoundError:
        print("Wrong file or file path")
    else:
        product_dictionary = read_dict(csv_file_name)  

        send_messages(product_dictionary, sender_address, sender_pass, subject)

def save_data():
    
    print("\nWelcome to the free text, and email app! If you haven't already, please follow the tutorial, and setup at https://github.com/Shrimppa/Texts_and_Emails_for_Free")
    
    print("\nThis is the initial setup of the app, prepare to input your Gmail account you are using.\n")

    print('Example email should be like:  example123@gmail.com')

    sender_address = input("\nInput the name of the gmail address you are sending from: ") # Put the gmail address you are sending from here

    print("\nNext you will have to enter your special app passcode.")

    print('\nThe google passcode should be a string of random letters, for example:  qeiwoejoijioe')

    sender_pass = input("\nEnter the special app passcode to login to the google account: ") # Put the passcode to login to that account from Google here
    
    make_save_location(sender_address, sender_pass)

def make_save_location(sender_address, sender_pass):

    new_folder = "C:\Free Emailer Save Location"

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    data = [ ["Gmail", "Password"], [sender_address, sender_pass] ]

    # Create a CSV file named data.csv in the CSV folder and write the data to it
    csv_file = os.path.join(new_folder, "data.csv")
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    os.system('cls')

    input(f"Data has been saved to {csv_file}, you can find the location of the data in the following file explorer location - {new_folder}\data.csv !press enter to continue: ")

def redo_initial_setup():
    os.system('cls')
    delete_data()
    save_data()

def delete_data():
    # Define the name and path of your CSV file
    csv_file = "data.csv"
    csv_path = os.path.join("C:\Free Emailer Save Location", csv_file)

    # Check if the file exists
    if os.path.exists(csv_path):
        # Delete the file using the os.remove function
        os.remove(csv_path)
        # Print a message to confirm that the file has been deleted
        print(f"{csv_file} has been deleted.")

def print_menu():

    print("\nWelcome to the free text, and email app! If you haven't already, please follow the tutorial, and setup at https://github.com/Shrimppa/Texts_and_Emails_for_Free")
       
    print('\nCSV Files information should be orders as the following: "Timestamp","First Name","Last Name","Email","Phone number","Phone carrier","Comments"')

    print('\n1. Send Message')
    print('\n2. Redo Initial Setup')
    print('\n3. Show Saved Data Location')
    print('\n4. Quit\n')

def show_saved_data():

    os.system('cls')

    # Open the CSV file in read mode and load the data into a list
    with open("C:\Free Emailer Save Location\data.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    # Print the data that has been loaded
    print(f"Data has been loaded from C:\Free Emailer Save Location\data.csv\n")

    print(data)

    input("\nPress enter to continue: ")


def load_saved_data():
    # Open the CSV file in read mode and load the data into a list
    with open("C:\Free Emailer Save Location\data.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

def main():

    os.system('cls')

    x = 0

    try:
        data1, data2 = load_saved_data()
    except:
        save_data()
        data1, data2 = load_saved_data()

    sender_address, sender_pass = data2

    while x != 5:

        print_menu()
        
        x = int(input("Enter a number between 1-4: "))
        
        if x == 1:
            send_message(sender_address, sender_pass)
        
        if x == 2:
            redo_initial_setup()
        
        if x == 3:
            show_saved_data()
        
        if x == 4:
            quit
        
        os.system('cls')

if __name__ == "__main__":
    main()