import smtplib
import csv

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

def send_message(product_dictionary, sender_address, sender_pass, subject):

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

def main():

    print("\n\nWelcome to the free text, and email app! If you haven't already, please follow the tutorial, and setup at ")
       
    print('\nCSV Files information should be orders as the following: "Timestamp","First Name","Last Name","Email","Phone number","Phone carrier","Comments"')
    
    print('\nCSV Filepath should look like this.     C:\MyDirve\Downloads\ContactInfo.csv')
    print('\nCSV Filepath should not look like this.     "C:\MyDirve\Downloads\ContactInfo.csv" ')


    csv_file_name1 = input("\nEnter the directory information to the csv file: ")

    print('\n\nExample email should be like:  example123@gmail.com')

    sender_address = input("\nInput the name of the gmail address you are sending from: ") # Put the gmail address you are sending from here

    print('\n\nThe google passcode should be a string of random letters, for example:  qeiwoejoijioe')

    sender_pass = input("\nEnter the special app passcode to login to the google account: ") # Put the passcode to login to that account from Google here

    subject = input("\n\nPlease enter what you want the subject line to be: ") # I.E. The reason you are writing this message

    try:
        file = open(csv_file_name1, 'r')
    except FileNotFoundError:
        print("Wrong file or file path")
    else:
        product_dictionary = read_dict(csv_file_name1)  

        send_message(product_dictionary, sender_address, sender_pass, subject)

if __name__ == "__main__":
    main()