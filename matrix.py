import random, shutil, sys, time

# Set up the constants:
MIN_STREAM_LENGTH = 6  # (!) Try changing this to 1 or 50.
MAX_STREAM_LENGTH = 14  # (!) Try changing this to 100.
PAUSE = 0.1  # (!) Try changing this to 0.0 or 2.0.
STREAM_CHARS = ['с', 'ә', 'л', 'е', 'м', 'д', 'о', 'с', 'т', 'а', 'р', '0', '1', '&', '@']  # (!) Try changing this to other characters.

# Density can range from 0.0 to 1.0:
DENSITY = 0.04  # (!) Try changing this to 0.10 or 0.30.

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]

# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Digital Stream, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Restart a stream on this column.
                    columns[i] = random.randint(MIN_STREAM_LENGTH,MAX_STREAM_LENGTH)

            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()  # Print a newline at the end of the row of columns.
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.