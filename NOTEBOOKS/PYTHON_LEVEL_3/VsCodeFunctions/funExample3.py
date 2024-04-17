from datetime import datetime

print(f'__name__ :  {__name__}')

def greet_user():
    current_date = datetime.now()
    print('hey hi welcome to april python training')
    print(f'Today : {current_date}')

def bye():
    print("bye bye..., i will be executed when imported..")

if __name__ == '__main__': # will execute when we run directly
    greet_user()
else: # will be executed when imported in other module.
    bye()

# greet_user()
# bye()