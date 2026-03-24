"""
Step 1: Build the interface skeleton in view.py
Start by focusing only on the graphical aspect, temporarily ignoring what happens when you
click the buttons.
In the add_content(self) method of the View class, you will need to implement the three requested rows (Row):
- Row 1: An ft.Dropdown for language selection ("italiano", "inglese", "spagnolo").
- Row 2: Create a row containing:
    - An ft.Dropdown for the search modality ("Default", "Linear", "Dichotomic").
    - An ft.TextField where the user will type the sentence to check.
    - An ft.ElevatedButton (e.g., "Spell Check").
- Row 3: Create and add a ft.ListView component to the page, which will act as a "console" for the results.
    Pay attention to the syntax suggested in the assignment to initialize it.

Remember to save the references to these inputs as class attributes
(e.g., self.__dd_language, self.__txt_sentence) in the __init__ method, so you can
read them later.
"""

import flet as ft


class View(object):
    def __init__(self, page: ft.Page):

        # Page setup
        self.page = page
        self.page.title = "TdP 2026 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # Controller
        self.__controller = None

        # UI elements
        self.__title = None
        self.__theme_switch = None

        # Row 1 elements
        self.__dd_language = None
        self.__lv_out = None

        # Row 2 elements
        self.__dd_modality = None
        self.__txt_sentence = None
        self.__btn_check = None

    def add_content(self):
        """
        Function that creates and adds the visual elements to the page. It also updates
        the page accordingly.
        """

        # Title + theme switch
        self.__title = ft.Text("TdP 2026 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Tema Chiaro", on_change=self.theme_changed)

        self.page.controls.append(
            ft.Row(spacing=30,
                   controls=[self.__theme_switch, self.__title],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Row 1 element - Language selection
        self.__dd_language = ft.Dropdown(
            label="Seleziona Lingua",
            options=[
                ft.dropdown.Option("Italiano"),
                ft.dropdown.Option("Inglese"),
                ft.dropdown.Option("Spagnolo"),
            ],
            on_change=self.language_changed,
            width=200
        )

        # Row 2 elements - Modality, sentence input, and spell check button
        self.__dd_modality = ft.Dropdown(
            label="Modalità di Ricerca",
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic"),
            ],
            on_change=self.modality_changed,
            width=200
        )

        self.__txt_sentence = ft.TextField(
            label="Inserisci la tua frase qui",
            expand=True  # Allows the text field to take up the remaining horizontal space
        )

        self.__btn_check = ft.ElevatedButton(
            text="Spell Check",
            on_click=self.handle_spell_check
        )

        # Row 3 elements - Output ListView
        self.__lv_out = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)

        # Creating Rows
        row1 = ft.Row(controls=[self.__dd_language])
        row2 = ft.Row(controls=[self.__dd_modality, self.__txt_sentence, self.__btn_check])
        row3 = ft.Row(controls=[self.__lv_out])

        # Adding rows to the page
        self.page.add(row1, row2, row3)

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """
        Function that changes the color theme of the app, when the corresponding
        switch is triggered
        """
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Tema Chiaro" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Tema Scuro"
        )
        self.page.update()

    def language_changed(self, e):
        """
        Method called when a language is selected from the Dropdown
        """

        # Create the output message
        msg = f"Lingua selezionata correttamente: {self.__dd_language.value}"

        # Add a Text control to our ListView
        self.__lv_out.controls.append(ft.Text(value=msg, color="green"))

        # Always remember to update the page!
        self.page.update()

    def modality_changed(self, e):
        """
        Visual feedback when the search modality is changed
        """

        # Create the output message
        msg = f"Modalità di ricerca selezionata: {self.__dd_modality.value}"

        # Add a Text control to our ListView
        self.__lv_out.controls.append(ft.Text(value=msg, color="green"))

        self.page.update()

    def handle_spell_check(self, e):
        """
        Method called by the 'Spell Check' button
        """

        # Validation (Explicitly requested by the assignment)
        if self.__dd_language.value is None or self.__dd_modality.value is None or self.__txt_sentence.value == "":
            self.__lv_out.controls.append(
                ft.Text(value="Errore: seleziona lingua, modalità e inserisci una frase.", color="red")
            )
            self.page.update()
            return  # Stop execution if data is missing

        # Extract values inserted by the user
        sentence = self.__txt_sentence.value
        language = self.__dd_language.value
        modality = self.__dd_modality.value

        if self.__controller is not None:
            # MAPPA DI TRADUZIONE: converte l'input UI (Italiano) nel formato di model (inglese minuscolo)
            language_map = {"Italiano": "Italian", "Inglese": "English", "Spagnolo": "Spanish"}

            # Prende la lingua formattata dalla mappa
            language_formatted = language_map[language]

            wrong_rws_str, time_elapsed = self.__controller.handleSentence(sentence, language_formatted, modality)

            # Output formatting as requested by the assignment
            self.__lv_out.controls.extend([
                ft.Text(f"Frase inserita: {sentence}"),
                ft.Text(f"Parole errate: {wrong_rws_str}", color="red"),
                ft.Text(f"Tempo richiesto dalla ricerca: {time_elapsed}")
            ])

            # Empty the TextField (requested by the assignment)
            self.__txt_sentence.value = ""

            self.page.update()
