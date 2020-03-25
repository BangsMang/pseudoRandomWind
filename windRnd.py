#---------------------------------------------------------------------------------
# Simple program for generating pseudo-random values for wind speed and wind direction.
# The program outputs the data in a CSV-file with incremented timestamps at 10Hz
#
#Written by Magnus Lindahl, 25/3 2020
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
#Global variables for better "randomness", and imprt random
#---------------------------------------------------------------------------------

import random
lastDir = 45
lastWind = 10
lastTime = 0.00

#---------------------------------------------------------------------------------
#Functions for generating pseudo-random values for wind speed, and wind direction.
#---------------------------------------------------------------------------------

def  windRnd():
     return random.uniform(lastWind-1, lastWind+1) #+- interval

def  dirRnd():
     return random.uniform(lastDir-5, lastDir+5) #+. interval



#---------------------------------------------------------------------------------
# Functions for fomrating the output as CSV
#---------------------------------------------------------------------------------

def timeCsv():
     global lastTime
     lastTime += 0.10
     newTimeCSV = (str("%.3f" % lastTime) + ";")                           # Limit number of decimals to 3, and convert int -> string
     return(newTimeCSV)

def windCsv():

     newWind = str("%.3f" % windRnd())
     newWindCSV = (newWind + ";")
     return(newWindCSV)

def dirCsv():

     newDir = (str("%.3f" % dirRnd()) + "\n")
     return (newDir)


     
#---------------------------------------------------------------------------------
#    MAIN
#---------------------------------------------------------------------------------

main = open("rndWindCSV.csv","w+")                                         # Create file and give R/W-privileges

main.write("INCREMENTED.time;RANDOM.windSpeed;RANDOM.direction\n")         # Write CSV-header

for i in range(1000):                                                      # Number of data-points

#    Print data

     main.write(timeCsv())
     main.write(windCsv())
     main.write(dirCsv())
     main.close                                                            # End