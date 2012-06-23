import re
import time

class Validator:
    """Validator Class

    Offers some basic validation for date, email

    """
    
    def __init__(self):
        # both regular expressions from
        # http://www.regular-expressions.info/email.html
        self.regex_email = re.compile(
            r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"
            r'"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09'
            r'\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]'
            r'(?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)'
            r'{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:['
            r'\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])', re.IGNORECASE)

        self.regex_strict = re.compile(
            r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]"
            r"*[a-z0-9])?\.)+(?:[A-Z]{2}|com|org|net|edu|gov|mil|biz|info|mobi|name|aero|asia|jobs|museum)\b", re.IGNORECASE)
        

    def validate_date(self, date, pattern):
        try:
            time.strptime(date, pattern)
        except ValueError:
            return False
        
        return True
    
    def validate_email(self, email, strict):
        """validates

        Optional plotz says to frobnicate the bizbaz first.
        
        """

        if strict:
            self.regex_email = self.regex_strict
        
        if self.regex_email.match(email):
            return True
        else:
            return False
