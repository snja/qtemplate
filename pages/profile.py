from .base import *


class PageProfile(PageBase):

    def __init__(self, parent):
        PageBase.__init__(self, parent)
        self.setup("Profile")