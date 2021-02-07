#!/usr/bin/env python3

################################################################
# Example of using Gmail API
################################################################

from datetime import datetime
from dotenv import load_dotenv
import helpers
import logging
import os

def load_env():
    
    load_dotenv()

    return_data = {}
    try:
        return_data['client_id'] = os.environ["CLIENT_ID"]
        return_data['client_secret'] = os.environ["CLIENT_SECRET"]
        return_data['refresh_token'] = os.environ["REFRESH_TOKEN"]
        return_data['email_user'] = os.environ["EMAIL_USER"]
        return_data['email_password'] = os.environ["EMAIL_PASSWORD"]
        return_data['email_to'] = os.environ["EMAIL_TO"]
    except KeyError:
        logging.error("Unable to get environmental variables")
    except Exception as e:
        logging.error("Generic catch: Unable to get environmental variables")
        logging.error("Generic catch: " + str(e))
    return return_data

def main():
    
    helpers.load_logging()
    
    logging.info("Starting...")


    total_budget = 2800

    logging.info("Loading environment vars...")
    env = load_env()
    client_id = env['client_id']
    client_secret = env['client_secret']
    refresh_token = env['refresh_token']
    email_user = env['email_user']
    email_password = env['email_password']
    email_to = env['email_to']
    logging.info("Loading environment vars...completed")


    # get messages
    gmail_access_token = helpers.get_access_token(client_id, client_secret, refresh_token)
    my_messages = helpers.get_messages(gmail_access_token['access_token'])
    #logging.info(f"Messages: {my_messages}")

    if my_messages['resultSizeEstimate'] == 0:
        logging.info("no emails")
    else:

        email_count = my_messages['resultSizeEstimate']
        
        if int(email_count) > 0:
            logging.info(f"Found {email_count} emails to go through")
        else:
            logging.info("No messages to go through")
            exit(0)

        results = 0
        counter = 0

        emails = my_messages['messages']
        for email in emails:
            
            counter += 1

            gmail_id = email['id']
            current_email = helpers.get_single_email(gmail_id, gmail_access_token['access_token'])
            
            snippet = current_email["snippet"]
            #logging.info(f"Snippet: {snippet}")
            logging.info("Seeing if this message matches the automated email we are looking for")
            if snippet.find("Available Credit Alert") != -1: 
                logging.info("Email subject matched the phrase: Available Credit Alert")
                
                read = helpers.read_message(current_email)
                logging.info(f"Card: {read['card']}")
                logging.info(f"Amount: ${read['amount']}")

                if read['card'] == "buying_cc":
                    amount_spent = 5500 - float(read['amount'])
                else:
                    amount_spent = 4500 - float(read['amount'])
                amount_spent = round(amount_spent)
                logging.info(f"Amount spent: ${amount_spent}")
                results += amount_spent

                trash = helpers.trash_single_email(gmail_id, gmail_access_token['access_token'])
                if trash == None:
                    logging.info("ERROR: Unable to delete email")
                else:
                    logging.info("Email moved to trash so it won't confuse the script for the next day")
            
            else:
                logging.info("Email subject did not have the phrase: Available Credit Alert")

        logging.info(f"Total spent on both credit cards combined: ${results}")

        days_until_payday = helpers.get_days_until_payday()
        today = datetime.today()
        day_of_month = today.day

        upcoming_bills = []

        # This section will be dependent on what days your bills come out
        # and what bills you have, but for an example, lets say you have the following bills:
        
        # 1 - Internet - $105
        # 6 - Groceries - $200
        # 13 - Groceries - $200
        # 16 - Water - $90
        # 16 - Cell_Phone - $45
        # 20 - Groceries - $200
        # 24 - Cable - $11
        # 27 - Electric - $200
        # 27 - Groceries - $200
        # 28 - Auto_Ins - $176

        # What the script will do is tell you which ones are due before the first of the next month
        # in conjunction with your current credit card usage


        if day_of_month >=1 and day_of_month <= 5:
            upcoming_bill_amount = 1455
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('06 - Groceries - $200<br>')
            upcoming_bills.append('13 - Groceries - $200<br>')
            upcoming_bills.append('16 - Water - $90<br>')
            upcoming_bills.append('16 - Cell_Phone - $45<br>')
            upcoming_bills.append('20 - Groceries - $200<br>')
            upcoming_bills.append('24 - Cable - $11<br>')
            upcoming_bills.append('27 - Electric - $200<br>')
            upcoming_bills.append('27 - Groceries - $200<br>')
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $1455<br>')
        elif day_of_month >=6 and day_of_month <= 12:
            upcoming_bill_amount = 1255
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('13 - Groceries - $200<br>')
            upcoming_bills.append('16 - Water - $90<br>')
            upcoming_bills.append('16 - Cell_Phone - $45<br>')
            upcoming_bills.append('20 - Groceries - $200<br>')
            upcoming_bills.append('24 - Cable - $11<br>')
            upcoming_bills.append('27 - Electric - $200<br>')
            upcoming_bills.append('27 - Groceries - $200<br>')
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $1255<br>')
        elif day_of_month ==13:
            upcoming_bill_amount = 1055
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('16 - Water - $90<br>')
            upcoming_bills.append('16 - Cell_Phone - $45<br>')
            upcoming_bills.append('20 - Groceries - $200<br>')
            upcoming_bills.append('24 - Cable - $11<br>')
            upcoming_bills.append('27 - Electric - $200<br>')
            upcoming_bills.append('27 - Groceries - $200<br>')
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $1055<br>')
        elif day_of_month >=14 and day_of_month <= 15:
            upcoming_bill_amount = 1042
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('16 - Water - $90<br>')
            upcoming_bills.append('16 - Cell_Phone - $45<br>')
            upcoming_bills.append('20 - Groceries - $200<br>')
            upcoming_bills.append('24 - Cable - $11<br>')
            upcoming_bills.append('27 - Electric - $200<br>')
            upcoming_bills.append('27 - Groceries - $200<br>')
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $1042<br>')
        elif day_of_month >=16 and day_of_month <= 19:
            upcoming_bill_amount = 907
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('20 - Groceries - $200<br>')
            upcoming_bills.append('24 - Cable - $11<br>')
            upcoming_bills.append('27 - Electric - $200<br>')
            upcoming_bills.append('27 - Groceries - $200<br>')
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $907<br>')
        elif day_of_month >=20 and day_of_month <= 23:
            upcoming_bill_amount = 707
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('24 - Cable - $11<br>')
            upcoming_bills.append('27 - Electric - $200<br>')
            upcoming_bills.append('27 - Groceries - $200<br>')
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $707<br>')
        elif day_of_month >=24 and day_of_month <= 26:
            upcoming_bill_amount = 696
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('27 - Electric - $200<br>')
            upcoming_bills.append('27 - Groceries - $200<br>')
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $696<br>')
        elif day_of_month ==27:
            upcoming_bill_amount = 281
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('28 - Auto_Ins. - $176<br>')
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $281<br>')
        elif day_of_month >=28 and day_of_month <= 31:
            upcoming_bill_amount = 105
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('01 - Internet - $105<br>')
            upcoming_bills.append('Total: $105<br>')
        else:
            upcoming_bill_amount = 0
            results_with_bills = results + upcoming_bill_amount
            upcoming_bills.append('None!<br>')

        logging.info(f"Upcoming bill amount: ${upcoming_bill_amount}")
        logging.info(f"Results with bills: ${results_with_bills}")

        budget = total_budget - results_with_bills
        logging.info(f"Budget => ${total_budget} - (current credit card balance + upcoming bill amount): ${budget}")



        if counter >= 1:
            
            # Send an email
            upcoming_bills_print= '\n'.join(upcoming_bills)

            subject = "Daily Budget Automated Task"
            body = """
            <html>
            <head>
            </head>
                <body>
                <p style="color:#006400"><b>Days until payoff:</b></p>{}<br />
                <p style="color:#006400"><b>Budget before payday:</b>
                </p>+ ${} Monthly budget<br />
                - ${} Current combined balance<br />
                - ${} Upcoming bills<br />
                =========================================<br />
                <b>${}</b> Spending balance available
                <p style="color:#006400"><b>Upcoming Bills:</b></p>
                {}
                </body>
            </html>
            """.format(days_until_payday, total_budget, results, upcoming_bill_amount, budget, upcoming_bills_print)
            email = helpers.send_email(
                email_user, 
                email_password, 
                email_to, 
                subject, 
                body
            )
            if email == "completed":
                logging.info(f"Email sent from {email_user} to {email_to}")
            else:
                logging.info(f"ERROR: Email failed to send from {email_user} to {email_to}")

            # Send a SMS message
            subject = "My_Budget"
            body = f"Budget before payday: ${budget}"
            email_to = "9999999999@txt.att.net"
            
            email = helpers.send_email(
                email_user, 
                email_password, 
                email_to, 
                subject, 
                body
            )
            if email == "completed":
                logging.info(f"Email sent from {email_user} to {email_to}")
            else:
                logging.info(f"ERROR: Email failed to send from {email_user} to {email_to}")
        
        else:
        
            # Send an email
            subject = "Daily Budget Automated Task"
            body = "Email didn't arrive"
            
            email = helpers.send_email(
                email_user, 
                email_password, 
                email_to, 
                subject, 
                body
            )
            if email == "completed":
                logging.info(f"Email sent from {email_user} to {email_to}")
            else:
                logging.info(f"ERROR: Email failed to send from {email_user} to {email_to}")

            # Send a SMS message
            subject = "My_Budget"
            body = "Email didn't arrive"
            email_to = "9999999999@txt.att.net"
            
            email = helpers.send_email(
                email_user, 
                email_password, 
                email_to, 
                subject, 
                body
            )
            if email == "completed":
                logging.info(f"Email sent from {email_user} to {email_to}")
            else:
                logging.info(f"ERROR: Email failed to send from {email_user} to {email_to}")


if __name__ == '__main__':
    main()