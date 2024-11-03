import re

class FormulaError(Exception):
    pass

def parse_formula(formula, periodic_table_dict):
    # Regex pattern for elements with optional quantities
    pattern = r'([A-Z][a-z]?)(\d*)|(\()|(\))|([^A-Za-z0-9()])'
    matches = re.findall(pattern, formula)
    
    stack = []
    symbol_quantity_list = []
    current_multiplier = 1

    for element, quantity, open_paren, close_paren, invalid in matches:
        if invalid:
            raise FormulaError(f"illegal character: '{invalid}'")

        if open_paren:
            stack.append(current_multiplier)
            current_multiplier = 1  # Reset multiplier for the group
        elif close_paren:
            if not stack:
                raise FormulaError("unmatched close parenthesis")
            current_multiplier = stack.pop()  # Pop the last multiplier
        elif element:
            quantity = int(quantity) if quantity else 1  # Default to 1
            if quantity == 0:
                raise FormulaError("quantity begins with zero")
            if element not in periodic_table_dict:
                raise FormulaError(f"unknown element symbol: '{element}'")

            symbol_quantity_list.append((element, quantity * current_multiplier))
        else:
            raise FormulaError("unmatched open parenthesis")

    if stack:
        raise FormulaError("unmatched open parenthesis")

    return symbol_quantity_list
