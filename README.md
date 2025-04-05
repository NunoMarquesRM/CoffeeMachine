# Coffee Machine Program

A Python-based coffee machine simulator that allows users to order drinks, process payments, and manage resources.

## Features

### Drink Options
- **Espresso** ($1.50)
  - 50ml water
  - 18g coffee
- **Latte** ($2.50)
  - 200ml water
  - 150ml milk
  - 24g coffee
- **Cappuccino** ($3.00)
  - 250ml water
  - 100ml milk
  - 24g coffee

### Resource Management
- Tracks available resources:
  - Water (in milliliters)
  - Milk (in milliliters)
  - Coffee (in grams)
- Automatically deducts resources when drinks are made
- Prevents orders when resources are insufficient

### Payment System
- Accepts multiple coin types:
  - Quarters (25¢)
  - Dimes (10¢)
  - Nickels (5¢)
  - Pennies (1¢)
- Calculates and returns change
- Tracks total profit

### Special Commands
- `report`: Displays current resource levels and profit
- `off`: Turns off the machine and shows final profit

## Usage

1. Run the program using Python:
   ```bash
   python main.py
   ```

2. Choose from the following options:
   - Type `espresso`, `latte`, or `cappuccino` to order a drink
   - Type `report` to check resource levels
   - Type `off` to turn off the machine

3. When ordering a drink:
   - The machine will check if resources are sufficient
   - If resources are available, you'll be prompted to insert coins
   - After successful payment, your drink will be prepared
   - Any change will be returned

## Error Handling
- Prevents orders when resources are insufficient
- Validates payment amounts
- Handles invalid drink selections
- Case-insensitive input handling

## Technical Details
- Written in Python
- Uses dictionary data structures for menu and resources
- Modular design with separate functions for different operations
- Comprehensive documentation with docstrings 