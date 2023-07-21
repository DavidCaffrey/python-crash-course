import time,sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        
        if indentIncreasing:
            # Increase the number of spaces
            indent = indent + 1
            if indent == 20:
                # change direction
                indentIncreasing = False
            else:
                # decrease number of spaces
                indent = indent - 1
                if indent == 0:
# change direction
                    indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()