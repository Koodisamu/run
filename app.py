def pace_to_times(pace, distances):
    """
    Calculate times for various distances given a pace.

    Parameters:
    pace (str): Pace in the format 'MM:SS'
    distances (list of float): List of distances in kilometers

    Returns:
    dict: A dictionary where keys are distances and values are the
          corresponding times in 'MM:SS' format.
    """
    minutes, seconds = map(int, pace.split(':'))
    total_pace_seconds = minutes * 60 + seconds
    results = {}
    for dist in distances:
        total_time_seconds = total_pace_seconds * dist
        time_minutes = int(total_time_seconds // 60)
        time_seconds = int(total_time_seconds % 60)
        results[f"{dist}km"] = f"{time_minutes}:{time_seconds:02d}"
    return results

def time_to_paces(time, distances):
    """
    Calculate paces for various distances given a total time.

    Parameters:
    time (str): Time in the format 'MM:SS'
    distances (list of float): List of distances in kilometers

    Returns:
    dict: A dictionary where keys are distances and values are the
          corresponding paces in 'MM:SS' format.
    """
    minutes, seconds = map(int, time.split(':'))
    total_time_seconds = minutes * 60 + seconds
    results = {}
    for dist in distances:
        if dist > 0:
            pace_seconds_per_kilometer = total_time_seconds / dist
            pace_minutes = int(pace_seconds_per_kilometer // 60)
            pace_seconds = int(pace_seconds_per_kilometer % 60)
            results[f"{dist}km"] = f"{pace_minutes}:{pace_seconds:02d}"
        else:
            results[f"{dist}km"] = "N/A (distance is zero)"
    return results

def distance_to_paces(distance, times):
    """
    Calculate paces for a given distance and various times.

    Parameters:
    distance (float): Distance in kilometers
    times (list of str): List of times in the format 'MM:SS'

    Returns:
    dict: A dictionary where keys are times and values are the
          corresponding paces in 'MM:SS' format.
    """
    results = {}
    for t in times:
        time_minutes, time_seconds = map(int, t.split(':'))
        total_time_seconds = time_minutes * 60 + time_seconds
        if distance > 0:
            pace_seconds_per_kilometer = total_time_seconds / distance
            pace_minutes = int(pace_seconds_per_kilometer // 60)
            pace_seconds = int(pace_seconds_per_kilometer % 60)
            results[t] = f"{pace_minutes}:{pace_seconds:02d}"
        else:
            results[t] = "N/A (distance is zero)"
    return results

def distance_to_times(distance, paces):
    """
    Calculate times for a given distance and various paces.

    Parameters:
    distance (float): Distance in kilometers
    paces (list of str): List of paces in the format 'MM:SS'

    Returns:
    dict: A dictionary where keys are paces and values are the
          corresponding times in 'MM:SS' format.
    """
    results = {}
    for p in paces:
        pace_minutes, pace_seconds = map(int, p.split(':'))
        total_pace_seconds = pace_minutes * 60 + pace_seconds
        total_time_seconds = total_pace_seconds * distance
        time_minutes = int(total_time_seconds // 60)
        time_seconds = int(total_time_seconds % 60)
        results[p] = f"{time_minutes}:{time_seconds:02d}"
    return results

def main():
    inpt = input("Enter the type of calculation (pace, time, distance): ").strip().lower()
    common_distances_km = [0.1, 0.2, 0.3, 0.4, 0.8, 1.0, 3.0, 5.0, 10.0, 15.0, 20.0, 21.0975] # Distances in km
    common_distances_m = [100/1000, 200/1000, 300/1000, 400/1000, 800/1000, 1000/1000, 3000/1000, 5000/1000, 10000/1000, 15000/1000, 20000/1000, 21097.5/1000] # Distances in km
    distance_labels_km = ["100m", "200m", "300m","400m", "800m", "1k", "3k", "5k", "10k", "15k", "20k", "Half Marathon"]

    if inpt == "pace":
        pace_input = input("Enter pace (MM:SS): ")
        results = pace_to_times(pace_input, common_distances_m)
        print(f"\nTimes for a pace of {pace_input}:")
        for i, dist_label in enumerate(distance_labels_km):
            print(f"{dist_label}: {results[f'{common_distances_m[i]}km']}")

    elif inpt == "time":
        time_input = input("Enter time (MM:SS): ")
        results = time_to_paces(time_input, common_distances_m)
        print(f"\nPaces for a time of {time_input}:")
        for i, dist_label in enumerate(distance_labels_km):
            print(f"{dist_label}: {results[f'{common_distances_m[i]}km']}")

    elif inpt == "distance":
        calc_type = input("Calculate for (time/pace)? ").strip().lower()
        distance_input = float(input("Enter distance (km): "))
        if calc_type == "time":
            paces_input = input("Enter paces (comma-separated, MM:SS): ").split(',')
            paces_input = [p.strip() for p in paces_input]
            results = distance_to_times(distance_input, paces_input)
            print(f"\nTimes for a distance of {distance_input}km:")
            for pace, time_result in results.items():
                print(f"Pace {pace}: {time_result}")
        elif calc_type == "pace":
            times_input = input("Enter times (comma-separated, MM:SS): ").split(',')
            times_input = [t.strip() for t in times_input]
            results = distance_to_paces(distance_input, times_input)
            print(f"\nPaces for a distance of {distance_input}km:")
            for time_input, pace_result in results.items():
                print(f"Time {time_input}: {pace_result}")
        else:
            print("Invalid calculation type for distance.")

    else:
        print("Invalid calculation type.")

if __name__ == "__main__":
    main()