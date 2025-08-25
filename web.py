import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("my TaskTraker")
st.header("TaskTraker")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}_{todo.strip()}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()





st.text_input(label="",placeholder="Add new todo:",
              on_change=add_todo,key='new_todo')

print("hello my dear")