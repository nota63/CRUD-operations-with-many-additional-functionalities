# CRUD with many functionalities
import re
import pyautogui as pg
import pyttsx3
import time
import requests
from plyer import notification


# Authentication system
def authenticate():
    engine = pyttsx3.init()
    print("Welcome! please Enter Your Email To Login!")
    email = input("Enter Your Email:")
    if len(email) <= 31:
        if '@' in email:
            if email[-3] or [-2] == "com" in email:
                if email.lower():
                    if "." in email:
                        print(" Email -- Verified")
                        sentence = (f"Congratulations Dear {email}\n Your Email Has Been Verified\n You Can "
                                    f"Process Further\n Happy journey!")
                        engine.say(sentence)
                        engine.runAndWait()
                        return True


                    else:
                        print("Your Email Does not have '.' !\n invalid Email! try Again")
                else:
                    print("email should be have in lower cases only!")
            else:
                print(" 'com' should be have in -2. or -3 indexes!")
        else:
            print("email should be have @ !")
    else:
        print("the length of the email should be have less than 31!")
    return False


# Done


class Notes:
    def __init__(self):
        self.notes = []

    # ADD NOTES
    def add_notes(self):
        engine = pyttsx3.init()
        print("Add Your Notes Here maximum 10000 Characters Only!")
        note = input("Enter Notes:")
        if len(note) <= 10000:
            print("Getting Info....")
            time.sleep(4)
            print("Adding Note...")
            time.sleep(4)
            self.notes.append(note)
            print("Note Has Been Added!")
            note2 = "Successfully added  Note to database"
            engine.say(note2)
            engine.runAndWait()
        else:
            print("Characters limit reached!")

    # SEARCH NOTES
    def search_notes(self):
        print("Enter One keyword To Search your Notes:")
        pattern = input("Enter Keyword to Match:")
        text = self.notes
        print("Searching your Keyword..")
        time.sleep(5)
        matches = [note for note in self.notes if re.search(pattern, note)]
        if matches:
            print("Keyword matched. Here are the matching notes:")
            for match in matches:
                print(match)
        else:
            print("Keyword didn't match any notes!")

    # DELETE NOTES
    def delete_notes(self):
        print("Loading Data..")
        time.sleep(2)
        print("Data Loaded")

        if not self.notes:
            print("There are no notes to delete.")
            return

        for index, note in enumerate(self.notes):
            print(f"{index + 1}: {note}")

        try:
            user = int(input("Enter Index To Delete Note:"))
            if 1 <= user <= len(self.notes):
                removed_note = self.notes.pop(user - 1)
                print(f"Removing your note '{removed_note}'")
                time.sleep(2)
                print(f"Note '{removed_note}' has been removed!")
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

    # VIEW NOTES:
    def view_notes(self):
        while True:
            try:
                if self.notes:
                    print("Your Notes Will Appear Here\n redirecting To Login Page...")
                    time.sleep(5)
                    var = int(input('Enter Your Password To view Notes:'))
                    print('Checking password..')
                    time.sleep(5)
                    if var == 1234:
                        print("Password verified")
                        print("Checking Notes Status...")
                        time.sleep(5)
                        print("Status Checked")
                        print("Notes Found")
                        if self.notes:
                            for index, key in enumerate(self.notes):
                                print(f"{index + 1}: {key}")
                        else:
                            print("There Are no noes to show!")
                    else:
                        print("Wrong Password!")
            except ValueError:
                print("ValueError")

            except IndexError:
                print("indexError")

            except WindowsError:
                print("WindowsError")

    # REQUESTS MODULE SECTION
    def download_source_code(self):
        while True:
            try:
                print("Welcome to HackerWorld! Just Enter An Url Of The Site And Get The Entire frontend Source Code!")
                input("Press Enter To Start:")
                print('Starting..')
                time.sleep(2)
                print('redirecting To Urls page..')
                time.sleep(3)
                url = input("enter url of the website:")
                r = requests.get(url)
                html = r.text
                print("Getting Info....\n Sending Requests To HackerWorld wait for accomplish..")
                time.sleep(3)
                print("Access Granted!")
                print("Loading....")
                print(html)
            except ValueError:
                print("valueError")
            except IndexError:
                print("IndexError")
            except WindowsError:
                print("windowsError")

    # for download images
    def download_images(self, names):
        while True:
            try:
                engine = pyttsx3.init()
                print("download Any Image by pasting url")
                url = input("Enter Image URL:")
                print("Getting Info...")
                time.sleep(5)
                print("Accessing..")
                time.sleep(2)
                response = requests.get(url)
                with open("downloaded_Image.png", 'wb') as f:
                    f.write(response.content)
                    print(f"File '{url}' Downloaded!")
                    for name in names:
                        sentence = f"Image {url} Downloaded\n you can view it\n in your project folder"
                        engine.say(sentence)
                    engine.runAndWait()
            except IndexError:
                print("indexError")
            except ValueError:
                print("ValueError")
            except IsADirectoryError:
                print("isDirectoryError")


def main():
    no = Notes()
    if authenticate():
        while True:
            try:
                menu = ("<<menu>>\n1.Add_Notes\n2.search_notes\n3.delete_notes\n4.view_notes\n5"
                        ".download_source_code\n6.Download_images")
                print(menu.title())
                variable = int(input("Enter An Index to Start!:"))
                if variable == 1:
                    no.add_notes()
                elif variable == 2:
                    no.search_notes()
                elif variable == 3:
                    no.delete_notes()
                elif variable == 4:
                    no.view_notes()
                elif variable == 5:
                    no.download_source_code()
                elif variable == 6:
                    no.download_images()
                elif variable == 7:
                    print("Exited")
                    break
            except ValueError:
                print("ValueError")
            except IndexError:
                print("IndexError")
            except WindowsError:

                print("WindowsError")


if __name__ == '__main__':
    main()
