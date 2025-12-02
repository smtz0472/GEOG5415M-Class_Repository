# points.py
# A simple py file that contains a list of points and a function that reads
# the list and returns the points

# ****************** EDIT BELOW ******************
# Add your point as a new item in the list. 
# Create a new line for your point, and don't forget the square brackets and the comma
# Poinst should be in the following format:
# [ latitude, longitude, "description" ],

points_list = [
    [  53.808478, -1.5527924, "University of Leeds" ],
    [  53.840032, -1.6432286, "Nick's neighbourhood" ],
    [  53.98180, -1.51175, "A seat with a good veiw"], 
    [  54.99163, -1.60362, "Phenix: Newcastle's best pub"],

    # Add more points here

     [ 52.65026, -0.47385, "Albert Bridge" ],
     [ 52.50787, -0.40212, "Cara's Hill" ],
    [  53.814665, -1.6376061, "Fran's favourite bakery"],
    
    [  53.800622, -1.5483202, "The Leeds Art Gallery!" ],
    [  53.798874, -1.5408800, "Rayan's Favourite Japanese Restaurant" ],
    [  34.58223767715908, 135.79883198965894, "Kuni's favourite ramen restaurant in Japan"],
    [ 31.473338429173076, 74.46975891032893, "Lanzhou noodles-LCC" ],
    

    [  53.800350,-1.539687, " Chenxi's favourite Thai Restaurant"],
]

def get_points():
    """Return the list of points"""
    return points_list
