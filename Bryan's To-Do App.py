import time
import streamlit as st
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

st.set_page_config(page_title="To-Do App")
FILEPATH = "todos.txt"

def get_save(filepath=FILEPATH): # everything after the = sign is the default argument/parameter.
    """Loads your To-Do Items from the specified Save.txt file.
    Reads the text file and returns the list of to-do items."""
    with open(filepath, "r") as savefile_local:
        todos_local = savefile_local.readlines()
    return todos_local

def write_save(todos_arg, filepath=FILEPATH): # Non-default parameters must always precede default parameters. IDK why.
    """Writes the current list saved in the variable todos to your specified Save.txt file.
    Thereby, when you run the program again, your To-Do Items will be saved."""
    with open(filepath,"w") as savefile_local:
        savefile_local.writelines(todos_arg)

def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

daymonth = time.strftime("%A, %B ")
date = ord(int(time.strftime("%d")))
dayofyear = ord(int(time.strftime("%j")))
time = time.strftime("%I:%M:%S %p")

datetimegreeting1 = f"Hello! The current date is {daymonth}{date}.\nThe time at which you opened this tab was {time}."
datetimegreeting2 = f"It is the {dayofyear} day of the year."

todos = get_save()

st.title("Bryan's To-Do App")
st.subheader("A clean, helpful scheduler")
st.markdown(":violet[Written in Python with Streamlit.]")

st.markdown(f":orange[{datetimegreeting1}]")
st.write(f":orange[{datetimegreeting2}]")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_save(todos)
        del st.session_state[todo]
        st.experimental_rerun()

if "temp" not in st.session_state:
    st.session_state["temp"]=""

def add_todo():
    new_todo = st.session_state["text"]
    todos.append(new_todo + "\n")
    write_save(todos)
    st.session_state["temp"] = st.session_state["text"]
    st.session_state["text"] = ""

input = st.text_input(label="Enter a To-Do Item below and then hit Enter:", placeholder="Walk the dog...", on_change=add_todo, key="text")

st.write("You can remove items from your To-Do List by clicking the checkbox next to them.")

# Just commenting so I can commit.