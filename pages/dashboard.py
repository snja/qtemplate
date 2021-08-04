from .base import *


class PageDashboard(PageBase):

    def __init__(self, parent):
        PageBase.__init__(self, parent)
        self.setup("Dashboard", False)
