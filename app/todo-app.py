import streamlit as st
from streamlit_option_menu import option_menu


# ToDO Application with CRUD functionality.
# Stored/retrieved the data inside the mysql.
# that is located in other server.
# @ Author : Irsyaad Rijwan.

# Initialized Horizontal Menu with.
# options menu that have its unique icons.
# Options : Create, Read, Update, Delete, About.
# @ return option_menu object.
def horizontal():
  selected = option_menu(
      menu_title = None,
      # menu options,
      options = ["Create", "Read", "Update", "Delete", "About"],
      # menu icons
      icons = ["pencil-square","book","gear","trash","info-circle"],
      # change the default icon of the menu title
      menu_icon = "cast",
      default_index = 0, # index of the icon 0 for menu title
      orientation = "horizontal", # orientation of the menu
      # css styles for the menu.
       styles={
        "container": {"padding": "0!important"},
      }
    )
  return selected

#  A function that displays the menu functionality,
#   when the user clicks one of hte menu buttons.
def menu_func(selected):
  if selected == "Create":
    st.title(f"You have selected {selected}")
  if selected == "Read":
    st.title(f"You have selected {selected}")
  if selected == "Update":
    st.title(f"You have selected {selected}")
  if selected == "Delete":
    st.title(f"You have selected {selected}")
  if selected == "About":
    st.title(f"You have selected {selected}")


if __name__ == "__main__":
  menu_func(horizontal())
  