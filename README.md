# PasswordValidator-regex-

Password validation in Python
Let’s take a password as a combination of alphanumeric characters along with special characters, and check whether the password is valid or not with the help of few conditions.

Conditions for a valid password are:

Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be between 6 to 20 characters long.

compile() method of Regex module makes a Regex object, making it possible to execute regex functions onto the comp variable. Then we check if the pattern defined by comp is followed by the input string passwd. If so, the search method returns true, which would allow the password to be valid.