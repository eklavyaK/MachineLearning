try:
	result = 10 + '10'   # we can't add int to a string, so error will occur and except block will run
except:
	print("This block runs if there was an exception occurred in try block")
finally:
	print("No matter what, This block always runs")  # finally block always runs (both in case of error or not)



try:
	result = 10 + '10'
except TypeError:
	print("there was an typeError")  # since above statement gives typeError, this block will run
except OSError:
	print("there was an OSError")
except:
	print("there was some other error") # if the error doesn't correspond to oserror or typeerror then this block will run
finally:
	print("I will definitely run")


try:
	result = 10 + 10
except:
	print("Error")
else:
	print("No Error")   # this is executed if no error occurs
finally:
	print("Whatever")