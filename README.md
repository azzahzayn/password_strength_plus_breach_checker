# password_strength_plus_breach_checker
Python program to check the input password strength and check if it has appeared in any known breaches

**Features**
-> Strength scoring (0-6) - 2 for length and 4 for characters
-> Uses HaveIBeenPwned (HBPI) API for breach detection
-> Uses k-anonymity - only first 5 characters of password hash checked hence privacy focused

**SAMPLE OUTPUT**
input pw: hello123
strength: medium pw
1 . password should contain atleast one uppercase character
2 . password should contain atleast one special character
no of times breach has happened -> 1430471
