from formulas import electrical_engineering
from topic_lib import electrical_engineering_lib
import formula_display.core as core
import formula_display.display_electrical_engineering as fd


def show_formula(formula):
    core.display_formula(formula)


def run_electrical_engineering():
    electrical_engineering_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        i = float(input("Current (A): "))
        r = float(input("Resistance (omega): "))
        print(f"Voltage = {electrical_engineering.ohms_law(i=i, r=r)} V")
        show_formula(fd.ohms_law())

    elif choice == "2":
        v = float(input("Voltage (V): "))
        i = float(input("Current (A): "))
        print(f"Power = {electrical_engineering.electrical_power(v, i)} W")
        show_formula(fd.electrical_power())

    elif choice == "3":
        i = float(input("Current (A): "))
        r = float(input("Resistance (omega): "))
        print(f"Power = {electrical_engineering.power_current(i, r)} W")
        show_formula(fd.power_current())

    elif choice == "4":
        v = float(input("Voltage (V): "))
        r = float(input("Resistance (omega): "))
        print(f"Power = {electrical_engineering.power_voltage(v, r)} W")
        show_formula(fd.power_voltage())

    elif choice == "5":
        p = float(input("Power (W): "))
        t = float(input("Time (s): "))
        print(f"Energy = {electrical_engineering.electrical_energy(p, t)} J")
        show_formula(fd.electrical_energy())

    elif choice == "6":
        values = input("Resistors separated by spaces: ").split()
        resistors = [float(x) for x in values]
        print(f"Total Resistance = {electrical_engineering.series_resistance(*resistors)} omega")
        show_formula(fd.series_resistance())

    elif choice == "7":
        values = input("Resistors separated by spaces: ").split()
        resistors = [float(x) for x in values]
        print(f"Total Resistance = {electrical_engineering.parallel_resistance(*resistors)} omega")
        show_formula(fd.parallel_resistance())

    elif choice == "8":
        r = float(input("Resistance (omega): "))
        print(f"Conductance = {electrical_engineering.conductance(r)} S")
        show_formula(fd.conductance())

    elif choice == "9":
        v_in = float(input("Input Voltage (V): "))
        r1 = float(input("R1 (omega): "))
        r2 = float(input("R2 (omega): "))
        print(f"Output Voltage = {electrical_engineering.voltage_divider(v_in, r1, r2)} V")
        show_formula(fd.voltage_divider())

    elif choice == "10":
        i_total = float(input("Total Current (A): "))
        r1 = float(input("R1 (omega): "))
        r2 = float(input("R2 (omega): "))
        print(f"Branch Current = {electrical_engineering.current_divider(i_total, r1, r2)} A")
        show_formula(fd.current_divider())

    elif choice == "11":
        t = float(input("Period (s): "))
        print(f"Frequency = {electrical_engineering.frequency(t)} Hz")
        show_formula(fd.frequency())

    elif choice == "12":
        f = float(input("Frequency (Hz): "))
        print(f"Period = {electrical_engineering.period(f)} s")
        show_formula(fd.period())

    elif choice == "13":
        f = float(input("Frequency (Hz): "))
        c = float(input("Capacitance (F): "))
        print(f"Capacitive Reactance = {electrical_engineering.capacitive_reactance(f, c)} omega")
        show_formula(fd.capacitive_reactance())

    elif choice == "14":
        f = float(input("Frequency (Hz): "))
        l = float(input("Inductance (H): "))
        print(f"Inductive Reactance = {electrical_engineering.inductive_reactance(f, l)} omega")
        show_formula(fd.inductive_reactance())

    elif choice == "15":
        r = float(input("Resistance (omega): "))
        xl = float(input("Inductive Reactance (omega): "))
        xc = float(input("Capacitive Reactance (omega): "))
        print(f"Impedance = {electrical_engineering.impedance(r, xl, xc)} omega")
        show_formula(fd.impedance())

    elif choice == "16":
        values = input("Voltages separated by spaces: ").split()
        voltages = [float(x) for x in values]
        print(f"Voltage Sum = {electrical_engineering.kvl(*voltages)} V")
        show_formula(fd.kirchhoffs_voltage_law())

    elif choice == "17":
        values = input("Currents separated by spaces: ").split()
        currents = [float(x) for x in values]
        print(f"Current Sum = {electrical_engineering.kcl(*currents)} A")
        show_formula(fd.kirchhoffs_current_law())

    elif choice == "18":
        q1 = float(input("Charge 1 (C): "))
        q2 = float(input("Charge 2 (C): "))
        r = float(input("Distance (m): "))
        print(f"Force = {electrical_engineering.coulombs_law(q1, q2, r)} N")
        show_formula(fd.coulombs_law())

    elif choice == "19":
        force = float(input("Force (N): "))
        charge = float(input("Charge (C): "))
        print(f"Electric Field = {electrical_engineering.electric_field(force, charge)} N/C")
        show_formula(fd.electric_field())

    elif choice == "20":
        work = float(input("Work (J): "))
        charge = float(input("Charge (C): "))
        print(f"Electric Potential = {electrical_engineering.electric_potential(work, charge)} V")
        show_formula(fd.electric_potential())

    elif choice == "0":
        exit()

    else:
        print("Invalid option.")