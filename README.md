# Box Drawing Script  

### Description  
This Python script allows a user to draw a **hollow rectangular box** on the console.  
- The user chooses a **single-character symbol**, along with the **width** and **height** of the box.  
- The script validates the inputs to make sure the box can be drawn correctly.  
- If the input is valid, the box is displayed. If not, an **exception message** is shown.  

This project demonstrates:  
- Input validation  
- Exception handling  
- String manipulation for ASCII art  

### Features  
- Draws a hollow rectangular box using any symbol.  
- Validates that the symbol is a **single character**.  
- Ensures **width and height > 2** for a proper box.  
- Graceful error handling with **try/except** blocks.  
- Modular code with a `box()` function and a `main()` function.  

### Script Structure  
#### `box(sym, width, height)`  
- **Parameters:**  
  - `sym` *(str)* → Single-character symbol used for the box borders.  
  - `width` *(int)* → Width of the box (must be > 2).  
  - `height` *(int)* → Height of the box (must be > 2).  
- **Behavior:**  
  - Prints a top border made of `sym`.  
  - Prints middle rows with spaces inside and `sym` on the edges.  
  - Prints a bottom border made of `sym`.  

#### `main()`  
- Collects user input for symbol, width, and height.  
- Validates inputs (raises exceptions for invalid cases).  
- Calls `box()` to draw the box.  
- Handles any runtime exceptions gracefully. 
