import flet as ft

import controller as c
import view as v


def main(page: ft.Page):
    """
    Main entry point for the Flet application.
    This function initializes the MVC architecture and starts the UI.
    """

    # 1. Initialize the View
    # We pass the 'page' object provided by Flet to the View,
    # so it knows where to draw the UI elements.
    view = v.View(page)

    # 2. Initialize the Controller
    # We pass the View to the Controller so the Controller can interact with it.
    # Note: Inside the SpellChecker's __init__, the Model (MultiDictionary)
    # is automatically created.
    controller = c.SpellChecker(view)

    # 3. Connect the View to the Controller
    # We pass the Controller instance back to the View. This allows the View
    # to delegate actions (like clicking the "Spell Check" button) to the Controller.
    view.setController(controller)

    # 4. Render the UI
    # Now that everything is wired up, we tell the View to build and display
    # its visual elements on the page.
    view.add_content()


# Start the Flet application and set the target function to 'main'
ft.app(target=main)