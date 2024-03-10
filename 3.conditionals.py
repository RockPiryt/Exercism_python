"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    if temperature < 800 and neutrons_emitted > 500 and temperature*neutrons_emitted < 500000:
        return True
    else:
        return False

result_1 = is_criticality_balanced(750, 650)
print(result_1)


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current #1000*999
    percentage_value = (generated_power / theoretical_max_power)*100
    # print(percentage_value)

    if percentage_value >= 80:
        efficiency = "green"
        return efficiency
    elif percentage_value >= 60 and percentage_value < 80:
        efficiency = "orange"
        return efficiency
    elif percentage_value >= 30 and percentage_value < 60:
        efficiency = "red"
        return efficiency
    elif percentage_value  < 30:
        efficiency = "black"
        return efficiency
    
        


result_2 = reactor_efficiency(200,50,15000)#should return orange
print(result_2)



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    actual_state = temperature * neutrons_produced_per_second
    print(f"actual state: {actual_state}")

    percentage_value = (actual_state / threshold) * 100
    print(f"normal percentage {percentage_value} %")

    if percentage_value < 90: 
        
        critical_state = "LOW"
        return critical_state
    elif percentage_value >= 90 and percentage_value <= 110:
        critical_state = "NORMAL"
        return critical_state
    elif percentage_value > 110:
        critical_state = "DANGER"
        return critical_state
    
result_3 = fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
print(result_3)
#should be 'DANGER'
#600% = 30 000
#90% = 0.9 *5000 = 4500 0.9*threshold
#110% =1.1 * 5000 =  5500 = 1.1*threshold