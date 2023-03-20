import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos_arg=todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # print(index, todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos_arg=todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a ToDo", placeholder="Add a new todo...", on_change=add_todo, key='new_todo')

st.session_state