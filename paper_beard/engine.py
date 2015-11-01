"""

"""
from pyGoogleSearch import Google


def google_scholar(title, author=None):
    """



    :type author: str
    :type title: str
    :param title:
    :param author:
    :return:
    """
    def get_key(year):
        key = author if author else title[:20]
        key += str(year)
        return ''.join(e for e in key if e.isalnum())

    search_string = title
    if author is not None:
        search_string += " " + author
    raw_scholar_data = Google(search_string, pages=1).search_scholar()

    if len(raw_scholar_data["results"]) == 0:
        return Nothing
    scholar_r = raw_scholar_data["results"][0]
    result = Result()
    result.author = author
    result.title = scholar_r['title']
    result.year = scholar_r['year']
    result.citations = scholar_r['citations']
    result.link = scholar_r['link']
    result.excerpt = scholar_r['excerpt']
    result.key = get_key(result.year)
    return Just(result)


class Maybe():
    def then(self, action):
        if self.__class__ == _MaybeNothing:
            return Nothing
        elif self.__class__ == Just:
            return action(self.value)


class _MaybeNothing(Maybe):
    def __repr__(self):
        return "Nothing"

Nothing = _MaybeNothing()


class Just(Maybe):
    def __init__(self, v):
        self.value = v

    def __repr__(self):
        return "Just(%r)" % self.value


class Result(object):
    def __init__(self):
        self.author = ''
        self.title = ''
        self.type = 'article'
        self.journal = ''
        self.year = ''
        self.key = None
        self.citations = 0
        self.link = ''
        self.excerpt = ''

    def get(self, field, default=''):
        return getattr(self, field, default)