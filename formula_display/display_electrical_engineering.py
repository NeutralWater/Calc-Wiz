from formula_display.core import make_formula

def ohms_law():
    return make_formula(
        "V = IR",
        {
            "V": "Voltage (volts)",
            "I": "Current (amperes)",
            "R": "Resistance (ohms)"
        },
        topic="Ohm's Law"
    )


def electrical_power():
    return make_formula(
        "P = VI",
        {
            "P": "Power (watts)",
            "V": "Voltage (volts)",
            "I": "Current (amperes)"
        },
        topic="Electrical Power"
    )


def power_current():
    return make_formula(
        "P = I²R",
        {
            "P": "Power (watts)",
            "I": "Current (amperes)",
            "R": "Resistance (ohms)"
        },
        topic="Power from Current"
    )


def power_voltage():
    return make_formula(
        "P = V²/R",
        {
            "P": "Power (watts)",
            "V": "Voltage (volts)",
            "R": "Resistance (ohms)"
        },
        topic="Power from Voltage"
    )


def electrical_energy():
    return make_formula(
        "E = Pt",
        {
            "E": "Energy (joules)",
            "P": "Power (watts)",
            "t": "Time (seconds)"
        },
        topic="Electrical Energy"
    )


def series_resistance():
    return make_formula(
        "Rₜ = R₁ + R₂ + ...",
        {
            "Rₜ": "Total resistance",
            "R₁, R₂": "Individual resistances"
        },
        topic="Series Resistance"
    )


def parallel_resistance():
    return make_formula(
        "1/Rₜ = 1/R₁ + 1/R₂ + ...",
        {
            "Rₜ": "Total resistance",
            "R₁, R₂": "Individual resistances"
        },
        topic="Parallel Resistance"
    )


def conductance():
    return make_formula(
        "G = 1/R",
        {
            "G": "Conductance (siemens)",
            "R": "Resistance (ohms)"
        },
        topic="Conductance"
    )


def voltage_divider():
    return make_formula(
        "Vₒ = Vᵢ(R₂/(R₁+R₂))",
        {
            "Vₒ": "Output voltage",
            "Vᵢ": "Input voltage",
            "R₁, R₂": "Resistors"
        },
        topic="Voltage Divider"
    )


def current_divider():
    return make_formula(
        "I₁ = Iₜ(R₂/(R₁+R₂))",
        {
            "I₁": "Branch current",
            "Iₜ": "Total current",
            "R₁, R₂": "Parallel resistors"
        },
        topic="Current Divider"
    )


def frequency():
    return make_formula(
        "f = 1/T",
        {
            "f": "Frequency (hertz)",
            "T": "Period (seconds)"
        },
        topic="Frequency"
    )


def period():
    return make_formula(
        "T = 1/f",
        {
            "T": "Period (seconds)",
            "f": "Frequency (hertz)"
        },
        topic="Period"
    )


def capacitive_reactance():
    return make_formula(
        "Xc = 1/(2πfC)",
        {
            "Xc": "Capacitive reactance (ohms)",
            "f": "Frequency (hertz)",
            "C": "Capacitance (farads)"
        },
        topic="Capacitive Reactance"
    )


def inductive_reactance():
    return make_formula(
        "Xl = 2πfL",
        {
            "Xl": "Inductive reactance (ohms)",
            "f": "Frequency (hertz)",
            "L": "Inductance (henrys)"
        },
        topic="Inductive Reactance"
    )


def impedance():
    return make_formula(
        "Z = √(R² + (Xl - Xc)²)",
        {
            "Z": "Impedance (ohms)",
            "R": "Resistance",
            "Xl": "Inductive reactance",
            "Xc": "Capacitive reactance"
        },
        topic="Impedance"
    )


def kirchhoffs_voltage_law():
    return make_formula(
        "ΣV = 0",
        {
            "ΣV": "Sum of voltages around a closed loop"
        },
        topic="Kirchhoff's Voltage Law"
    )


def kirchhoffs_current_law():
    return make_formula(
        "ΣI(in) = ΣI(out)",
        {
            "ΣI": "Sum of currents entering equals leaving a junction"
        },
        topic="Kirchhoff's Current Law"
    )


def coulombs_law():
    return make_formula(
        "F = k(q₁q₂/r²)",
        {
            "F": "Electrostatic force (newtons)",
            "k": "Coulomb's constant",
            "q₁, q₂": "Charges (coulombs)",
            "r": "Distance (meters)"
        },
        topic="Coulomb's Law"
    )


def electric_field():
    return make_formula(
        "E = F/q",
        {
            "E": "Electric field (N/C)",
            "F": "Force (newtons)",
            "q": "Test charge (coulombs)"
        },
        topic="Electric Field"
    )


def electric_potential():
    return make_formula(
        "V = W/q",
        {
            "V": "Electric potential (volts)",
            "W": "Work (joules)",
            "q": "Charge (coulombs)"
        },
        topic="Electric Potential"
    )