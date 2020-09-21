#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Ardath Dixon (ardath.dixon@duke.edu)
# Date:   Sept 2020
#--------------------------------------------------------------

# Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

# Create a file object from the file
file_object = open(file_name,'r')

# Read contents of file into a list
line_list = file_object.readlines()

# Close the file
file_object.close()

# Create two empty dictionary objects
date_dict = {}
coord_dict = {}

# Iterate through all lines in the lineList
for lineString in line_list:
    if lineString[0] in ("#","u"): continue

    # Split the string into a list of data items
    lineData = lineString.split()
    # Only keep LC 3, 2, 1
    if lineData[4] != "3" and lineData[4] != "2" and lineData[4] != "1": continue

    # Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    # print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    # Assign values to dictionaries
    date_dict[record_id] = obs_date
    coord_dict[record_id] = (obs_lat,obs_lon )
