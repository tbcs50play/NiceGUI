import streamlit as st
from nicegui import ui

#Welcome me to my app
ui.chat_message('Hey Travis, Sweet app!',
                name='Robot',
                avatar='https://robohash.org/ui')

#define function for declaring awesomeness and assigning button count
click_count=int(0)

def clicked():
    ui.notify('You are awesome')
    global click_count
    click_count +=1
    button.set_text(click_count)
    
#create the button
button = ui.button('Click me!', on_click=clicked).style('width: 200px')

ui.run()
