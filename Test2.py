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
        # TODO #4. Redo GUI?
        # TODO #5. Which definition is most right / most wrong
        # TODO #6. When user is fully done, add buttons to enter new definitions, edit definitions and quiz again
        # TODO #7. If user gets definition wrong twice, then show the definition
        # TODO #8. Remove all "print()" in final build
        # TODO #9. Try to fix { "" : "" } problem in the dictionary UI. It is fixed in the Quiz section

        # <----- BEGIN GLOBAL VARIABLES ----->

        # Append button, used here for scope. Used with def append_to_dictionary()
        self.append_button = tk.Button(text="Add to existing set")

        # Goes with the button_click() below, declared here for global scope
        self.show_dictionary_as_user_updates = tk.Label(text="")

        # Global scope for edit function below
        self.edit_label = tk.Label(text="Enter new values below")
        self.edit_entry_1 = tk.Entry()
        self.edit_entry_2 = tk.Entry()

        # Declare command, used in quiz_click()
        self.done_button = tk.Button(master, text="", command="")

        # Pre-made button for when user selects pre-made decks
        self.face_button = tk.Button(text="Parts of the Face (RUS/ENG)", command="")

        # Label for pre-made
        self.new_title = tk.Label(text="Select from  the pre-made decks below")

        # <----- END GLOBAL VARIABLES ----->

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

        # <-- BEGIN ENTRY FIELDS -->
        self.text_entry_1 = tk.Entry(text="")
        self.text_entry_1.grid(column=3, row=3)

        self.text_entry_2 = tk.Entry(text="")
        self.text_entry_2.grid(column=3, row=4)
        # <-- END ENTRY FIELDS -->

        # <----- BEGIN MAIN FUNCTIONS ----->
        self.main_button = tk.Button(text="Create New Deck", command="")
        self.pre_made_button = tk.Button(text="Select From Pre-Made", command="")  # TODO Make pre-made things

        # Show buttons again after the home page is clicked
        def button_clicked_for_main_page():
            self.title.grid(column=3, row=0)
            self.text_entry_1.grid(column=3, row=3)
            self.text_entry_2.grid(column=3, row=4)
            self.submit_button.grid(column=3, row=6)
            self.quiz_button.grid(column=3, row=7)
            self.main_button.grid_forget()
            self.pre_made_button.grid_forget()

        # "Home page"
        def main_page():
            self.append_button.grid_forget()
            self.submit_button.grid_forget()
            self.quiz_button.grid_forget()
            self.text_entry_1.grid_forget()
            self.text_entry_2.grid_forget()
            self.title.grid_forget()

            self.main_button.grid(column=3, row=2)
            self.pre_made_button.grid(column=3, row=3)

            # on main_button click, run create_pair_function
            self.main_button["command"] = button_clicked_for_main_page

        # Function for setting text
        def set_text(text):
            self.text_entry_1.delete(0, END)
            self.text_entry_1.insert(0, text)
            return

        # When user clicks button, get text from text_entry_1 & text_entry_2 and put into dictionary
        # Also displays what the user is typing
        def create_pair_function():
            self.append_button.grid_forget()

            def_1 = str(self.text_entry_1.get())
            def_2 = str(self.text_entry_2.get())
            main_dictionary[def_1] = def_2

            # Solves problem if the user goes to quiz right away and doesn't need to edit. Why? I don't know but it
            # works so don't touch it :)
            main_dictionary[""] = ""

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

        # Allows edits to be performed on the second definition only; requires the first definition (the key) to work!
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

        # Edit button
        self.edit_button = tk.Button(text="Edit", command=edit_function)
        self.edit_button.grid(column=4, row=6)

        # When the user is ready to quiz him/herself, change the button text on "self.submit_button" to "Check Answer"
        def quiz_click():
            # Change Title header
            self.title["text"] = "Quiz Time!"

            # Hide Edit button and input
            self.edit_button.grid_forget()
            self.edit_button.grid_forget()
            self.edit_label.grid_forget()
            self.edit_entry_1.grid_forget()
            self.edit_entry_2.grid_forget()
            self.append_button.grid_forget()
            # Solves a problem with the Edit Function. While hitting Edit, a null pair would be set
            # in the dictionary. This removes that null pair during the quiz.
            if len(main_dictionary) > 0:
                if main_dictionary[""] == "":
                    del main_dictionary[""]
            else:
                pass

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
            self.done_button["text"] = "Done"
            self.done_button["command"] = show_final_dictionaries
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

        def append_to_dictionary():
            # Attach to grid
            self.append_button.grid(column=3, row=8)

        # Home page is down here. Yeah, I know...
        main_page()

        # For scope, goes with below function
        self.title_2 = tk.Label(text="What you got wrong: ")

        # For Scope
        self.good_dictionary_label = tk.Label(text="")
        self.bad_dictionary_label = tk.Label(text="")

        # When the user is fully done with the program and wants to show what they got correct
        def show_final_dictionaries():
            # Hide these buttons
            self.quiz_button.grid_forget()
            self.submit_button.grid_forget()
            self.text_entry_1.grid_forget()
            self.text_entry_2.grid_forget()
            self.answer_response.grid_forget()
            self.edit_button.grid_forget()

            good_pair_list = []
            bad_pair_list = []

            self.title["text"] = "What you got correct: "
            self.title_2.grid(column=3, row=4)

            # Store everything in the good dictionary into the good list
            for key in good_dictionary.items():
                good_pair_list.append(key)

            # Store everything in the bad dictionary into the bad list
            for key in bad_dictionary.items():
                bad_pair_list.append(key)

            # Show the good pairs in the UI
            self.good_dictionary_label["text"] = good_pair_list
            self.good_dictionary_label.grid(column=3, row=3)

            # Show the bad pairs in the UI
            self.bad_dictionary_label["text"] = bad_pair_list
            self.bad_dictionary_label.grid(column=3, row=5)

            # Show append button at the end
            append_to_dictionary()

        # <----- END MAIN FUNCTIONS ----->

        # Pre-made Decks
        # Hides main homepage
        def click_pre_made():
            self.main_button.grid_forget()
            self.pre_made_button.grid_forget()
            self.edit_button.grid_forget()
            self.new_title.grid(column=1, row=0)
            self.face_button.grid(column=1, row=1)

        # Hides buttons when passed as an argument
        def hide_pre_made_button(name_of_button):
            name_of_button.grid_forget()

        # When clicked, run click_pre_made()
        self.pre_made_button["command"] = click_pre_made

        # Setup for showing Face deck (hiding components, changing title, etc)
        def pre_made_face_setup():
            hide_pre_made_button(self.face_button)

            self.new_title["text"] = "Russian <-> English Parts of Face"
            self.face_button.grid_forget()

        self.face_button["command"] = pre_made_face_setup

        dict_rus_eng_face = {
            "лицо": "face",
            "голова": "head",
            "волосы": "hair",
            "лоб": "forehead",
            "бровь": "eyebrow",
            "ухо": "ear",
            "глаз": "eye",
            "рот": "mouth",
            "нос": "nose",
            "шея": "neck",
            "зубы": "teeth",
            "подбородок": "chin"
        }

        def pass_in_dictionary(this_dict):
            this_dict

if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
