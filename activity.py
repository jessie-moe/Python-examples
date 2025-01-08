## This script takes two arguments from the command line and prints them out, Two arguments are required to run this script.
import sys

print("*--------------------")
print("|", "First name: ", sys.argv[1])  ## This line takes the first argument passed to the script
print("|", "Second name: ", sys.argv[2]) ## This line takes the second argument passed to the script
print("*--------------------")
