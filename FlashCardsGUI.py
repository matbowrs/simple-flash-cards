import tkinter as tk
from tkinter import *
from random import randint


class GUI (Frame):

    # Honestly no idea what this does
    def __init__(self, master=None):

        # TODO #1. Show the words the user needs to study and the words that the user got correct (SEE 1.1) !!DONE!!
        # TODO #1.1 -> Port it to GUI and create "Done" button to make #1 functional
        # TODO #1.2 -> If 2 pairs are in both good and bad dictionary, automatically move it to bad dictionary !!DONE!!
        # TODO #2. Show dictionary as the user updates it
        # TODO #3. Database functionality
        # TODO #4. Add how many times the user got each pair correct; not critical
        # TODO #5. When showing the final dictionary, remove functioanlity for check_answer()

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
        self.answer_response = tk.Label(text="")
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

        # When you hit the Next button, this function is called and displays next value
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

            # When the user is fully done with the program and wants to show what they got correct
        def show_final_dictionaries():

            good_pair_list = []
            bad_pair_list = []

            self.title["text"] = "What you got correct: "
            self.text_entry_1.grid_forget()
            self.text_entry_2.grid_forget()

            self.answer_response.grid_forget()

            for key in good_dictionary.items():
                good_pair_list.append(key)

            for key in bad_dictionary.items():
                bad_pair_list.append(key)

        # Submit button
        self.submit_button = tk.Button(master, text="Create Pair", command=button_click)
        self.submit_button.grid(column=3, row=6)

        # When the user is ready to quiz him/herself, change the button text on "self.submit_button" to "Check Answer"
        def quiz_click():
            self.submit_button["text"] = "Check Answer"
            self.submit_button["command"] = check_answer

            # Create a button for next_entry
            self.next_entry_button = tk.Button(text="Next", command=next_entry)
            self.next_entry_button.grid(column=4, row=6)

            # Remove the quiz button from the UI
            self.quiz_button.grid_forget()

            # Done button for when user is done taking the quiz; replaces self.quiz_button
            self.done_button = tk.Button(master, text="Done", command=show_final_dictionaries)
            self.done_button.grid(column=3, row=7)

        # Quiz Button for when the user is ready to stop entering values and is ready for a quiz of dictionary
        # values
        self.quiz_button = tk.Button(master, text="Quiz Me!", command=quiz_click)
        self.quiz_button.grid(column=3, row=7)

        # Check if pair is in the dictionary
        def check_exist(dic, key, value):
            try:
                bool_exists = dic[key] == value
                return bool_exists
            except KeyError:
                return False

        # <----- END MAIN FUNCTIONS ----->

        # Function to check answer
        def check_answer():

            key_answer = str(self.text_entry_1.get())  # Get input from text_entry_1
            user_answer = str(self.text_entry_2.get())  # Get input from text_entry_2

            does_pair_exist_bool = check_exist(main_dictionary, key_answer, user_answer)

            # Check if the user_answer and key_answer are paired together in the dictionary
            if does_pair_exist_bool:
                self.answer_response["text"] = "Correct!"
                good_dictionary[user_answer] = key_answer

                # If the entry is in the bad_dictionary{} and the user got it correct, move to good_dictionary{}
                for key in good_dictionary.keys():
                    if key in bad_dictionary.keys():
                        del bad_dictionary[key]

                print("Good Dictionary:")
                print(good_dictionary)
            else:
                self.answer_response["text"] = "Wrong!"
                for i in main_dictionary:
                    if i == key_answer:
                        # Matches the correct words together and stores it in the bad_dictionary{}
                        bad_dictionary[main_dictionary[i]] = key_answer
                        print("Bad Dictionary:")
                        print(bad_dictionary)
                        print("Good Dictionary:")
                        print(good_dictionary)

                # If the pair is found in both the good and the bad dictionary, by default, delete the
                # Entry from the good_dictionary{} and move it to the bad_dictionary, as they got it wrong
                for key in bad_dictionary.keys():
                    if key in good_dictionary.keys():
                        del good_dictionary[key]

                # TODO After this is ported to GUI, make sure to delete!
                print("Bad Dictionary:")
                print(bad_dictionary)
                print("Good Dictionary:")
                print(good_dictionary)


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
