
"""
Search object - used with Watson APIs
To keep track of search and their results. for statistics purposes

"""
class Search(object):

    def __init__(self):
        self.searchId = ''
        self.query = ''
        self.result = ''
        self.options = ''
