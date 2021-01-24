import math

def calculateStats(numbers):
  
  #If list is empty return NaN
  if( len(numbers) == 0 ):
    average = math.nan
    maximum = math.nan
    minimum = math.nan
  else:
    #Find average, Maximum, Minimum
    average  = sum(numbers) / len(numbers)
    maximum  = max(numbers)
    minimum  = min(numbers)
  
  return { "avg":average, "max":maximum, "min":minimum }
