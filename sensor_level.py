def calculate_water_height(value):
    return max(0, (value - 4000) / (20000 - 4000) * 10)

def main():
    raw_data = [5963, 4007, 0, 0, 0, 0, 0, 0]  # Replace with actual sensor data
    heights = [calculate_water_height(current) for current in raw_data]

    for i, height in enumerate(heights):
        print(f"Sensor {i + 1}: Water Height = {height:.3f} meters")

if __name__ == "__main__":
    main()
