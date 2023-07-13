from qaguru.components.left_panel import LeftPanel
from qaguru.components.simple_registration_form import SimpleRegistrationForm


class Application:
    def __init__(self):
        self.left_panel: LeftPanel = LeftPanel()


app = Application()
