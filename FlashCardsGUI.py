import tkinter as tk
from tkinter import *
from random import randint


class GUI (Frame):

    # Honestly no idea what this does
    def __init__(self, master=None):

        # TODO #1. Show dictionary as the user updates it !!DONE!! but, should I have this? !!!!!!!

        # TODO #1.1 If this feature is kept, problem with dictionary length
        # TODO #2. Database functionality
        # TODO #3. Add how many times the user got each pair correct; not critical & see 7
        # TODO #4. When showing the final dictionary, remove functionality for check_answer()
        # TODO #5. Redo GUI?
        # TODO #6. Which definition is most right / most wrong
        # TODO #7. When user is fully done, add buttons to enter new definitions, edit definitions and quiz again
        # TODO #8. If user gets definition wrong twice, then show the definition
        # TODO #9. Remove all "print()" in final build

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

        # Goes with the button_click() below, declared here for global scope
        self.show_dictionary_as_user_updates = tk.Label(text="")

        # When user clicks button, get text from text_entry_1 & text_entry_2 and put into dictionary
        # Also displays what the user is typing
        def create_pair_function():
            def_1 = str(self.text_entry_1.get())
            def_2 = str(self.text_entry_2.get())
            main_dictionary[def_1] = def_2

            # Show the dictionary as the user enters pairs
            self.store_dict_values = []
            for key in main_dictionary.items():
                self.store_dict_values.append(key)

            self.show_dictionary_as_user_updates["text"] = self.store_dict_values
            self.show_dictionary_as_user_updates.grid(column=7, row=3)
            print(main_dictionary)

        # Submit button
        self.submit_button = tk.Button(master, text="Create Pair", command=create_pair_function)
        self.submit_button.grid(column=3, row=6)

        # Global scope for edit function below
        self.edit_label = tk.Label(text="Enter new values below")
        self.edit_entry_1 = tk.Entry()
        self.edit_entry_2 = tk.Entry()

        def edit_function():
            # Bind all edit objects to grid
            self.edit_label.grid(column=4, row=3)
            self.edit_entry_1.grid(column=4, row=4)
            self.edit_entry_2.grid(column=4, row=5)

            # Change edit_button text to Submit New Entry
            self.edit_button["text"] = "Submit New Entry"

            # Vars to store input from user in the Edit section
            new_edit_var = str(self.edit_entry_1.get())
            new_edit_var_2 = str(self.edit_entry_2.get())

            # Replace the values
            main_dictionary[new_edit_var] = new_edit_var_2

            # Update printed dictionary in UI
            # Show the dictionary as the user enters pairs
            self.store_dict_values = []
            for key in main_dictionary.items():
                self.store_dict_values.append(key)

            self.show_dictionary_as_user_updates["text"] = self.store_dict_values
            self.show_dictionary_as_user_updates.grid(column=7, row=3)

            print(main_dictionary)

        self.edit_button = tk.Button(text="Edit", command=edit_function)
        self.edit_button.grid(column=4, row=6)

        # When the user is ready to quiz him/herself, change the button text on "self.submit_button" to "Check Answer"
        def quiz_click():
            # Hide Edit button
            self.edit_button.grid_forget()

            # Hide Edit button and input
            self.edit_button.grid_forget()
            self.edit_label.grid_forget()
            self.edit_entry_1.grid_forget()
            self.edit_entry_2.grid_forget()

            # Solves a problem with the Edit Function. While hitting Edit, a null pair would be set
            # in the dictionary. This removes that null pair during the quiz.
            if main_dictionary[""] == "":
                del main_dictionary[""]

            # Hides the dictionary entries
            self.show_dictionary_as_user_updates.grid_forget()

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

        # When you hit the Next button, this function is called and displays next value; comes during quiz
        def next_entry():
            list_of_keys = []
            my_list = []

            for x in main_dictionary:
                my_list.append(x)

            list_of_keys.append(self.text_entry_1.get())

            # Used for selection when choosing a value for quizzing the user
            rand_num = randint(0, len(main_dictionary) - 1)

            # If the last entry and the new entry-to-be are the same, make the new entry-to-be different
            while list_of_keys[len(list_of_keys) - 1] == my_list[rand_num]:
                rand_num = randint(0, len(main_dictionary) - 1)

            set_text(my_list[rand_num])
            print(my_list[rand_num])

        # Check if pair is in the dictionary
        def check_exist(dic, key, value):
            try:
                bool_exists = dic[key] == value
                return bool_exists
            except KeyError:
                return False

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
                print("Bad Dictionary:")
                print(bad_dictionary)
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

        # When the user is fully done with the program and wants to show what they got correct
        def show_final_dictionaries():
            # Hide these buttons
            self.quiz_button.grid_forget()
            self.submit_button.grid_forget()

            good_pair_list = []
            bad_pair_list = []

            self.title["text"] = "What you got correct: "
            self.title_2 = tk.Label(text="What you got wrong: ")
            self.title_2.grid(column=3, row=4)

            # Delete all of these fields
            self.text_entry_1.grid_forget()
            self.text_entry_2.grid_forget()
            self.answer_response.grid_forget()

            # Store everything in the good dictionary into the good list
            for key in good_dictionary.items():
                good_pair_list.append(key)

            # Store everything in the bad dictionary into the bad list
            for key in bad_dictionary.items():
                bad_pair_list.append(key)

            # Show the good pairs in the UI
            self.good_dictionary_label = tk.Label(text=good_pair_list)
            self.good_dictionary_label.grid(column=3, row=3)

            # Show the bad pairs in the UI
            self.bad_dictionary_label = tk.Label(text=bad_pair_list)
            self.bad_dictionary_label.grid(column=3, row=5)

        # <----- END MAIN FUNCTIONS ----->


if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
