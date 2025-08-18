def calculate_power_bill(units_consumed, rate_type="standard"):
    """
    Calculate power bill based on units consumed and rate type
    
    Args:
        units_consumed (float): Number of units (kWh) consumed
        rate_type (str): Type of rate structure ("standard", "tiered", "time_of_day")
    
    Returns:
        dict: Bill details including breakdown and total
    """
    
    if rate_type == "standard":
        return calculate_standard_rate(units_consumed)
    elif rate_type == "tiered":
        return calculate_tiered_rate(units_consumed)
    elif rate_type == "time_of_day":
        return calculate_time_of_day_rate(units_consumed)
    else:
        return {"error": "Invalid rate type specified"}

def calculate_standard_rate(units):
    """Standard flat rate calculation"""
    rate_per_unit = 8.50  # Rs per kWh
    base_charge = 100     # Fixed monthly charge
    
    energy_charge = units * rate_per_unit
    total = base_charge + energy_charge
    
    return {
        "rate_type": "Standard Rate",
        "units_consumed": units,
        "rate_per_unit": rate_per_unit,
        "energy_charge": energy_charge,
        "base_charge": base_charge,
        "total_bill": total
    }

def calculate_tiered_rate(units):
    """Tiered rate calculation with different rates for usage levels"""
    base_charge = 100
    
    # Tier structure: (upper_limit, rate_per_unit)
    tiers = [
        (100, 6.50),   # First 100 units: Rs 6.50 per unit
        (200, 8.00),   # 101-200 units: Rs 8.00 per unit
        (300, 9.50),   # 201-300 units: Rs 9.50 per unit
        (float('inf'), 11.00)  # Above 300 units: Rs 11.00 per unit
    ]
    
    energy_charge = 0
    remaining_units = units
    tier_breakdown = []
    
    for i, (upper_limit, rate) in enumerate(tiers):
        if remaining_units <= 0:
            break
            
        if i == 0:
            # First tier
            tier_units = min(remaining_units, upper_limit)
            tier_charge = tier_units * rate
            tier_breakdown.append({
                "tier": f"1-{upper_limit}",
                "units": tier_units,
                "rate": rate,
                "charge": tier_charge
            })
            energy_charge += tier_charge
            remaining_units -= tier_units
        else:
            # Subsequent tiers
            prev_limit = tiers[i-1][0]
            tier_units = min(remaining_units, upper_limit - prev_limit)
            if tier_units > 0:
                tier_charge = tier_units * rate
                tier_breakdown.append({
                    "tier": f"{prev_limit+1}-{upper_limit}",
                    "units": tier_units,
                    "rate": rate,
                    "charge": tier_charge
                })
                energy_charge += tier_charge
                remaining_units -= tier_units
    
    total = base_charge + energy_charge
    
    return {
        "rate_type": "Tiered Rate",
        "units_consumed": units,
        "tier_breakdown": tier_breakdown,
        "energy_charge": energy_charge,
        "base_charge": base_charge,
        "total_bill": total
    }

def calculate_time_of_day_rate(units):
    """Time of day rate calculation with peak/off-peak rates"""
    base_charge = 100
    
    # Assume 60% peak hours, 40% off-peak hours
    peak_units = units * 0.6
    off_peak_units = units * 0.4
    
    peak_rate = 10.50      # Rs per kWh during peak hours
    off_peak_rate = 6.00   # Rs per kWh during off-peak hours
    
    peak_charge = peak_units * peak_rate
    off_peak_charge = off_peak_units * off_peak_rate
    energy_charge = peak_charge + off_peak_charge
    
    total = base_charge + energy_charge
    
    return {
        "rate_type": "Time of Day Rate",
        "units_consumed": units,
        "peak_units": peak_units,
        "peak_rate": peak_rate,
        "peak_charge": peak_charge,
        "off_peak_units": off_peak_units,
        "off_peak_rate": off_peak_rate,
        "off_peak_charge": off_peak_charge,
        "energy_charge": energy_charge,
        "base_charge": base_charge,
        "total_bill": total
    }

def display_bill(bill_details):
    """Display the power bill in a formatted way"""
    print("=" * 60)
    print(f"           POWER BILL CALCULATOR")
    print("=" * 60)
    print(f"Rate Type: {bill_details['rate_type']}")
    print(f"Units Consumed: {bill_details['units_consumed']:.2f} kWh")
    print("-" * 60)
    
    if bill_details['rate_type'] == "Standard Rate":
        print(f"Rate per Unit: Rs {bill_details['rate_per_unit']:.2f}")
        print(f"Energy Charge: Rs {bill_details['energy_charge']:.2f}")
        
    elif bill_details['rate_type'] == "Tiered Rate":
        print("Tier Breakdown:")
        for tier in bill_details['tier_breakdown']:
            print(f"  {tier['tier']} units: {tier['units']:.2f} × Rs {tier['rate']:.2f} = Rs {tier['charge']:.2f}")
        print(f"Total Energy Charge: Rs {bill_details['energy_charge']:.2f}")
        
    elif bill_details['rate_type'] == "Time of Day Rate":
        print(f"Peak Hours ({bill_details['peak_units']:.2f} units): Rs {bill_details['peak_charge']:.2f}")
        print(f"Off-Peak Hours ({bill_details['off_peak_units']:.2f} units): Rs {bill_details['off_peak_charge']:.2f}")
        print(f"Total Energy Charge: Rs {bill_details['energy_charge']:.2f}")
    
    print("-" * 60)
    print(f"Base Charge: Rs {bill_details['base_charge']:.2f}")
    print(f"TOTAL BILL: Rs {bill_details['total_bill']:.2f}")
    print("=" * 60)

def main():
    print("=== POWER BILL CALCULATOR ===\n")
    
    while True:
        print("\nChoose rate structure:")
        print("1. Standard Rate (Flat rate)")
        print("2. Tiered Rate (Different rates for usage levels)")
        print("3. Time of Day Rate (Peak/Off-peak)")
        print("4. Compare all rates")
        print("5. Exit")
        
        try:
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '5':
                print("Thank you for using Power Bill Calculator!")
                break
                
            if choice in ['1', '2', '3']:
                units = float(input("Enter units consumed (kWh): "))
                
                if choice == '1':
                    rate_type = "standard"
                elif choice == '2':
                    rate_type = "tiered"
                else:
                    rate_type = "time_of_day"
                
                bill = calculate_power_bill(units, rate_type)
                display_bill(bill)
                
            elif choice == '4':
                units = float(input("Enter units consumed (kWh): "))
                print(f"\nComparing all rate structures for {units} units:")
                
                standard_bill = calculate_power_bill(units, "standard")
                tiered_bill = calculate_power_bill(units, "tiered")
                time_bill = calculate_power_bill(units, "time_of_day")
                
                print(f"\nStandard Rate: Rs {standard_bill['total_bill']:.2f}")
                print(f"Tiered Rate:  Rs {tiered_bill['total_bill']:.2f}")
                print(f"Time of Day:  Rs {time_bill['total_bill']:.2f}")
                
                # Find cheapest option
                bills = [standard_bill, tiered_bill, time_bill]
                cheapest = min(bills, key=lambda x: x['total_bill'])
                print(f"\nCheapest option: {cheapest['rate_type']} at Rs {cheapest['total_bill']:.2f}")
                
            else:
                print("Invalid choice! Please select 1-5.")
                
        except ValueError:
            print("Error: Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()
