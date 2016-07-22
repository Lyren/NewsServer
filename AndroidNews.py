class AndroidNews(object):

    type = ''
    title = ''
    link = ''
    desc = ''
    issue_id = 0

    def __init__(self,issue_id,type):
        self.issue_id = issue_id
        self.type = type
