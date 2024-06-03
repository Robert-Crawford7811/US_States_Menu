'''Menu system that prints information about the United States'''
import matplotlib.pyplot as plt

#Data Structure to hold state information
State_Data = [
    #Defines State by State's Name, Capital City Name, Population, and State's Flower
    {'State:': 'Alabama', 'Capital':'Montgomery','Population': 193948,'Flower':'Camellia',},
    {'State:':'Arkansas','Capital':'Little Rock','Population':203106,'Flower':'Apple Blossom'},
    {'State:':'California','Capital':'Sacramento','Population':530334,'Flower':'California Poppy'},
    {'State:':'Colorado','Capital':'Denver',
     'Population':708648,'Flower':'Rocky Mountain Columbine'},
    {'State:':'Connecticut','Capital':'Hartford','Population':120734,'Flower':'Mountain Laurel'},
    {'State:': 'Delaware', 'Capital': 'Dover', 'Population': 37811, 'Flower': 'Peach Blossom'},
    {'State:':'Florida','Capital':'Tallahasse','Population':205536,'Flower':'Orange Blossom'},
    {'State:':'Georgia','Capital':'Atlanta','Population': 498386, 'Flower': 'Atlanta'},
    {'State:': 'Hawaii', 'Capital': 'Honolulu', 'Population': 349913, 'Flower': 'Hibiscus'},
    {'State:': 'Idaho', 'Capital': 'Boise', 'Population': 237250, 'Flower': 'Syringa'},
    {'State:': 'Illinois', 'Capital': 'Springfield', 'Population': 112282, 'Flower': 'Violet'},
    {'State:': 'Indiana', 'Capital': 'Indianapolis', 'Population': 874089, 'Flower': 'Peony'},
    {'State:': 'Iowa', 'Capital': 'Des Moines', 'Population': 208254, 'Flower': 'Wild Rose'},
    {'State:': 'Kansas', 'Capital': 'Topeka', 'Population': 124479, 'Flower': 'Sunflower'},
    {"State:": 'Kentucky', 'Capital': 'Frankfort', 'Population': 28172, 'Flower': 'Goldenrod'},
    {"State:": 'Louisiana', 'Capital': 'Baton Rouge', 'Population': 216641, 'Flower': 'Magnolia'},
    {'State:': 'Maine', 'Capital': 'Augusta', 'Population': 19220, 'Flower': 'White Pine'},
    {'State:':'Maryland', 'Capital':'Annapolis', 'Population':40425, 'Flower':'Black-Eyed Susan'},
    {'State:': 'Massachusetts', 'Capital': 'Boston', 'Population': 629842, 'Flower': 'Mayflower'},
    {'State:':'Michigan', 'Capital':'Lansing', 'Population':112520, 'Flower':'Apple Blossom'},
    {'State:':'Minnesota','Capital':'St.Paul','Population':295522,
    'Flower':'Pink & White Ladys Slipper'},
    {'State:': 'Mississippi', 'Capital': 'Jackson', 'Population': 138998, 'Flower': 'Magnolia'},
    {'State:': 'Missouri', 'Capital': 'Jefferson City', 'Population': 42541, 'Flower': 'Hawthorn'},
    {'State:': 'Montana', 'Capital': 'Helena', 'Population': 35540, 'Flower': 'Bitterroot'},
    {'State:': 'Nebraska', 'Capital': 'Lincoln', 'Population': 293678, 'Flower': 'Goldenrod'},
    {'State:': 'Nevada', 'Capital': 'Carson City', 'Population': 57577, 'Flower': 'Sagebrush'},
    {'State:':'New Hampshire', 'Capital':'Concord', 'Population':44964, 'Flower':'Purple Lilac'},
    {'State:': 'New Jersey', 'Capital': 'Trenton', 'Population': 88744, 'Flower': 'Purple Violet'},
    {'State:': 'New Mexico', 'Capital': 'Santa Fe', 'Population': 90292, 'Flower': 'Yucca'},
    {'State:':'New York', 'Capital':'Albany', 'Population':102988, 'Flower':'Rose'},
    {'State:': 'North Carolina', 'Capital': 'Raleigh', 'Population': 488854, 'Flower': 'Dogwood'},
    {'State:':'North Dakota','Capital':'Bismarck','Population':75153,'Flower':'Wild Prairie Rose'},
    {'State:': 'Ohio', 'Capital': 'Columbus', 'Population': 909676, 'Flower': 'Scarlet Carnation'},
    {'State:':'Oklahoma', 'Capital':'Oklahoma City', 'Population':706576, 'Flower':'Oklahoma Rose'},
    {'State:': 'Oregon', 'Capital': 'Salem', 'Population': 179043, 'Flower': 'Oregon Grape'},
    {'State:':'Pennsylvania','Capital':'Harrisburg','Population':50274,'Flower':'Mountain Laurel'},
    {'State:': 'Rhode Island', 'Capital': 'Providence', 'Population': 188398, 'Flower': 'Violet'},
    {'State:':'South Carolina','Capital':'Columbia','Population':143210,'Flower':'YellowJessamine'},
    {'State:': 'Tennessee', 'Capital': 'Nashville', 'Population': 677519, 'Flower': 'Iris'},
    {'State:': 'Texas', 'Capital': 'Austin', 'Population': 983126, 'Flower': 'Bluebonnet'},
    {'State:':"Utah", "Capital":"Salt Lake City", "Population":208656, "Flower":"Sego Lily"},
    {'State:': 'Vermont', 'Capital': 'Montpelier', 'Population': 231782, 'Flower': 'Red Clover'},
    {'State:':'Virginia', 'Capital':'Richmond', 'Population':231782, 'Flower':'American Dogwood'},
    {'State:':'Washington','Capital':'Olympia','Population':55731,'Flower':'Western Rhododendron'},
    {'State:':'West Virginia', 'Capital':'Madison', 'Population':45616, 'Flower':'Rhododendron'},
    {'State:':'Wisconsin', 'Capital':'Madison', 'Population':275493, 'Flower':'Wood Violet'},
    {'State:':'Wyoming', 'Capital':'Cheyenne', 'Population':64000, 'Flower':'Indian Paintbrush'},
]
def state_display():
    '''Function that displays the information in the data structure in alphabetical order'''
    for x in State_Data:
        #Formating the data in the dictionary to be readable
        print(f"State:{x['State:']} ,Capital:{x['Capital']},"
              f"Population:{x['Population']},Flower:{x['Flower']}")

def most_populated_states():
    '''Function that creates and prints bar graphs of the top 5 most populated states'''
    #Defines the organization and how many states should be displayed
    pop_states = sorted(State_Data, key=lambda x: x['Population'], reverse=True)[:5]
    #Defines state and population numbers for comparison
    states = [x['State:'] for x in pop_states]
    populations = [x['Population'] for x in pop_states]
    # Defines the labels of the bar graph
    plt.bar(states, populations)
    plt.xlabel('State')
    plt.ylabel('Population')
    plt.title("Most populated states of the U.S.")
    plt.show()

def state_search():
    """Allows the user to look up information about a specific state"""
    #Prompt the user for the state that they want information about
    state_choice = input("Enter the state's name: ")
    #Searches and displays the information on the specified state
    for x in State_Data:
        if x['State:'].lower() == state_choice.lower():
            #Prints the information about the specified state
            print(f"State: {x['State:']}")
            print(f"Capital: {x['Capital']}")
            print(f"Population: {x['Population']}")
            print(f"Flower: {x['Flower']}")
            print(f"Image: {x['Image']}")
            return

    #Prints a statement if inputted state can't be found
    print(f"State'{state_choice}' not found.")

def update_population():
    """Allows the user to update the population of a specified state"""
    #Prompt the user for the state they would like to update of
    state_choice = input("Enter the state's name: ")
    while True:
        try:
            new_pop = int(input("Enter the state's new population number: "))
            break
        except ValueError:
            print("Enter a number please")
    # Update State Population
    for x in State_Data:
        if x['State:'].lower() == state_choice.lower():
            x['Population'] = new_pop
            print(f"Population of {state_choice} updated to {new_pop}.")
            return
    print(f"State '{state_choice}' not found.")

#Welcomes user to the program
print("Welcome to the US state Statistics System! Please make a selection!")
#Presents the options to the user.
print("1. Display U.S. States")
print("2. State Search")
print("3. Most populated states")
print("4. Update State's population")
print("5. Exit the program")

# Menu for navigation of the application
MENU = 0
# While user has not ended the program they will be prompted to make a decision
while MENU != 5:
    #Requests a decision to be made by the user
    MENU = int(input("Enter a selection: "))
    if MENU == 1:
        print("The states are....")
        #Call function to display states in alphabetical order
        state_display()
    elif MENU == 2:
        print("What state you want")
        #Call function that allows user to find a state
        state_search()
    elif MENU == 3:
        print("The most populated states are...")
        #Call function that displays graphs of states
        most_populated_states()
    elif MENU == 4:
        print("Enter in states new population...")
        #Call function that updates state with new information
        update_population()
    elif MENU == 5:
        print("Thank you for using the program")
        #Ends the program if user decides to end the program
        break
    else:
        # Prompts the user to attempt to make a correct selection
        print("Please Try Again.")
