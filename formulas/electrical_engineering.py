from formulas import constant_values as c
import math

def ohms_law(v=None, i=None, r=None):
    if v is None:
        return i * r
    elif i is None:
        return v / r
    elif r is None:
        return v / i

def electrical_power(v, i):
    return v * i

def power_current(i, r):
    return i ** 2 * r

def power_voltage(v, r):
    return v**2 / r

def electrical_energy(p, t):
    return p * t

def series_resistance(*resistors):
    return sum(resistors)

def parallel_resistance(*resistors):
    return 1 / sum(1 / r for r in resistors)
    
def conductance(r):
    return 1 / r

def voltage_divider(v_in, r1, r2):
    return v_in * (r2 / (r1 + r2))
    
def current_divider(i_total, r1, r2):
    return i_total * (r2 / (r1 + r2))
    
def frequency(period):
    return 1 / period
    
def period(frequency):
    return 1 / frequency
    
def capacitive_reactance(frequency, capacitance):
    return 1 / (2 * math.pi * frequency * capacitance)
    
def inductive_reactance(frequency, inductance):
    return 2 * math.pi * frequency * inductance
    
def impedance(r, x1, xc):
    return math.sqrt(r ** 2 + (x1 - xc) ** 2)
    
def kirchhoffs_voltage_law(*voltages):
    return sum(voltages)
    
def kirchhoffs_current_law(*currents):
    return sum(currents)
    
def coulombs_law(q1, q2, r):
    return c.K * q1 * q2 / (r ** 2)
    
def electric_field(force, charge):
    return force / charge
    
def electric_potential(work, charge):
    return work / charge