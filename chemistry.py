from formula import parse_formula, FormulaError

# Periodic table dictionary
periodic_table_dict = {
    "Ac": ["Actinium", 227],
    "Ag": ["Silver", 107.8682],
    "Al": ["Aluminum", 26.9815386],
    "H": ["Hydrogen", 1.00794],
    "O": ["Oxygen", 15.9994],
    # Add more elements as needed
}

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    """
    total_molar_mass = 0

    # Iterate through each symbol and its quantity
    for symbol_quantity in symbol_quantity_list:
        symbol = symbol_quantity[SYMBOL_INDEX]
        quantity = symbol_quantity[QUANTITY_INDEX]

        # Handle missing symbols
        if symbol not in periodic_table_dict:
            raise KeyError(f"Element '{symbol}' not found in periodic table.")

        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]

        # Ensure quantity is a positive integer
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError(f"Quantity for '{symbol}' must be a positive integer.")

        # Multiply the atomic mass by the quantity and add to total molar mass
        total_molar_mass += atomic_mass * quantity

    return total_molar_mass

# Example of using parse_formula and compute_molar_mass
if __name__ == "__main__":
    formula = "H2O"  # Example chemical formula
    try:
        symbol_quantity_list = parse_formula(formula, periodic_table_dict)
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
        print(f"Molar mass of {formula}: {molar_mass:.4f} g/mol")
    except (FormulaError, KeyError, ValueError) as e:
        print(f"Error: {e}")
