from dealroom_urlextract import extract


# Valid
print(extract('http://www.something.com/home.html?abc'))
print(extract('https://app.example.co.uk/something.html'))

# Raises exception
print(extract('https://app.example.invalid/something.html'))
