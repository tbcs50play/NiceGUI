from datetime import datetime
from nicegui import ui

# Define a global variable
pie_count = int(0)
secondcount1 = 0

# Create refreshable counter function that shows the lil guy imqages
@ui.refreshable
def newcard(name: str):
    with ui.card():
        count, set_count = ui.state(0)
        color, set_color = ui.state('black')
        ui.label(f'{name}, {count} hrs old').classes(f'text-{color}')
        ui.button(f'{name} Add 1', on_click=lambda: set_count(count + 1))
        # Create the lil guys
        with ui.avatar(size=f'{count+100}px', color=None):
            #ui.image('https://robohash.org/N7E.png')
            if(count<10):
                ui.image('https://cdn.leonardo.ai/users/494bb5c0-70e6-424a-bbac-6e723b241f08/generations/99d26d74-2ec4-4cfb-b10d-61e289951f3f/Leonardo_Diffusion_XL_a_cute_small_raccoon_0.jpg?w=512')
            elif(count>=10 and count<20):
                ui.image('https://cdn.leonardo.ai/users/494bb5c0-70e6-424a-bbac-6e723b241f08/generations/44a878a9-99af-4724-956d-74951d9f0eb5/Leonardo_Diffusion_XL_a_cute_small_raccoon_0.jpg?w=512')
            else:
                ui.image('https://cdn.leonardo.ai/users/494bb5c0-70e6-424a-bbac-6e723b241f08/generations/16cf1a4c-3c63-441a-9239-09fa01cea32b/Leonardo_Diffusion_XL_a_cute_largesized_raccoon_0.jpg')

        # create a timer element with an interval of 1 second
        timer = ui.timer(1.0, lambda: update_count())
        ui.switch('On').bind_value_to(timer, 'active')

        # define a callback function that increments the time count by 1 and updates the label
        def update_count():
            global secondcount1
            secondcount1 += 1
            secondcountlabel.set_text(f'Count: {secondcount1}')
        
        # show the timer count
        secondcountlabel = ui.label(f'Count: {secondcount1}')

        # testing define a callback function that resets the time count and the label
        #countyz, reset_count = ui.state(0)
        #def reset_count():
        #    secondcountlabel.set_text(f'Count: {secondcount1}')
         # Testing combo button (it works but adds to both A and B)
        #ui.button(f'{name} Reset', on_click=lambda: secoundcount1=0)
        
        # Testing combo button (it works but adds to both A and B)
        #ui.button(f'{name} Combine', on_click=lambda: set_count(count + secondcount1))


# Call counter function
with ui.row():
    newcard('Alan')
    newcard('Bandit')
    newcard('Cubby')

ui.run()

"""
#ui.run(on_air='d7MHhwsKKvICfTRug')
"""