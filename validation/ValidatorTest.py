from Validator import Validator

def test_date():
    dates = (
        # valid
        '22.05.1988',
        '01.01.2000',
        '1.1.0001',
        '1.1.9999',
        '27.02.2000',
        '28.2.2000',
        '29.02.2000',   # 29.02. is a valid date in 2000
        
        # not valid
        '1.1.10000',    # biggest possible year is 9999
        '1.1.0',        # smallest possible year is 1
        '1.1.0000',
        '1.1.'
        '1',
        '30.02.2000',
        '31.02.2000',
        '31.04.2000',
        '29.02.2001'
        )

    validator = Validator()
    for date in dates:
        if validator.validate_date(date, "%d.%m.%Y"):
            validated = 'valid'
        else:
            validated = 'not valid'
        print('{0:32} {1:10}'.format(date, validated))


def test_email():
    addresses = (
        # valid
        'john@doe.com',   
        'cust/dep=shipping@example.com',    # /, = are valid characters
        '!def!xyz%abc@example.com',         # !, %
        'a+bcdef@ddd.com',                  # + is allowed
        '!#$%&*+-/=?^_`{}|~@example.org',
        'unusual@dept.example.com',
        'example@example.com',
        'president@whitehouse.gov',
        'me+valid@mydomain.example.net',
        '"Abc@def"@example.com',            # @ in " "
        '"bert\ ernie"@w00t.com',           # blank allowed, if in " " and
        '"\ \\\""@dot.org',
        '"()<[:@\\\"-/=?^_`{}|~.a"@ab.org',
        '""@example.org',
        'a@[10.10.10.10]',
        
        # theoretically valid, but not recognized
        'abc."defghi".xyz@example.com',     # dot-separated quoted string, not commonly used
        'b@[IPv6:2001:db8:1ff::a0b:dbd0]',  # IP address literal as IPv6
        'postbox@com',                      # top-level domains are valid hostnames
        
        # not valid
        'A@b@c@example.com',
        'a"b(c)d,e:f;g<h>i[j@example.com',
        'abc"defghi"xyz@example.com',
        ' not\ allowed@example.com',
        '.test123@dfg.com',
        'test123.@dfg.com',
        'test 123@dfg.com',
        'John..Doe@example.com',            # two consectutive dots
        '"bert ernie"@w00t.com',
        'Abc\@def@example.com',             # escaping @ only in " " allowed
        'lulz',
        'foo@bar',                          # bar is no top-level domain
        'foo@bar com',
        'foo@hello bar.com',
        'foo@[hello bar].com',
        'abcdefghijklmno@pqrstuvwxyz'
        )

    validator = Validator()
    for email in addresses:
        if validator.validate_email(email, False):
            validated = 'valid'
        else:
            validated = 'not valid'
        print('{0:32} {1:10}'.format(email, validated))


if __name__ == '__main__':
    print "Email addresses"
    print "==============="
    test_email()
    print "\nDates"
    print "==============="
    test_date()
