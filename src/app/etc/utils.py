'''
    Utils: All the extra odds & ends we need to make things run
'''
def safe_load_int(raw_value, logger):
    '''Casts a string as an integer, safely. For use with .env vars.'''
    try:
        value = int(raw_value)
        return value
    except ValueError:
        logger.error("Invalid value found in .env: expected an int, found %s", raw_value)
        return 0