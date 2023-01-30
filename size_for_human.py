''' writing a new python file '''
print('\n\nFirst practice python program\n')

# define dictionary suffixes, keys are 1000 and 1024
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# define routines to be used by main()
def approximate_size(size, a_kilobyte_is_1024_bytes=True): 
                        # NB variable set in arg
    if size < 0: 
        raise ValueError('number must be non-negative')
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000 

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix) 
            
    ''' reached beyond the last entry in dictionary '''
    raise ValueError('number is larger than YB')

# Start main body of the program
if __name__ == '__main__': 
    ''' use machine size '''
    print(approximate_size(1000000000000, False))
    ''' print human size '''
    print(approximate_size(1000000000000))