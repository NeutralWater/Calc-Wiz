from formulas import digital_electronics
from topic_lib import digital_electronics_lib
import formula_display.core as core
import formula_display.display_digital_electronics as fd


def show_formula(formula):
    core.display_formula(formula)

def run_digital_electronics():
    digital_electronics_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        e = input("Boolean expression: ")
        print("")
        print(f"Simplified = {digital_electronics.simplify_boolean_expression(e)}")
        show_formula(fd.simplify_boolean_expression())
    
    elif choice == "2":
        e = input("Boolean expression: ")
        print("")
        print(digital_electronics.format_truth_table(e))
        show_formula(fd.truth_table())

    elif choice == "3":
        e = input("Boolean expression: ")
        print("")
        print(digital_electronics.generate_kmap(e))
        show_formula(fd.karnaugh_map())

    elif choice == "0":
        exit()