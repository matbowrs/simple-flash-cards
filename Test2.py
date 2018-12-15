import tkinter as tk
from tkinter import *
from random import randint


class GUI (Frame):

    def __init__(self, master=None):

        # <-- BEGIN DICTIONARY DECLARATIONS -->

        # Declare main dictionary
        main_dictionary = {}

        # If user gets definition wrong, pair is sent here
        bad_dictionary = {}

        # If user gets definition correct, pair is sent here
        good_dictionary = {}

        # <-- END DICTIONARY DECLARATIONS -->

        # No idea what this does
        Frame.__init__(self, master)
        self.grid()

        # ----- GUI -----
        window = tk.Tk()

        # Title of the application
        window.title("Flash Cards")

        # Window dimensions
        # window.geometry("700x400")

        # <--- START LABELS --->
        self.title = tk.Label(text="Enter the first word/definition, followed by the second.")
        self.title.grid(column=3, row=0)

        # Label for showing whether the answer was correct or not
        self.answer_response = tk.Label(text="Correct Or Not?")
        self.answer_response.grid(column=3, row=5)
        # <--- END LABELS --->

        # <-- Begin Entry fields -->
        self.text_entry_1 = tk.Entry(text="")
        self.text_entry_1.grid(column=3, row=3)

        self.text_entry_2 = tk.Entry(text="")
        self.text_entry_2.grid(column=3, row=4)
        # <-- End Entry Fields -->

        # <----- BEGIN MAIN FUNCTIONS ----->

        # Function for setting text
        def set_text(text):
            self.text_entry_1.delete(0, END)
            self.text_entry_1.insert(0, text)
            return

        # Function for changing text
        def change_text():
            index_zero_list = [elem for elem in main_dictionary.values()]  # Puts all entries of text_entry_2 into list
            # TODO index_zero_list[0] was a test to see if the string would change. It passed, now need
            # TODO to get all text_entry_2 entries looping through
            set_text(index_zero_list[0])
            #self.text_entry_1.config(state=DISABLED)

        # TODO ???? NEED?
        def next_entry():
            rand_num = randint(0, len(main_dictionary) - 1)
            my_list = []

            for x in main_dictionary:
                my_list.append(x)
            print(my_list[rand_num])
            set_text(my_list[rand_num])

        # When user clicks button, get text from text_entry_1 & text_entry_2 and put into dictionary
        def button_click():
            def_1 = str(self.text_entry_1.get())
            def_2 = str(self.text_entry_2.get())
            main_dictionary[def_1] = def_2
            print(main_dictionary)

        # Submit button
        self.submit_button = tk.Button(master, text="Create Pair", command=button_click)
        self.submit_button.grid(column=3, row=6)

        # When the user is ready to quiz him/herself, change the button text on "self.submit_button" to "Check Answer"
        def quiz_click():
            self.submit_button["text"] = "Check Answer"
            self.submit_button["command"] = check_answer

            # Create a button for next_entry
            next_entry_button = tk.Button(text="Next", command=next_entry)
            next_entry_button.grid(column=4, row=6)

            change_text()

        # Check if pair is in the dictionary
        def check_exist(dic, key, value):
            try:
                return dic[key] == value
            except KeyError:
                return False
        # <----- END MAIN FUNCTIONS ----->

        # Quiz Button for when the user is ready to stop entering values and is ready for a quiz of dictionary
        # values
        self.quiz_button = tk.Button(master, text="Quiz Me!", command=quiz_click)
        self.quiz_button.grid(column=3, row=7)

        # Function to check answer
        def check_answer():
            num = randint(0, len(main_dictionary.values()))
            list_for_keys = []


            # set_text(list_for_keys[num])

            key_answer = str(self.text_entry_1.get())
            user_answer = str(self.text_entry_2.get())

            does_pair_exit_bool = check_exist(main_dictionary, key_answer, user_answer)

            # Check if the user_answer and key_answer are paired together in the dictionary
            # For loop started here
            # TODO error if a key is entered ( i.e. text_entry_1 = 'Russia' | text_entry_2 = 'Russia' -> Error )
            if does_pair_exit_bool:
                self.answer_response["text"] = "Correct!"
                good_dictionary[user_answer] = key_answer

            else:
                self.answer_response["text"] = "Wrong!"
                bad_dictionary[user_answer] = key_answer


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
