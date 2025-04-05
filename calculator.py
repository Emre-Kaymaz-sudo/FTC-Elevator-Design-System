import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_required_torque(mass_kg, radius_m, acceleration_m_s2=1.0, friction_coefficient=0.1):
    """
    Calculate the required torque to lift a mass.
    
    Parameters:
    - mass_kg: Mass to be lifted in kilograms
    - radius_m: Radius of pulley or gear in meters
    - acceleration_m_s2: Desired acceleration in m/s^2 (default: 1.0)
    - friction_coefficient: Coefficient of friction (default: 0.1)
    
    Returns:
    - Required torque in Nm
    """
    gravity = 9.81  # m/s^2
    
    # Calculate gravitational component
    gravity_torque = mass_kg * gravity * radius_m
    
    # Calculate acceleration component
    acceleration_torque = mass_kg * acceleration_m_s2 * radius_m
    
    # Calculate friction component
    friction_torque = mass_kg * gravity * friction_coefficient * radius_m
    
    # Total required torque
    total_torque = gravity_torque + acceleration_torque + friction_torque
    
    return total_torque

def calculate_optimal_gear_ratio(motor_rpm, pulley_diameter_m, desired_linear_speed_m_s, efficiency=0.85):
    """
    Calculate the optimal gear ratio for an elevator system.
    
    Parameters:
    - motor_rpm: No-load RPM of the motor
    - pulley_diameter_m: Diameter of the pulley in meters
    - desired_linear_speed_m_s: Desired linear speed in m/s
    - efficiency: Efficiency of the gear system (default: 0.85)
    
    Returns:
    - Optimal gear ratio
    """
    # Calculate the required RPM at the output shaft
    required_rpm = (desired_linear_speed_m_s * 60) / (math.pi * pulley_diameter_m)
    
    # Calculate the optimal gear ratio
    gear_ratio = motor_rpm / required_rpm
    
    # Adjust for efficiency
    adjusted_gear_ratio = gear_ratio / efficiency
    
    return adjusted_gear_ratio

def calculate_final_specs(motor_rpm, motor_torque_nm, gear_ratio, pulley_diameter_m, efficiency=0.85):
    """
    Calculate the final specifications of the system.
    
    Parameters:
    - motor_rpm: No-load RPM of the motor
    - motor_torque_nm: Stall torque of the motor in Nm
    - gear_ratio: Selected gear ratio
    - pulley_diameter_m: Diameter of the pulley in meters
    - efficiency: Efficiency of the gear system (default: 0.85)
    
    Returns:
    - Dictionary with final specifications
    """
    # Calculate output RPM
    output_rpm = motor_rpm / gear_ratio
    
    # Calculate output torque
    output_torque = motor_torque_nm * gear_ratio * efficiency
    
    # Calculate linear speed
    linear_speed = (output_rpm * math.pi * pulley_diameter_m) / 60
    
    # Calculate maximum mass that can be lifted
    max_mass = output_torque / (9.81 * pulley_diameter_m / 2)
    
    return {
        "output_rpm": output_rpm,
        "output_torque_nm": output_torque,
        "linear_speed_m_s": linear_speed,
        "max_mass_kg": max_mass
    }

def plot_gear_ratio_comparison(motor_rpm, motor_torque_nm, pulley_diameter_m, mass_kg, 
                               gear_ratios=None, efficiency=0.85):
    """
    Plot a comparison of different gear ratios.
    
    Parameters:
    - motor_rpm: No-load RPM of the motor
    - motor_torque_nm: Stall torque of the motor in Nm
    - pulley_diameter_m: Diameter of the pulley in meters
    - mass_kg: Mass to be lifted in kilograms
    - gear_ratios: List of gear ratios to compare (default: [5, 7, 10, 15, 20])
    - efficiency: Efficiency of the gear system (default: 0.85)
    """
    if gear_ratios is None:
        gear_ratios = [5, 7, 10, 15, 20]
    
    speeds = []
    torques = []
    max_masses = []
    
    for ratio in gear_ratios:
        specs = calculate_final_specs(motor_rpm, motor_torque_nm, ratio, pulley_diameter_m, efficiency)
        speeds.append(specs["linear_speed_m_s"])
        torques.append(specs["output_torque_nm"])
        max_masses.append(specs["max_mass_kg"])
    
    # Create the figure and primary axis
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plot linear speed on primary axis
    ax1.set_xlabel('Gear Ratio')
    ax1.set_ylabel('Linear Speed (m/s)', color='b')
    ax1.plot(gear_ratios, speeds, 'b-', marker='o', label='Linear Speed')
    ax1.tick_params(axis='y', labelcolor='b')
    
    # Create secondary axis for torque
    ax2 = ax1.twinx()
    ax2.set_ylabel('Output Torque (Nm)', color='r')
    ax2.plot(gear_ratios, torques, 'r-', marker='s', label='Output Torque')
    ax2.tick_params(axis='y', labelcolor='r')
    
    # Add a horizontal line for the required torque
    required_torque = calculate_required_torque(mass_kg, pulley_diameter_m/2)
    ax2.axhline(y=required_torque, color='g', linestyle='--', 
                label=f'Required Torque for {mass_kg}kg: {required_torque:.2f}Nm')
    
    # Add title and legend
    plt.title('Gear Ratio Comparison')
    
    # Create combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', bbox_to_anchor=(0.5, -0.15))
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('gear_ratio_comparison.png')
    plt.close()
    
    return 'gear_ratio_comparison.png'

if __name__ == "__main__":
    # Example calculation based on the provided scenario
    print("FTC Elevator System Calculator")
    print("-" * 30)
    
    # Input parameters
    mass = float(input("Enter mass to be lifted (kg): ") or "2.0")
    motor_rpm = float(input("Enter motor no-load RPM: ") or "6000")
    motor_torque = float(input("Enter motor stall torque (Nm): ") or "0.17")  # Example for a typical FTC motor
    pulley_diameter = float(input("Enter pulley diameter (cm): ") or "2.0") / 100  # Convert cm to m
    desired_speed = float(input("Enter desired linear speed (m/s): ") or "0.8")
    
    # Calculate required torque
    req_torque = calculate_required_torque(mass, pulley_diameter/2)
    print(f"\nRequired torque: {req_torque:.2f} Nm")
    
    # Calculate optimal gear ratio
    opt_ratio = calculate_optimal_gear_ratio(motor_rpm, pulley_diameter, desired_speed)
    print(f"Calculated optimal gear ratio: {opt_ratio:.2f}:1")
    
    # Round to nearest standard gear ratio for practicality
    standard_ratios = [5, 7, 10, 15, 20]
    nearest_ratio = min(standard_ratios, key=lambda x: abs(x - opt_ratio))
    print(f"Nearest standard gear ratio: {nearest_ratio}:1")
    
    # Calculate final specifications with the standard ratio
    final_specs = calculate_final_specs(motor_rpm, motor_torque, nearest_ratio, pulley_diameter)
    
    print("\nFinal System Specifications:")
    print(f"Output RPM: {final_specs['output_rpm']:.2f}")
    print(f"Output Torque: {final_specs['output_torque_nm']:.2f} Nm")
    print(f"Linear Speed: {final_specs['linear_speed_m_s']:.2f} m/s")
    print(f"Maximum Mass Capacity: {final_specs['max_mass_kg']:.2f} kg")
    
    # Determine if the system can lift the required mass
    if final_specs['max_mass_kg'] >= mass:
        print("\nSTATUS: ✅ The system can successfully lift the required mass.")
    else:
        print("\nSTATUS: ❌ The system CANNOT lift the required mass. Consider:")
        print("  - Increasing the gear ratio")
        print("  - Using a motor with higher torque")
        print("  - Reducing the mass to be lifted")
    
    # Generate comparison plot
    print("\nGenerating gear ratio comparison plot...")
    plot_path = plot_gear_ratio_comparison(motor_rpm, motor_torque, pulley_diameter, mass)
    print(f"Plot saved as: {plot_path}")
    
    print("\nDon't forget to consider:")
    print("- Motor efficiency decreases under load")
    print("- Actual performance may vary due to friction and other factors")
    print("- Always test your system with a safety factor of 1.5-2x")