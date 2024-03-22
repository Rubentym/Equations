def balance_equation(equation):
    reactants, products = equation.split('->')
    reactant_atoms = count_atoms(reactants.strip())
    product_atoms = count_atoms(products.strip())
    
    balanced_equation = ''
    for atom, count in reactant_atoms.items():
        product_count = product_atoms.get(atom, 0)
        if count != product_count:
            multiplier = product_count / count
            balanced_equation += f"{multiplier}{atom} + "
    
    balanced_equation += "-> " + products.strip()
    return balanced_equation

equation = "H2 + O2 -> H2O"
print("Unbalanced Equation:", equation)
print("Balanced Equation:", balance_equation(equation))
