from gpiozero import Servo
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

# === GPIO Setup ===
left_servo = Servo(17)
right_servo = Servo(18)

# === Angle Helpers ===
def deg_to_gpiozero(angle_deg):
    """Convert degrees (0-180) to gpiozero value (-1 to 1)."""
    return (angle_deg - 90) / 90.0  # Mapping 90° to 0

def gpiozero_to_deg(value):
    """Convert gpiozero value (-1 to 1) back to degrees (0-180)."""
    return value * 90 + 90

# === Servo + Visualization Combined ===
def set_flap_positions(left_angle_deg, right_angle_deg):
    """Move servo motors to angles, visualize, then reset to center."""
    left_val = deg_to_gpiozero(left_angle_deg)
    right_val = deg_to_gpiozero(right_angle_deg)

    # Move flaps
    left_servo.value = left_val
    right_servo.value = right_val
    sleep(1.5)

    # Visualize flap movement
    visualize_flaps(left_angle_deg, right_angle_deg)

    # Return to center position
    left_servo.value = deg_to_gpiozero(90)
    right_servo.value = deg_to_gpiozero(90)
    sleep(1)

# === Visual Debug Plot ===
def visualize_flaps(left_deg, right_deg):
    """Visualize the orientation of flaps using matplotlib."""
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title(f"Left Flap: {left_deg}°, Right Flap: {right_deg}°")

    # Flap pivots
    left_pivot = (-1, 0)
    right_pivot = (1, 0)
    length = 1.0

    # Convert angles to radians
    left_rad = np.deg2rad(left_deg)
    right_rad = np.deg2rad(right_deg)

    # Flap ends
    left_x = left_pivot[0] + length * np.cos(left_rad)
    left_y = left_pivot[1] + length * np.sin(left_rad)
    right_x = right_pivot[0] + length * np.cos(np.pi - right_rad)
    right_y = right_pivot[1] + length * np.sin(np.pi - right_rad)

    # Draw flaps
    ax.plot([left_pivot[0], left_x], [left_pivot[1], left_y], color='blue', lw=3, label='Left Flap')
    ax.plot([right_pivot[0], right_x], [right_pivot[1], right_y], color='green', lw=3, label='Right Flap')

    # Draw conveyor centerline
    ax.axhline(y=0, color='gray', linestyle='--')
    ax.legend()
    plt.grid()
    plt.show()

# === Sort Logic ===
def sort_object(direction):
    """
    Sorts based on direction:
    1 - Left: Left opens 65°, Right closes 50°
    2 - Center: No motion, both at 90°
    3 - Right: Left closes 130°, Right opens 120°
    """
    if direction == 1:
        print("Sorting to LEFT...")
        set_flap_positions(65, 50)
    elif direction == 3:
        print("Sorting to RIGHT...")
        set_flap_positions(130, 120)
    elif direction == 2:
        print("Staying at CENTER...")
        set_flap_positions(90, 90)
    else:
        print("Invalid direction! Use 1, 2, or 3.")

# === Main Loop ===
if _name_ == "_main_":
    try:
        while True:
            try:
                user_input = input("Enter direction (1=Left, 2=Center, 3=Right, q=Quit): ").strip()
                if user_input.lower() == 'q':
                    break

                direction = int(user_input)
                sort_object(direction)
            except ValueError:
                print("Please enter a valid integer (1, 2, or 3).")
    except KeyboardInterrupt:
        print("\nProgram terminated.")