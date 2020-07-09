# CONSTRUCOT EXAMPLE - MOVIE INFO
class Movie():
    def __init__(self,title,actor,actress):
        self.title = title
        self.actor = actor
        self.actress = actress
    def info(self):
        print('**MOVIE CAST AND CREW** :',self.title,'-',self.actor,',',self.actress)

listOfMovies = []
while True:
    title = input('ENTER MOVIE NAME :')
    actor = input('ENTER ACTOR NAME :')
    actress = input('ENTER ACTRESS NAME :')
    m = Movie(title, actor, actress)  # Movie object, Constructor Executed
    listOfMovies.append(m)
    print('***MOVIE INFO ADDED SUCCESSFULLY**')
    option = input('DO YOU WANT TO ADD ONE MORE MOVIE ?[YES/NO] :')
    if option.lower() == 'no':
        break
print()
print('### MOVIES INFORMATION ###')
for movie in listOfMovies:
    movie.info()     # INSTANCE METHOD
    print()