fav_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
friends = ['phil','sarah']
for name in fav_language.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite programming language is"
               + fav_language[name].title() + "!")