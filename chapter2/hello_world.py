message = "Example test message."
print(message)

message = "Same variable name, but different value because variable values change line by line as the code is interpretted down the page."
print(message)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!") 

message = f"Hello, {full_name.title()}!"
print(message)

favorite_language = 'Python '
print(favorite_language)

favorite_language.rstrip()
print(favorite_language.rstrip())

favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = '   python  '
print(favorite_language.strip())

nostarch_url = 'https://nostarch.com'
print(nostarch_url)

nostarch_url = nostarch_url.removeprefix('https://')

print(nostarch_url)

message = "One of Python'd strengths is its diverse community."

print(message)

# message = 'One of Python's strengths is its diverse community.'

# print(message)

