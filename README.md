# FTC Elevator Design System

## Overview
This repository contains tools and guidelines for designing elevator and slider mechanisms for FTC robots with a focus on optimal gear ratio selection.

## Contents
- **Calculator Tool**: Interactive calculator for determining the optimal gear ratio
- **Design Guidelines**: Best practices for elevator and slider mechanisms
- **Example Calculations**: Sample scenarios with detailed calculations
- **Common Pitfalls**: Mistakes to avoid when designing lift systems

## Key Formulas

### Torque Calculation
```
T = (m × g × r) + (m × a × r)
```
Where:
- T = required torque (Nm)
- m = mass to be lifted (kg)
- g = gravitational acceleration (9.81 m/s²)
- r = force arm (m) - pulley radius or gear distance
- a = desired acceleration (m/s²)

### Optimal Gear Ratio Formula
```
Gear Ratio = (Motor RPM × π × D) ÷ (60 × Desired Linear Speed)
```
Where:
- D = drive pulley or gear diameter (m)
- Desired Linear Speed = slider movement speed (m/s)

## Typical Values for FTC Robots
- Gear ratios between 5:1 and 10:1 are common starting points
- Linear speeds of 0.5-1 m/s are typically sufficient
- Always account for efficiency losses (typically 70-90%)