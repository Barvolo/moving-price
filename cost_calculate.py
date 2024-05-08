
from price_list import get_price_sum_for_items
from distance import get_osrm_distance

def calculate_moving_cost(items, distance):
    base_cost = 50  # Basic starting fee for the moving service
    cost_per_km = 0.5  # Cost per kilometer
    item_cost = get_price_sum_for_items(items)

    total_cost = base_cost + (distance * cost_per_km) + item_cost
    return total_cost

# Example usage
items_to_move = ['ספה תלת', 'ארון 2 דלתות', 'ארגז', 'ארגז', 'ארגז', 'ארגז', 'ארגז', 'ארגז', 'ארגז', 'ארגז', 'ארגז', 'ארגז', 'טלויזיה 50- 60 אינצ', 'מזנון רגיל', 'כורסא יחיד', 'שולחן משרדי', 'מזרן זוגי', 'בסיס מיטה רגיל']
source = '34.780527,32.0853'  # Example: Rabin Square
destination = '34.769142,32.074177'  # Example: HaTikva Market

distance_km = get_osrm_distance(source, destination)
if distance_km is not None:
    print(f"Driving distance: {distance_km:.2f} km")
else:
    print("Failed to calculate distance.")

estimated_cost = calculate_moving_cost(items_to_move, 1.2)
print(f"The estimated moving cost is: ₪ {estimated_cost}")