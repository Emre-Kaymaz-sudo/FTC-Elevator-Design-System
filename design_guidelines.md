# Elevator and Slider Mechanism Design Guidelines for FTC

## Table of Contents
1. [Mechanism Types](#mechanism-types)
2. [Material Selection](#material-selection)
3. [Motor Selection](#motor-selection)
4. [Gear Ratio Selection](#gear-ratio-selection)
5. [Mechanical Design Considerations](#mechanical-design-considerations)
6. [Programming and Control](#programming-and-control)
7. [Testing and Iteration](#testing-and-iteration)
8. [Common Pitfalls](#common-pitfalls)

## Mechanism Types

### Cascading Elevator
- **Description**: Multiple stages that extend sequentially
- **Pros**: High extension-to-retracted ratio, compact when retracted
- **Cons**: More complex to build, higher friction, requires precise alignment
- **Best For**: High-reach applications with limited base footprint

### Continuous Elevator
- **Description**: Single extending section
- **Pros**: Simpler design, lower friction, easier to build
- **Cons**: Limited extension range, larger footprint when retracted
- **Best For**: Medium-height applications, simpler robots

### Linear Slider
- **Description**: Horizontal motion system
- **Pros**: Easier balance, lower power requirements
- **Cons**: Limited to horizontal plane, requires more space
- **Best For**: Reaching objects at the same height but different distances

## Material Selection

### Structural Elements
- **Aluminum Extrusion** (e.g., MakerBeam, REV Rail): Lightweight, easy to modify, good strength-to-weight ratio
- **Carbon Fiber**: High strength, very lightweight, but expensive and difficult to modify
- **3D Printed Parts**: Good for custom brackets and connectors, but weaker than metal

### Motion Components
- **Drawer Slides**: Inexpensive, but heavy and can have alignment issues
- **Linear Bearings**: Smooth operation, reduced friction, but more expensive
- **V-Groove Wheels**: Good middle ground, relatively inexpensive with good performance

### Cable/Chain Systems
- **Timing Belts**: Low stretch, positive engagement, clean operation
- **Spectra/Dyneema Line**: Very lightweight, strong, but may require tensioning
- **Roller Chain**: Very strong, positive engagement, but heavy and requires maintenance

## Motor Selection

### Key Specifications to Consider
- **Stall Torque**: Maximum torque the motor can produce (usually at 0 RPM)
- **Free Speed**: Maximum speed with no load
- **Power Curve**: Where on the torque-speed curve the motor operates most efficiently
- **Current Draw**: Especially important during stall conditions

### Common FTC Motor Options
- **Andymark NeveRest**: Good general-purpose motors
- **REV HD Hex**: Standard motor for many applications
- **GoBILDA Yellow Jacket**: Various gear ratios available built-in
- **Tetrix TorqueNADO**: High torque options

### Motors vs Servos
- **Motors**: Better for continuous motion, higher power, require encoders for position
- **Servos**: Built-in position control, easier to program, limited motion range
- **High-Torque Servos**: Good middle ground for some applications

## Gear Ratio Selection

### Understanding the Speed-Torque Tradeoff
- Lower gear ratio = Higher speed, Lower torque
- Higher gear ratio = Lower speed, Higher torque

### Calculating Required Torque
```
T = (m × g × r) + (m × a × r) + T_friction
```
Where:
- T = required torque (Nm)
- m = mass to be lifted (kg)
- g = gravitational acceleration (9.81 m/s²)
- r = force arm (m) - pulley radius or gear distance
- a = desired acceleration (m/s²)
- T_friction = torque required to overcome friction

### Calculating Optimal Gear Ratio
```
Gear Ratio = (Motor RPM × π × D) ÷ (60 × Desired Linear Speed)
```
Where:
- D = drive pulley or gear diameter (m)
- Desired Linear Speed = slider movement speed (m/s)

### Practical Considerations
- Account for system efficiency (typically 70-90%)
- Consider standard available ratios (common FTC gearboxes offer 20:1, 40:1, etc.)
- Factor in startup current draw (avoid stalling during startup)
- Build in a safety factor of 1.5-2x the calculated required torque

## Mechanical Design Considerations

### Stability and Alignment
- Ensure parallel rails with precise alignment
- Use properly sized bearings and bushings
- Consider cross-bracing for taller structures
- Minimize slop in all connections

### Cable/Chain Management
- Provide appropriate tensioning mechanisms
- Use idler pulleys to maintain proper engagement
- Consider cable stretch over time
- Ensure cable/chain paths avoid interference

### Limit Switches and Hard Stops
- Implement physical hard stops to prevent over-extension
- Use limit switches or sensors for software limits
- Design fail-safe mechanical systems

### Weight Distribution
- Balance the robot considering all positions of the mechanism
- Consider counterweights for tall elevators
- Minimize moving mass to reduce required power

## Programming and Control

### Motion Profiling
- Implement acceleration and deceleration curves
- Avoid sudden starts and stops that stress the mechanism
- Consider using PID control for position accuracy

### Position Control
- Use encoders for closed-loop position feedback
- Implement software limits before physical limits
- Create preset positions for common tasks

### Power Management
- Monitor current draw during operation
- Implement software current limiting
- Provide appropriate power delivery (wire gauge, voltage regulation)

## Testing and Iteration

### Load Testing
- Test with weights exceeding competition requirements
- Test with various load positions
- Verify performance throughout battery discharge cycle

### Durability Testing
- Cycle the mechanism repeatedly to identify wear points
- Test under various environmental conditions
- Simulate competition scenarios

### Data Collection
- Record speed, current draw, and position accuracy
- Compare actual performance to calculated values
- Use data to refine the design

## Common Pitfalls

### Undersized Motors/Gear Ratios
- **Symptom**: Mechanism stalls or moves slowly under load
- **Solution**: Increase gear ratio or use higher-torque motors

### Excessive Friction
- **Symptom**: High current draw, jerky motion
- **Solution**: Improve alignment, use better bearings, reduce binding points

### Mechanical Binding
- **Symptom**: Mechanism gets stuck at certain positions
- **Solution**: Improve alignment, add guides, increase clearances

### Structural Weakness
- **Symptom**: Flexing, bending, or failing under load
- **Solution**: Reinforce weak points, use stronger materials, improve bracing

### Cable/Chain Issues
- **Symptom**: Skipping, slipping, or derailing
- **Solution**: Improve tensioning, check alignment, use proper guides

Remember, the best elevator designs in FTC are often those that balance simplicity with reliability rather than those with the most features or highest reach. Start with a conservative design and iterate based on testing results.