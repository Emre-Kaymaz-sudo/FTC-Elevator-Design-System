# Example Elevator Calculations

This document provides detailed calculations for common FTC elevator and slider mechanism scenarios. These examples can be used as a starting point for your own design.

## Scenario 1: Basic Elevator for Game Elements

### Requirements
- Lift a 0.5 kg game element
- Reach height of 0.6 meters
- Desired linear speed of 0.7 m/s

### Motor Information
- Using a REV HD Hex Motor
- No-load speed: 6000 RPM
- Stall torque: 0.17 Nm

### Mechanical Configuration
- Pulley diameter: 2 cm (0.02 m)
- Estimated mechanism weight: 1.2 kg
- Total mass to lift: 1.7 kg (mechanism + game element)

### Calculations

1. **Required Torque Calculation**:
   ```
   T = (m × g × r) + (m × a × r) + T_friction
   ```
   
   Where:
   - m = 1.7 kg
   - g = 9.81 m/s²
   - r = 0.01 m (pulley radius)
   - a = 1.0 m/s² (desired acceleration)
   - T_friction = m × g × 0.1 × r (assuming 10% friction coefficient)
   
   ```
   T = (1.7 × 9.81 × 0.01) + (1.7 × 1.0 × 0.01) + (1.7 × 9.81 × 0.1 × 0.01)
   T = 0.167 + 0.017 + 0.017
   T = 0.201 Nm
   ```

2. **Optimal Gear Ratio Calculation**:
   ```
   Gear Ratio = (Motor RPM × π × D) ÷ (60 × Desired Linear Speed)
   ```
   
   Where:
   - Motor RPM = 6000
   - D = 0.02 m
   - Desired Linear Speed = 0.7 m/s
   
   ```
   Gear Ratio = (6000 × 3.14159 × 0.02) ÷ (60 × 0.7)
   Gear Ratio = 377 ÷ 42
   Gear Ratio = 8.98
   ```

3. **Adjusted for Efficiency**:
   Assuming 85% efficiency in the gear system:
   ```
   Adjusted Ratio = 8.98 ÷ 0.85 = 10.56
   ```
   
   Nearest standard ratio: 10:1

4. **Final Specifications**:
   - Output RPM = 6000 ÷ 10 = 600 RPM
   - Output Torque = 0.17 × 10 × 0.85 = 1.445 Nm
   - Linear Speed = (600 × 3.14159 × 0.02) ÷ 60 = 0.628 m/s
   - Maximum Lift Capacity = 1.445 ÷ (9.81 × 0.01) = 14.73 kg

5. **Safety Check**:
   - Required torque: 0.201 Nm
   - Available torque: 1.445 Nm
   - Safety factor: 1.445 ÷ 0.201 = 7.19
   
   This is well above the recommended safety factor of 1.5-2x, indicating a very robust design.

---

## Scenario 2: Heavy-Duty Cascading Elevator

### Requirements
- Lift a 2.5 kg game element
- Reach height of 1.2 meters
- Desired linear speed of 0.5 m/s

### Motor Information
- Using a GoBILDA Yellow Jacket 5202 Series (435 RPM)
- No-load speed: 435 RPM (already geared down internally)
- Stall torque: 3.2 Nm

### Mechanical Configuration
- Pulley diameter: 3.5 cm (0.035 m)
- Estimated mechanism weight: 3.5 kg
- Total mass to lift: 6.0 kg (mechanism + game element)

### Calculations

1. **Required Torque Calculation**:
   ```
   T = (m × g × r) + (m × a × r) + T_friction
   ```
   
   Where:
   - m = 6.0 kg
   - g = 9.81 m/s²
   - r = 0.0175 m (pulley radius)
   - a = 0.8 m/s² (desired acceleration)
   - T_friction = m × g × 0.15 × r (assuming 15% friction due to cascading stages)
   
   ```
   T = (6.0 × 9.81 × 0.0175) + (6.0 × 0.8 × 0.0175) + (6.0 × 9.81 × 0.15 × 0.0175)
   T = 1.03 + 0.084 + 0.154
   T = 1.268 Nm
   ```

2. **Optimal Gear Ratio Calculation**:
   Since the motor is already pre-geared to 435 RPM, we calculate the ratio from this base.
   ```
   Gear Ratio = (Motor RPM × π × D) ÷ (60 × Desired Linear Speed)
   ```
   
   Where:
   - Motor RPM = 435
   - D = 0.035 m
   - Desired Linear Speed = 0.5 m/s
   
   ```
   Gear Ratio = (435 × 3.14159 × 0.035) ÷ (60 × 0.5)
   Gear Ratio = 47.76 ÷ 30
   Gear Ratio = 1.59
   ```

3. **Adjusted for Efficiency**:
   Assuming 80% efficiency due to the cascading design:
   ```
   Adjusted Ratio = 1.59 ÷ 0.8 = 1.99
   ```
   
   Nearest standard ratio: 2:1

4. **Final Specifications**:
   - Output RPM = 435 ÷ 2 = 217.5 RPM
   - Output Torque = 3.2 × 2 × 0.8 = 5.12 Nm
   - Linear Speed = (217.5 × 3.14159 × 0.035) ÷ 60 = 0.398 m/s
   - Maximum Lift Capacity = 5.12 ÷ (9.81 × 0.0175) = 29.8 kg

5. **Safety Check**:
   - Required torque: 1.268 Nm
   - Available torque: 5.12 Nm
   - Safety factor: 5.12 ÷ 1.268 = 4.04
   
   This is well above the recommended safety factor, indicating a robust design.

---

## Scenario 3: High-Speed Slider Mechanism

### Requirements
- Move a 1.0 kg scoring mechanism horizontally
- Travel distance of 0.75 meters
- Desired linear speed of 1.2 m/s

### Motor Information
- Using a NeveRest 40 Motor
- No-load speed: 160 RPM (already geared down internally)
- Stall torque: 2.6 Nm

### Mechanical Configuration
- Sprocket diameter: 4.0 cm (0.04 m)
- Estimated mechanism weight: 2.0 kg
- Total mass to move: 3.0 kg (mechanism + scoring device)

### Calculations

1. **Required Torque Calculation**:
   For horizontal motion, we don't need to overcome gravity, but we do need to overcome friction and provide acceleration:
   ```
   T = (m × a × r) + (m × g × μ × r)
   ```
   
   Where:
   - m = 3.0 kg
   - a = 2.0 m/s² (higher acceleration for quick movements)
   - r = 0.02 m (sprocket radius)
   - μ = 0.2 (friction coefficient for horizontal sliding)
   - g = 9.81 m/s²
   
   ```
   T = (3.0 × 2.0 × 0.02) + (3.0 × 9.81 × 0.2 × 0.02)
   T = 0.12 + 0.118
   T = 0.238 Nm
   ```

2. **Optimal Gear Ratio Calculation**:
   ```
   Gear Ratio = (Motor RPM × π × D) ÷ (60 × Desired Linear Speed)
   ```
   
   Where:
   - Motor RPM = 160
   - D = 0.04 m
   - Desired Linear Speed = 1.2 m/s
   
   ```
   Gear Ratio = (160 × 3.14159 × 0.04) ÷ (60 × 1.2)
   Gear Ratio = 20.11 ÷ 72
   Gear Ratio = 0.28
   ```

   Since this is less than 1, we need to use a step-up ratio rather than a reduction.

3. **Adjusted for Efficiency**:
   Assuming 90% efficiency for a horizontal system:
   ```
   Adjusted Ratio = 0.28 ÷ 0.9 = 0.31
   ```
   
   This means we need a 1:3 ratio (motor turns 1, output turns 3)

4. **Final Specifications**:
   - Output RPM = 160 × 3 = 480 RPM
   - Output Torque = 2.6 ÷ 3 × 0.9 = 0.78 Nm
   - Linear Speed = (480 × 3.14159 × 0.04) ÷ 60 = 1.005 m/s
   - Maximum Force = 0.78 ÷ 0.02 = 39 N

5. **Safety Check**:
   - Required torque: 0.238 Nm
   - Available torque: 0.78 Nm
   - Safety factor: 0.78 ÷ 0.238 = 3.28
   
   This provides a good safety margin for the horizontal motion system.

---

## Summary of Design Principles from Examples

1. **Always calculate required torque first**, then determine the gear ratio.
2. **Include all sources of torque**: gravitational, acceleration, and friction.
3. **Account for system efficiency** when calculating the final gear ratio.
4. **Round to standard ratios** that are available or easily constructed.
5. **Verify the safety factor** is at least 1.5-2× the required torque.
6. **Consider the final speed** to ensure it meets your performance requirements.
7. **For horizontal systems**, friction becomes the dominant factor rather than gravity.
8. **Pre-geared motors** can simplify your design by reducing the additional gearing needed.

Remember that these calculations represent ideal conditions. In practice, you should:
- Test your system with actual loads
- Measure current draw to ensure motors aren't being overworked
- Make iterative improvements based on real-world performance