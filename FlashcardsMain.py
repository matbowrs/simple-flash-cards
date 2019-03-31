import tkinter as tk
from tkinter import *
from random import randint


# For database
import sqlite3
from sqlite3 import Error

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


def delete_category_entry():
    c.execute("DELETE FROM cards WHERE category = 'state capitals' OR category = 'french words' "
              "OR category = 'Capitals'")


def select_all_cards(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM cards")

    rows = cur.fetchall()

    ''' for row in rows:
        print(row)
    '''


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

    ''' for row in rows:
        print(row) 
    '''


def main():
    database = "./flashcard_database.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        select_card_by_category(conn, 'default')

        select_all_cards(conn)

    delete_category_entry()


main()

''' <----- END DATABASE -----> '''

''' <----- GUI And Logic ----->'''

# TODO #1. Have edit function?
# TODO #2. Remove all "print()" in final build

# ----- GUI -----
window = tk.Tk()

# Title of the application
window.title("Flash Cards")

# Window dimensions
window.geometry("700x500")

# <----- BEGIN GLOBAL VARIABLES ----->

# Label for deck entry
label_for_deck_topic = tk.Label(text="Create a name for your deck:")

# Entry field for deck topic
entry_for_deck_topic = tk.Entry()

# Button for creating a new topic for the deck
create_deck_topic_button = tk.Button(text="Create!", command="")

# Append button, used here for scope. Used with def append_to_dictionary()
append_button = tk.Button(text="Add to existing set")

# Goes with the button_click() below, declared here for global scope
show_dictionary_as_user_updates = tk.Label(text="")

# Entry for quiz topic
quiz_topic_entry = tk.Entry()
# Button for quiz topic
quiz_topic_button = tk.Button(text="Submit", command="")

# ListBox for showing all available categories the user can select from the database
lb = Listbox()
lb_as_user_updates = Listbox()

# Show which category the quiz is on ?? Delete ??
category_quiz_label = tk.Label(text="Category Name Here")

# Global scope for edit function below
edit_label = tk.Label(text="Enter new values below")
edit_entry_1 = tk.Entry()
edit_entry_2 = tk.Entry()

# Learn button
learn_button = tk.Button(text="Learn Topic", command="")

# Declare command, used in quiz_click()
done_button = tk.Button(text="", command="")

# <----- END GLOBAL VARIABLES -----

# <-- BEGIN DICTIONARY DECLARATIONS -->

# Declare main dictionary
main_dictionary = {}

# If user gets definition wrong, pair is sent here
bad_dictionary = {}

# If user gets definition correct, pair is sent here
good_dictionary = {}

good_dictionary_label = tk.Label(text="")
bad_dictionary_label = tk.Label(text="")

title_2 = tk.Label(text="What you got wrong: ")

# <-- END DICTIONARY DECLARATIONS -->

# <--- START LABELS --->
title = tk.Label(text="Enter the first word/definition, followed by the second.")
title.grid(column=6, row=0, padx=250)

# Label for showing whether the answer was correct or not
answer_response = tk.Label(text="")
answer_response.grid(column=6, row=6, padx=250)
# <--- END LABELS --->

# <-- BEGIN ENTRY FIELDS -->
text_entry_1 = tk.Entry(text="")
text_entry_1.grid(column=6, row=7, padx=250)

text_entry_2 = tk.Entry(text="")
text_entry_2.grid(column=6, row=8, padx=250)
# <-- END ENTRY FIELDS -->

# <----- BEGIN MAIN FUNCTIONS ----->
create_new_deck_button = tk.Button(text="Create New Deck", command="")


def create_topic_for_deck():
    create_new_deck_button.grid_forget()
    learn_button.grid_forget()
    quiz_button.grid_forget()
    text_entry_1.delete(0, END) # ?
    label_for_deck_topic.grid(column=6, row=0, padx=250, pady=(125, 5))
    entry_for_deck_topic.grid(column=6, row=1, padx=250)
    create_deck_topic_button.grid(column=6, row=2, padx=250)

    create_deck_topic_button["command"] = button_clicked_for_main_page


# As method says; used with the category and sending data to database
def get_card_deck_name():
    name = str(entry_for_deck_topic.get())
    return name


# Prompts user to enter information
def button_clicked_for_main_page():
    title.grid(column=6, row=0, padx=150, pady=(125, 5))
    text_entry_1.grid(column=6, row=4, padx=175)
    text_entry_2.grid(column=6, row=5, padx=175)
    submit_button.grid(column=6, row=6, padx=175)
    quiz_button.grid(column=6, row=7, padx=175)
    edit_button.grid(column=7, row=6, padx=175)

    learn_button.grid_forget()
    create_new_deck_button.grid_forget()
    label_for_deck_topic.grid_forget()
    entry_for_deck_topic.grid_forget()
    create_deck_topic_button.grid_forget()

    # On click, get the card deck topic name
    get_card_deck_name()


# "Home page"
def main_page():
    append_button.grid_forget()
    submit_button.grid_forget()
    # quiz_button.grid_forget()
    text_entry_1.grid_forget()
    text_entry_2.grid_forget()
    title.grid_forget()
    edit_button.grid_forget()
    done_button.grid_forget()
    next_entry_button.grid_forget()
    bad_dictionary_label.grid_forget()
    good_dictionary_label.grid_forget()
    title_2.grid_forget()
    create_new_deck_button.grid(column=6, row=4, padx=250, pady=(125, 10))
    learn_button.grid(column=6, row=5, padx=250)

    # on main_button click, run create_pair_function
    create_new_deck_button["command"] = create_topic_for_deck


# Function for setting text
def set_text(text):
    text_entry_1.delete(0, END)
    text_entry_1.insert(0, text)
    return


def set_text_2(text):
    text_entry_2.delete(0, END)
    text_entry_2.insert(0, text)
    return


# Allows edits to be performed on the second definition only; requires the first definition (the key) to work!
def edit_function():
    # Bind all edit objects to grid
    edit_label.grid(column=4, row=3)
    edit_entry_1.grid(column=4, row=4)
    edit_entry_2.grid(column=4, row=5)

    # Change edit_button text to Submit New Entry
    edit_button["text"] = "Submit New Entry"

    # Vars to store input from user in the Edit section
    new_edit_var = str(edit_entry_1.get())
    new_edit_var_2 = str(edit_entry_2.get())

    # Replace the values
    main_dictionary[new_edit_var] = new_edit_var_2

    # Update printed dictionary in UI
    # Show the dictionary as the user enters pairs
    store_dict_values = []
    for key in main_dictionary.items():
        store_dict_values.append(key)

    show_dictionary_as_user_updates["text"] = store_dict_values
    show_dictionary_as_user_updates.grid(column=7, row=3)

    print(main_dictionary)


# Edit button
edit_button = tk.Button(text="Edit", command=edit_function)
edit_button.grid(column=7, row=6)


# When user clicks button, get text from text_entry_1 & text_entry_2 and put into dictionary
# Also displays what the user is typing
def create_pair_function():
    append_button.grid_forget()

    def_1 = str(text_entry_1.get())
    def_2 = str(text_entry_2.get())
    main_dictionary[def_1] = def_2

    text_entry_1.delete(0, END)
    text_entry_2.delete(0, END)

    # Solves problem if the user goes to quiz right away and doesn't need to edit. Why? I don't know but it
    # works so don't touch it :)
    main_dictionary[""] = ""

    # Show the dictionary as the user enters pairs
    store_dict_values = []

    # Remove any blank pairs
    if '' in main_dictionary:
        del main_dictionary['']

    # Append dictionary pairs to list
    for key in main_dictionary.items():
        store_dict_values.append(key)

    lb_as_user_updates.grid(column=6, row=9)

    # Use list to show items in ListBox as user enters information
    lb_as_user_updates.delete(0, END)

    for i in store_dict_values:
        lb_as_user_updates.insert(END, i)

    # Send to database as user updates store_dit_values
    send_to_database(main_dictionary)

    print(main_dictionary)


# Submit button
submit_button = tk.Button(text="Create Pair", command=create_pair_function)
submit_button.grid(column=6, row=6, padx=250)


def learn_section(a_dictionary):
    # Learn section, kept here for scope reasons
    list_of_keys = []

    # Stores the keys
    my_keys = []

    # Stores the values
    my_values = []

    for x, y in a_dictionary.items():
        my_keys.append(x)
        my_values.append(y)

    list_of_keys.append(text_entry_1.get())

    # Used for selection when choosing a value for quizzing the user
    rand_num = randint(0, len(a_dictionary) - 1)

    # If the last entry and the new entry-to-be are the same, make the new entry-to-be different
    while list_of_keys[len(list_of_keys) - 1] == my_keys[rand_num]:
        rand_num = randint(0, len(a_dictionary) - 1)

    # Set the text using a random number, the key and the value
    set_text(my_keys[rand_num])
    set_text_2(my_values[rand_num])
    print(my_keys[rand_num])


next_entry_button = tk.Button(text="Next", command='')


def learn_click():
    # Change Title header
    title["text"] = "Let's learn!"

    # Hide Edit button and input
    edit_button.grid_forget()
    edit_button.grid_forget()
    edit_label.grid_forget()
    edit_entry_1.grid_forget()
    edit_entry_2.grid_forget()
    append_button.grid_forget()
    quiz_topic_button.grid_forget()
    quiz_topic_entry.grid_forget()
    lb.grid_forget()
    learn_button.grid_forget()
    show_dictionary_as_user_updates.grid_forget()
    submit_button.grid_forget()

    text_entry_1.grid(column=6, row=4, padx=250, pady=50)
    text_entry_2.grid(column=6, row=5, padx=250)

    # Bind next_entry_button
    next_entry_button.grid(column=6, row=5, padx=(300, 0))
    next_entry_button['command'] = lambda: learn_section(retrieve_category_pairs_from_database())

    # Remove the quiz button from the UI
    quiz_button.grid_forget()

    # Done button takes user back to main_page()
    done_button["text"] = "Done"
    done_button["command"] = main_page
    done_button.grid(column=6, row=8)

    # Shows first pair of words when learn section is started
    learn_section(retrieve_category_pairs_from_database())


def learn_get_pairs():
    entry_for_deck_topic.grid_forget()
    title["text"] = "Let's learn"


def learn_function():
    create_new_deck_button.grid_forget()
    text_entry_1.grid(column=6, row=4, padx=250, pady=50)
    text_entry_2.grid(column=6, row=5, padx=250)
    submit_button.grid(column=6, row=6, padx=250)
    # next_entry_button.grid(column=6, row=7, padx=250)
    topic_for_quiz()

    submit_button["command"] = create_pair_function
    # quiz_topic_button is the button at the screen where the user chooses a topic to quiz/study over.
    # This changes the command of the button to def learn_function()
    quiz_topic_button['command'] = learn_click


learn_button['command'] = learn_function


def data_into_dictionary(x):
    # Where x is a list
    updated_dictionary = dict(t for t in zip(x[::2], x[1::2]))
    return updated_dictionary


# Asks user for category, then retrieve the database
def topic_for_quiz():
    # Hide Edit button and input
    edit_button.grid_forget()
    edit_button.grid_forget()
    edit_label.grid_forget()
    edit_entry_1.grid_forget()
    edit_entry_2.grid_forget()
    done_button.grid_forget()
    next_entry_button.grid_forget()
    append_button.grid_forget()
    text_entry_1.grid_forget()
    text_entry_2.grid_forget()
    quiz_button.grid_forget()
    submit_button.grid_forget()
    show_dictionary_as_user_updates.grid_forget()
    learn_button.grid_forget()
    lb_as_user_updates.grid_forget()
    create_new_deck_button.grid_forget()
    create_deck_topic_button.grid_forget()

    quiz_topic_entry.grid(column=6, row=2, padx=250, pady=(5, 0))
    quiz_topic_button.grid(column=6, row=3, padx=250)

    title["text"] = "Enter the topic for the quiz (the name you called the decks)"
    title.grid(column=6, row=0, padx=150)

    retrieve_all_available_categories()


def retrieve_all_available_categories():
    c.execute("SELECT DISTINCT category FROM cards")
    all_categories = c.fetchall()

    lb.grid(column=6, row=1, padx=250)

    print(all_categories)

    # Delete everything in list box so that it can be added without repeats
    lb.delete(0, END)

    # Add values into the listbox
    for i in all_categories:
        lb.insert(END, i)


def retrieve_category_pairs_from_database():
    # Get which category the user typed in
    user_category = str(quiz_topic_entry.get())

    # Set user category equal to the label that is to be used during the quiz
    category_quiz_label["text"] = user_category

    c.execute("SELECT firstSide, secondSide FROM cards WHERE category = '" + user_category + "'")

    rows = c.fetchall()

    # Removes the tuple pairings from "rows" and puts everything into a list of strings
    result = []
    for t in rows:
        for x in t:
            result.append(x)

    print(result)
    # Put everything from result[] into a dictionary
    updated_dictionary = data_into_dictionary(result)

    print("pairs in category => %s" % updated_dictionary)

    return updated_dictionary


def send_to_database(a_dictionary):
    for i in a_dictionary:
        c.execute("INSERT INTO cards VALUES ('" + i + "','" + a_dictionary[
            i] + "','" + get_card_deck_name() + "','" + "image" + "')")
        conn.commit()


def quiz_section(a_dictionary):
    create_deck_topic_button.grid_forget()
    create_new_deck_button.grid_forget()
    text_entry_2.delete(0, END)

    # Quiz section, kept here for scope reasons
    list_of_keys = []
    my_list = []

    for x in a_dictionary:
        my_list.append(x)

    list_of_keys.append(text_entry_1.get())

    # Used for selection when choosing a value for quizzing the user
    rand_num = randint(0, len(a_dictionary) - 1)

    # If the last entry and the new entry-to-be are the same, make the new entry-to-be different
    while list_of_keys[len(list_of_keys) - 1] == my_list[rand_num]:
        rand_num = randint(0, len(a_dictionary) - 1)

    submit_button["command"] = lambda: check_answer(a_dictionary)

    set_text(my_list[rand_num])
    print(my_list[rand_num])


# When the user is ready to quiz him/her, change the button text on ".submit_button" to "Check Answer"
def quiz_click():

    text_entry_2['text'] = ''
    # Change Title header
    title["text"] = "Quiz Time!"

    # Hide Edit button and input
    edit_button.grid_forget()
    edit_button.grid_forget()
    edit_label.grid_forget()
    edit_entry_1.grid_forget()
    edit_entry_2.grid_forget()
    append_button.grid_forget()
    quiz_topic_button.grid_forget()
    quiz_topic_entry.grid_forget()
    lb.grid_forget()
    learn_button.grid_forget()

    text_entry_1.grid(column=6, row=4, padx=250, pady=50)
    text_entry_2.grid(column=6, row=5, padx=250)
    submit_button.grid(column=6, row=7, padx=250)

    # Hides the dictionary entries
    show_dictionary_as_user_updates.grid_forget()

    submit_button["text"] = "Check Answer"

    # Bind next_entry_button
    next_entry_button.grid(column=6, row=5, padx=(300, 0))

    # Remove the quiz button from the UI
    quiz_button.grid_forget()

    # Done button for when user is done taking the quiz; replaces .quiz_button
    done_button["text"] = "Done"
    done_button["command"] = show_final_dictionaries
    # done_button["command"] = main_page
    append_button["command"] = main_page
    done_button.grid(column=6, row=8)

    # Shows first pair of words when quiz is started. If removed, it will appear blank until 'next' button is clicked
    quiz_section(retrieve_category_pairs_from_database())


quiz_topic_button["command"] = quiz_click

# Quiz Button for when the user is ready to stop entering values and is ready for a quiz of dictionary
# values
quiz_button = tk.Button(text="Quiz Me!", command=topic_for_quiz)
quiz_button.grid(column=3, row=7)


# Check if pair is in the dictionary
def check_exist(dic, key, value):
    try:
        bool_exists = dic[key] == value
        return bool_exists
    except KeyError:
        return False


# Button to show next entry during the quiz; HERE FOR SCOPE ISSUE
# next_entry_button = tk.Button(text="Next", command=lambda: quiz_section(retrieve_category_pairs_from_database()))
next_entry_button['command'] = lambda: quiz_section(retrieve_category_pairs_from_database())


# Function to check answer
# Function that takes a dictionary as an argument
def check_answer(x):
    key_answer = str(text_entry_1.get())  # Get input from text_entry_1
    user_answer = str(text_entry_2.get())  # Get input from text_entry_2

    does_pair_exist_bool = check_exist(x, key_answer, user_answer)
    # Check if the user_answer and key_answer are paired together in the dictionary
    if does_pair_exist_bool:
        answer_response["text"] = "Correct!"
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
        answer_response["text"] = "Wrong!"
        for i in x:
            if i == key_answer:
                # Matches the correct words together and stores it in the bad_dictionary{}
                bad_dictionary[x[i]] = key_answer
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
    append_button.grid(column=3, row=8)


# Home page is down here. Yeah, I know...
main_page()


# When the user is fully done with the program and wants to show what they got correct
def show_final_dictionaries():
    # Hide these buttons
    quiz_button.grid_forget()
    submit_button.grid_forget()
    text_entry_1.grid_forget()
    text_entry_2.grid_forget()
    answer_response.grid_forget()
    edit_button.grid_forget()
    next_entry_button.grid_forget()
    learn_button.grid_forget()

    good_pair_list = []
    bad_pair_list = []

    title["text"] = "What you got correct: "
    title.grid(column=3, row=1, padx=275, pady=(150, 5))
    title_2.grid(column=3, row=3, pady=(20, 5))

    # Store everything in the good dictionary into the good list
    for key in good_dictionary.items():
        good_pair_list.append(key)

    # Store everything in the bad dictionary into the bad list
    for key in bad_dictionary.items():
        bad_pair_list.append(key)

    # Show the good pairs in the UI
    good_dictionary_label["text"] = good_pair_list
    good_dictionary_label.grid(column=3, row=2, padx=275)

    # Show the bad pairs in the UI
    bad_dictionary_label["text"] = bad_pair_list
    bad_dictionary_label.grid(column=3, row=4, padx=275)

    done_button.grid(column=3, row=5, padx=275, pady=(20, 5))
    done_button['command'] = main_page

    # Show append button at the end
    append_to_dictionary()

# <----- END MAIN FUNCTIONS ----->


if __name__ == "__main__":
    window.mainloop()
