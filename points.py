# points.py
# A simple py file that contains a list of points and a function that reads
# the list and returns the points

# ****************** EDIT BELOW ******************
# Add your point as a new item in the list. 
# Create a new line for your point, and don't forget the square brackets and the comma
# Poinst should be in the following format:
# [ latitude, longitude, "description" ]

points_list = [
    [  53.808478, -1.5527924, "University of Leeds" ],
    [  53.840032, -1.6432286, "Nick's neighbourhood" ],

    # Add more points here

    [ 53, -1.5, "Close to University of Leeds" ], 
    [ 53, -1.6, "Close to Nick's neighbourhood" ], 

]

def get_points():
    """Return the list of points"""
    return points_list
