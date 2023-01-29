# Raise own exception

# raise Exception('This is the error message.')


# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')

#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)

# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))

# import traceback

# # Save error to file

# try:
#           raise Exception('This is the error message.')
# except:
#           errorFile = open('errorInfo.txt', 'w')
#           errorFile.write(traceback.format_exc())
#           errorFile.close()
#           print('The traceback info was written to errorInfo.txt.')

# # Assertions - check code works good

# ## Good code
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# ages
# [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
# assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

# ## Bad code
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# ages
# [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
# assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

# Logging

## Wrong code
import logging
logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')

## Right code

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')

# Logging are nice because show you where is the problem, you can add as many as you like. If you don't want to use them just change config -> logging.disable(logging.CRITICAL)

# There are logging types level for different purposes
# DEBUG

# logging.debug()

# The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
# ---------------------------------
# INFO

# logging.info()

# Used to record information on general events in your program or confirm that things are working at their point in the program.
# ---------------------------------
# WARNING

# logging.warning()

# Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
# ---------------------------------
# ERROR

# logging.error()

# Used to record an error that caused the program to fail to do something.
# ---------------------------------
# CRITICAL

# logging.critical()

# The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.

# Logging save to file

# logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

# # Samples

# logging.debug('Some debugging details.')
# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')

