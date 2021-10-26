# python-email-validator
Simple python email validator

Uses the included python *re* library and the third-party library [*tld*](https://pypi.org/project/tld/)

We have made every attempt to find a compatible license, please alert me in the bug tracker if there is a conflict!

## Usage

1)Run 
```console
spam@eggs:~$ pip3 install tld
```
2)Clone the repository somewhere<br>
3)Copy/move the validate_email.py file into your project folder<br>
4)In your Python file
```python
import validate_email
```
5)To use, call
```python
isvalid, topleveldomain, domain = validate_email.check("email@tocheck.com") # Or whatever email you want.
```
This unpacks the tuple for you, or you can use the tuple on its own, if you wish.  The variables named here are the function responses in the order they appear in the tuple.

6)For only the validity status, use
```python
isvalid = validate_email.check("email@tocheck.com")[0] # Or whatever email you want.
```
