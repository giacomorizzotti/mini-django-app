import string, random
from datetime import datetime

def randomCode(n):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))

class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)  

