import streamlit as st
from modules import functions

todo_list = functions.read_to_do_list()


def add_todo():
    todo_local = st.session_state["input_todo"]
    todo_list.append(todo_local)
    functions.write_to_do_list(todo_list)


st.title("My To Do Program")
st.header("The current Todos: ")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todo_list.pop(todo_list.index(todo))
        functions.write_to_do_list(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Input Todo", placeholder="Write a new todo!", on_change=add_todo, key="input_todo")
# st.session_state




