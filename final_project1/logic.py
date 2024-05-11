import csv
from PyQt6.QtWidgets import *
from gui import *
import random
from typing import Optional, List


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Initialize the application logic."""
        super().__init__()
        self.setupUi(self)
        self.candidates_button_group: QButtonGroup = QButtonGroup()
        self.candidates_button_group.addButton(self.edward_button)
        self.candidates_button_group.addButton(self.bianca_button)
        self.candidates_button_group.addButton(self.felicia_button)

        self.candidates_button_group.buttonClicked.connect(lambda: self.candidates())
        self.selected_button: [QAbstractButton] = None  # No button selected by default
        self.candidate: Optional[str] = None
        self.candidates_called: bool = False
        self.total_vote: int = 0
        self.edward_vote: int = 0
        self.felicia_vote: int = 0
        self.bianca_vote: int = 0

        self.firstname_input.setText(" ")
        self.lastname_input.setText(" ")
        self.state_input.setText(" ")
        self.address_input.setText(" ")
        self.zip_input.setText(" ")
        self.continue_button.setEnabled(False)
        self.stackedWidget.setCurrentIndex(0)
        self.citizen_input.setCurrentIndex(0)
        self.citizen_input.setCurrentText("")
        self.age_number.setValue(0)
        self.registered_input.setCurrentIndex(0)
        self.registered_input.setCurrentText("")
        self.firstname_input.setFocus()

        self.clear_button.clicked.connect(lambda: self.clear_app())
        self.submit_button.clicked.connect(lambda: self.submit_app())
        self.continue_button.clicked.connect(lambda: self.continue_to_ballot())
        self.submit_button2.clicked.connect(lambda: self.submit_ballot())
        self.restart_button.clicked.connect(lambda: self.restart())

    def submit_app(self) -> None:
        """Processes the submitted application once the user clicks the submit button."""
        try:
            self.first_name: str = self.firstname_input.text()
            self.last_name: str = self.lastname_input.text()
            self.age: int = int(self.age_number.value())
            self.state: str = self.state_input.text()
            self.address: str = self.address_input.text()
            self.zip: int = int(self.zip_input.text())
            self.citizen: str = self.citizen_input.currentText()
            self.registered: str = self.registered_input.currentText()

            # Input validation
            self.zip_checked: bool = len(str(self.zip)) > 0
            self.citizen_checked: bool = self.citizen == 'Yes'
            self.registered_checked: bool = self.registered == 'Yes'
            self.name_checked: bool = len(self.first_name.strip()) > 0 and len(self.last_name.strip()) > 0 \
                and self.first_name.strip().isalpha() and self.last_name.strip().isalpha()
            self.state_checked: bool = len(self.state.strip()) > 0 and self.state.strip().isalpha()
            self.address_checked: bool = len(self.address.strip()) > 0
            self.age_checked: bool = self.age >= 18

            # Determine application status
            if self.name_checked and self.state_checked and self.age_checked and \
                    self.address_checked and self.zip_checked and self.citizen_checked and self.registered_checked:
                self.random_id: int = random.randint(100000, 999999)
                self.output_label.setText(f'<font color="green">Thank you for applying. Your application has been '
                                          f'accepted. Your ID number is {self.random_id}. Please '
                                          f'click the continue button to access the ballot.</font>')
                self.submit_button.setEnabled(False)
                self.continue_button.setEnabled(True)
            else:
                self.output_label.setText(f'<font color ="red">Your application has been declined. '
                                          f'Make sure you are inputting correct and valid information. '
                                          f'You must be 18 or older, a U.S. citizen, and registered to vote.</font>')
        except ValueError:
            # Error Handling: Update output label with error message
            error_message = ('Please fill everything out correctly. Make sure the zip code '
                             'only contains digits.'
                             ' Make sure name and state inputs contain no digits. Address can only consist of letters '
                             'and digits. ')
            self.output_label.setText(f'<font color="red">{error_message}</font>')

    def clear_app(self) -> None:
        """Clears the application form inputs and resets UI state."""
        self.firstname_input.clear()
        self.lastname_input.clear()
        self.address_input.clear()
        self.state_input.clear()
        self.zip_input.clear()
        self.output_label.clear()
        self.firstname_input.setFocus()
        self.continue_button.setEnabled(False)
        self.submit_button.setEnabled(True)
        self.age_number.setValue(0)
        self.citizen_input.setCurrentIndex(0)
        self.registered_input.setCurrentIndex(0)

    def continue_to_ballot(self) -> None:
        """Switches the UI to the ballot page."""
        self.stackedWidget.setCurrentIndex(1)
        self.restart_button.setEnabled(False)

    # Second page methods below

    def candidates(self) -> None:
        """Callback function for when a candidate is selected."""
        self.candidates_called = True
        self.selected_button = self.candidates_button_group.checkedButton()

    def submit_ballot(self) -> None:
        """Processes the submitted ballot."""
        self.valid_entry = False
        self.restart_button.setEnabled(True)
        try:
            self.id_number: str = self.id_name.text().strip()
            self.id_number = int(self.id_number)  # Convert ID text to an integer

            if self.id_number != self.random_id or len(str(self.id_number)) < 6:
                self.output_label2.setText(
                    '<font color="red">Please make sure to enter your given ID number correctly.</font>')
            elif not self.candidates_called:  # If no candidate has been selected
                self.output_label2.setText(
                    '<font color="red">Please select a candidate before submitting your vote.</font>')
            else:
                if self.selected_button == self.edward_button:
                    self.candidate = 'Edward'
                    self.total_vote += 1
                    self.edward_vote += 1
                elif self.selected_button == self.bianca_button:
                    self.candidate = 'Bianca'
                    self.total_vote += 1
                    self.bianca_vote += 1
                elif self.selected_button == self.felicia_button:
                    self.candidate = 'Felicia'
                    self.total_vote += 1
                    self.felicia_vote += 1
                self.submit_button2.setEnabled(False)
                self.output_label2.setText('<font color="green">Thank you for voting.</font>')
                self.totalvotes_label.setText(
                    f'Edward Votes - {self.edward_vote} | Bianca Votes - {self.bianca_vote} | Felicia Votes - {self.felicia_vote} | Total Votes - {self.total_vote}')
                self.valid_entry = True

        except ValueError:
            self.output_label2.setText(
                '<font color="red">Please make sure to enter your given ID number correctly. Your given ID should be numeric and not contain letters.</font>')
        self.save_to_csv()

    def clear_ballot(self) -> None:
        """Clears the ballot form inputs and resets UI state."""
        self.id_name.clear()
        self.candidates_button_group.setExclusive(False)
        self.candidates_button_group.checkedButton().setChecked(False)
        self.candidates_button_group.setExclusive(True)
        self.output_label2.clear()
        self.submit_button2.setEnabled(True)

    def restart(self) -> None:
        """Restarts the application by resetting UI and form inputs."""
        self.stackedWidget.setCurrentIndex(0)
        self.clear_app()
        self.clear_ballot()

    def save_to_csv(self) -> None:
        """Saves the submitted ballot data to a CSV file."""
        if self.valid_entry:
            self.assigned_ids: List[int] = []
            if self.random_id in self.assigned_ids:
                self.output_label.setText('<font color="red">Error: Duplicate ID detected. Please try again.</font>')
                return

            self.assigned_ids.append(self.random_id)

            headers = ["First Name", "Last Name", "Age", "State", "Address", "ZIP", "Citizen", "Registered",
                       "Random ID"]
            data = [self.first_name, self.last_name, self.age, self.state, self.address, self.zip, self.citizen,
                    self.registered, self.random_id]

            with open('voters_data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                if csvfile.tell() == 0:
                    writer.writerow(headers)
                writer.writerow(data)