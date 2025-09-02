def drawBox(sym, width, height): 
    """
    Draws a hollow rectangular box using the given symbol, width, and height.
    """
    # Print top border
    print(sym * width)

    # Print middle rows with spaces inside
    for i in range(height - 2):
        print(sym + ' ' * (width - 2) + sym)

    # Print bottom border
    print(sym * width)

def main():
    """
    Main function: gets user input for symbol, width, and height,
    validates input, then draws the box.
    """

    # Ask user for a symbol
    sym = (input('Choose a single character symbol:> '))
    if len(sym) != 1:  # Validate length
        raise Exception('Symbol must be a single character.')

    # Ask for width
    width = int(input('Choose the width of the box:> '))
    if width <= 2:  # Must be > 2 to form a box
        raise Exception('Width must be greater than 2.')
    
    # Ask for height
    height = int(input('Choose the height of the box:> '))
    if height <= 2:  # Must be > 2 to form a box
        raise Exception('Height must be greater than 2.')
    
    try:
        drawBox(sym, width, height)  # Attempt to draw box
    except Exception as err:     # Catch any runtime errors
        print('There was an Exception: ' + str(err))

# Entry point check
if __name__ == "__main__":
    main()
