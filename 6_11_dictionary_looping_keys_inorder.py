fav_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
if 'erin' not in fav_language.keys():
    print("Erin, please take our poll")
    
fav_language = {
    'jen' : 'python',
    'sarah' :'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in sorted(fav_language.keys()):
    print(name.title() + ", thank you for taking the poll.")