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
