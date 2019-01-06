import tkinter as tk
from tkinter import *
from random import randint
import sqlite3
from sqlite3 import Error
from operator import itemgetter


''' <----- DATABASE -----> '''
conn = sqlite3.connect('flashcard_database.db')

c = conn.cursor()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_cards(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM cards")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_card_by_category(conn, category):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()

    cur.execute("SELECT * FROM cards WHERE category='" + category + "'")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = "./flashcard_database.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_card_by_category(conn, 'default')

        print("2. Query all tasks")
        select_all_cards(conn)


main()


''' <----- END DATABASE -----> '''


''' <----- GUI And Logic ----->'''


class GUI (Frame):

    # Honestly no idea what this does
    def __init__(self, master=None):

        # TODO #1. Show dictionary as the user updates it !!DONE!! but, should I have this? !!!!!!!
        # TODO #1.1 If this feature is kept, problem with dictionary length

        # TODO #2. Database functionality * DOING *
        # TODO #3. Redo GUI?
        # TODO #4. When user is fully done, add buttons to enter new definitions, edit definitions and quiz again
        # TODO #5. Remove all "print()" in final build
        # TODO #6. Try to fix { "" : "" } problem in the dictionary UI. It is fixed in the Quiz section
        # TODO #7. If the user enters the same deck topic, append the new definitions into the existing deck topic
        # TODO #8. When user inputs which topic to study during quiz, pull correct topic from database

        # <----- BEGIN GLOBAL VARIABLES ----->

        # Label for deck entry
        self.label_for_deck_topic = tk.Label(text="Create a name for your deck:")

        # Entry field for deck topic
        self.entry_for_deck_topic = tk.Entry()

        # Button for creating a new topic for the deck
        self.create_deck_topic_button = tk.Button(text="Create!", command="")

        # Append button, used here for scope. Used with def append_to_dictionary()
        self.append_button = tk.Button(text="Add to existing set")

        # Goes with the button_click() below, declared here for global scope
        self.show_dictionary_as_user_updates = tk.Label(text="")

        # Entry for quiz topic
        self.quiz_topic_entry = tk.Entry()
        # Button for quiz topic
        self.quiz_topic_button = tk.Button(text="Submit", command="")

        # Global scope for edit function below
        self.edit_label = tk.Label(text="Enter new values below")
        self.edit_entry_1 = tk.Entry()
        self.edit_entry_2 = tk.Entry()

        # Declare command, used in quiz_click()
        self.done_button = tk.Button(master, text="", command="")

        # Globals for pre-made deck
        # Pre-made button for when user selects pre-made decks
        self.face_button = tk.Button(text="Parts of the Face (RUS/ENG)", command="")

        # Label for pre-made
        self.new_title = tk.Label(text="Select from  the pre-made decks below")

        # Inside pre-made, review button
        self.review_button = tk.Button(text="Review Words", command="")

        # <----- END GLOBAL VARIABLES -----

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
        self.create_new_deck_button = tk.Button(text="Create New Deck", command="")
        self.pre_made_button = tk.Button(text="Select From Pre-Made", command="")  # TODO Make pre-made things

        def create_topic_for_deck():
            self.create_new_deck_button.grid_forget()
            self.pre_made_button.grid_forget()

            self.label_for_deck_topic.grid(column=1, row=0)
            self.entry_for_deck_topic.grid(column=1, row=1)
            self.create_deck_topic_button.grid(column=1, row=2)

            self.create_deck_topic_button["command"] = button_clicked_for_main_page

        # As method says; used with the category and sending data to database
        def get_card_deck_name():
            name = str(self.entry_for_deck_topic.get())
            return name

        # Prompts user to enter information
        def button_clicked_for_main_page():
            self.title.grid(column=3, row=0)
            self.text_entry_1.grid(column=3, row=3)
            self.text_entry_2.grid(column=3, row=4)
            self.submit_button.grid(column=3, row=6)
            self.quiz_button.grid(column=3, row=7)
            self.edit_button.grid(column=4, row=6)

            self.create_new_deck_button.grid_forget()
            self.pre_made_button.grid_forget()
            self.label_for_deck_topic.grid_forget()
            self.entry_for_deck_topic.grid_forget()
            self.create_deck_topic_button.grid_forget()

            # On click, get the card deck topic name
            get_card_deck_name()

        # "Home page"
        def main_page():
            self.append_button.grid_forget()
            self.submit_button.grid_forget()
            self.quiz_button.grid_forget()
            self.text_entry_1.grid_forget()
            self.text_entry_2.grid_forget()
            self.title.grid_forget()
            self.edit_button.grid_forget()

            self.create_new_deck_button.grid(column=3, row=2)
            self.pre_made_button.grid(column=3, row=3)

            # on main_button click, run create_pair_function
            self.create_new_deck_button["command"] = create_topic_for_deck

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

        # Asks user for category, then retrieve the database
        def topic_for_quiz():
            # Hide Edit button and input
            self.edit_button.grid_forget()
            self.edit_button.grid_forget()
            self.edit_label.grid_forget()
            self.edit_entry_1.grid_forget()
            self.edit_entry_2.grid_forget()
            self.append_button.grid_forget()
            self.text_entry_1.grid_forget()
            self.text_entry_2.grid_forget()
            self.quiz_button.grid_forget()
            self.submit_button.grid_forget()

            self.title["text"] = "Enter the topic for the quiz (the name you called the decks)"

            self.quiz_topic_entry.grid(column=3, row=2)
            self.quiz_topic_button.grid(column=3, row=3)

        def retrieve_categories_from_database():
            user_category = str(self.quiz_topic_entry.get())

            c.execute("SELECT firstSide, secondSide FROM cards WHERE category = '" + user_category + "'")

            rows = c.fetchall()

            # Removes the tuple pairings from "rows" and puts everything into a list of strings
            result = []
            for t in rows:
                for x in t:
                    result.append(x)

            # Put everything from result[] into a dictionary
            updated_dictionary = dict(t for t in zip(result[::2], result[1::2]))

            print("updated dictionary")
            print(updated_dictionary)

            print("rows")
            print(rows)
            print("for row in rows")
            for row in rows:
                print(row)

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
            self.quiz_topic_button.grid_forget()
            self.quiz_topic_entry.grid_forget()

            self.text_entry_1.grid(column=3, row=2)
            self.text_entry_2.grid(column=3, row=3)
            self.submit_button.grid(column=3, row=4)

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

            # Bind next_entry_button
            self.next_entry_button.grid(column=4, row=4)

            # Remove the quiz button from the UI
            self.quiz_button.grid_forget()

            # Done button for when user is done taking the quiz; replaces self.quiz_button
            self.done_button["text"] = "Done"
            self.done_button["command"] = show_final_dictionaries
            self.done_button.grid(column=3, row=5)

            # Send to database when user clicks on Quiz Me
            for i in main_dictionary:
                c.execute("INSERT INTO cards VALUES ('" + i + "','" + main_dictionary[
                    i] + "','" + get_card_deck_name() + "','" + "image" + "')")
                conn.commit()

            retrieve_categories_from_database()

        self.quiz_topic_button["command"] = quiz_click

        # Quiz Button for when the user is ready to stop entering values and is ready for a quiz of dictionary
        # values
        self.quiz_button = tk.Button(master, text="Quiz Me!", command=topic_for_quiz)
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

        # Button to show next entry during the quiz; HERE FOR SCOPE ISSUE
        self.next_entry_button = tk.Button(text="Next", command=next_entry)

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
            self.next_entry_button.grid_forget()

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


'''
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

            self.review_button = tk.Button(text="Review Words", command="")
            self.review_button.grid(column=1, row=1)
            self.quiz_button.grid(column=1, row=2)

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

        # def pass_in_dictionary(this_dict):
'''

if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
