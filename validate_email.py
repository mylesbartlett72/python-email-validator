import tld
import re


def check(addr):
    '''Takes an email address (addr) and returns a tuple containing, in order:
    If the email is valid (boolean)
    The top level domain of the email address' domain (str)
    The full domain of the email address (str)
    
    You can assign these to separate variables like this:
    isvalid, topleveldomain, domain = check("s+p.a_m@ham.eggs.example.co.uk")
    The example would set:
    isvalid = True
    topleveldomain = co.uk
    domain = ham.eggs.example.co.uk
    
    You can implement the regex used for checking validity yourself, it is:
    ^[a-z0-9\._\+]+[@]{1,251}[a-zA-Z0-9\._]+[\.]+\w+$
    
    Bear in mind that this does not check if the TLD is real.  Use the tld library (not mine) for that.'''
    isvalid = True # assumed
    regex = '^[a-z0-9\._\+]+[@]{1,251}[a-zA-Z0-9\._]+[\.]+\w+$' # complex regex that involved a lot of web searches and frustration to make

    domain = email[email.index('@') + 1 : ] # Thanks, geeksforgeeks!
    try:
        topleveldomain = tld.get_tld(domain, fix_protocol=True)
    except tld.exceptions.TldDomainNotFound:
        isvalid = False
        topleveldomain = None

    if isvalid: # no need to do anything if invalid TLD
        if re.search(regex, email):
            pass # No need to do anything as already assumed valid email
        else:
            isvalid = False
    return (isvalid, topleveldomain, domain)


if __name__ == "__main__": # If run on own.
    email = input("Email\n>")
    isvalid, topleveldomain, domain = check(email)
    humanreadable_isvalid = str()
    if isvalid:
        humanreadable_isvalid = "Yes"
    elif not isvalid:
        humanreadable_isvalid = "No"
    else:
        humanreadable_isvalid = "We are not sure what happened.  Try not running the script on a quantum computer!"
    print("TLD:\n" + topleveldomain, "\nIs a valid email address:\n" + humanreadable_isvalid, "\nFull domain:\n" + domain)
