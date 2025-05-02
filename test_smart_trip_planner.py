import pytest
#pytest will test all possible and not possible outcomes of the program
from smart_trip_planner import suggest_checklist_items

def test_suggest_checklist_items():

    # Test Case 1: Hiking in cold weather (< 40F)
    trip1 = "Hiking"
    temp1 = 35
    suggestions1 = suggest_checklist_items(trip1, temp1)
    # Basic checks
    assert isinstance(suggestions1, list) # Should return a list
    assert "Water Bottle" in suggestions1 # Basic item check
    # Trip-specific checks
    assert "Hiking Boots" in suggestions1import pytest
from smart_trip_planner import suggest_checklist_items

def test_suggest_checklist_items():

    trip1 = "Hiking"
    temp1 = 35
    suggestions1 = suggest_checklist_items(trip1, temp1)
    assert isinstance(suggestions1, list)
    assert "Water Bottle" in suggestions1
    assert "Hiking Boots" in suggestions1
    assert "Backpack" in suggestions1
    assert "Warm Hat" in suggestions1
    assert "Gloves" in suggestions1
    assert "Insulated Jacket" in suggestions1
    assert "Sun Hat" not in suggestions1
    assert "Light Jacket" not in suggestions1

    trip2 = "Jeep"
    temp2 = 85
    suggestions2 = suggest_checklist_items(trip2, temp2)
    assert "Snacks" in suggestions2
    assert "Recovery Strap" in suggestions2
    assert "Air Compressor" in suggestions2
    assert "Sun Hat" in suggestions2
    assert "Sunscreen" in suggestions2
    assert "Extra Water" in suggestions2
    assert "Sunglasses" in suggestions2
    assert "Warm Hat" not in suggestions2
    assert "Insulated Jacket" not in suggestions2

    trip3 = "Camping"
    temp3 = 55
    suggestions3 = suggest_checklist_items(trip3, temp3)
    assert "First-Aid Kit" in suggestions3
    assert "Tent" in suggestions3
    assert "Sleeping Bag" in suggestions3
    assert "Light Jacket" in suggestions3
    assert "Long Sleeves" in suggestions3
    assert "Warm Hat" not in suggestions3
    assert "Sun Hat" not in suggestions3
    assert "Sunglasses" not in suggestions3

    trip4 = "Fishing"
    temp4 = 75
    suggestions4 = suggest_checklist_items(trip4, temp4)
    assert "Fishing Rod/Reel" in suggestions4
    assert "Cooler" in suggestions4
    assert "Sunglasses" in suggestions4
    assert "Light Jacket" not in suggestions4

    trip5 = "Kayaking"
    temp5 = 65
    suggestions5 = suggest_checklist_items(trip5, temp5)
    assert "Water Bottle" in suggestions5
    assert "Phone" in suggestions5
    assert "Hiking Boots" not in suggestions5
    assert "Tent" not in suggestions5
    assert "Warm Hat" not in suggestions5
    assert "Light Jacket" not in suggestions5
    assert "Sun Hat" not in suggestions5
    assert "Sunglasses" not in suggestions5
    assert "Backpack" in suggestions1
    # Temperature-specific checks
    assert "Warm Hat" in suggestions1
    assert "Gloves" in suggestions1
    assert "Insulated Jacket" in suggestions1
    # Check for items that shouldn't be there
    assert "Sun Hat" not in suggestions1
    assert "Light Jacket" not in suggestions1


    # Test Case 2: Jeep trip in very hot weather (> 80F)
    trip2 = "Jeep"
    temp2 = 85
    suggestions2 = suggest_checklist_items(trip2, temp2)
    # Basic checks
    assert "Snacks" in suggestions2
    # Trip-specific checks
    assert "Recovery Strap" in suggestions2
    assert "Air Compressor" in suggestions2
    # Temperature-specific checks
    assert "Sun Hat" in suggestions2
    assert "Sunscreen" in suggestions2
    assert "Extra Water" in suggestions2
    assert "Sunglasses" in suggestions2
    # Check for items that shouldn't be there
    assert "Warm Hat" not in suggestions2
    assert "Insulated Jacket" not in suggestions2


    # Test Case 3: Camping in moderate/cool weather (e.g., 55F)
    trip3 = "Camping"
    temp3 = 55
    suggestions3 = suggest_checklist_items(trip3, temp3)
    # Basic checks
    assert "First-Aid Kit" in suggestions3
    # Trip-specific checks
    assert "Tent" in suggestions3
    assert "Sleeping Bag" in suggestions3
    # Temperature-specific checks (should get cool weather gear)
    assert "Light Jacket" in suggestions3
    assert "Long Sleeves" in suggestions3
    # Check for items that shouldn't be there
    assert "Warm Hat" not in suggestions3 # Too warm
    assert "Sun Hat" not in suggestions3 # Too cool
    assert "Sunglasses" not in suggestions3 # Not triggered by 55F


    # Test Case 4: Fishing in warm weather (e.g., 75F)
    trip4 = "Fishing"
    temp4 = 75
    suggestions4 = suggest_checklist_items(trip4, temp4)
    # Trip-specific check
    assert "Fishing Rod/Reel" in suggestions4
    assert "Cooler" in suggestions4
    # Temperature-specific check (should get sunglasses)
    assert "Sunglasses" in suggestions4
    assert "Light Jacket" not in suggestions4 # Too warm


    # Test Case 5: Unknown trip type in neutral temp (e.g., 65F)
    trip5 = "Kayaking" # Not explicitly handled in function
    temp5 = 65
    suggestions5 = suggest_checklist_items(trip5, temp5)
    # Should still get basic items
    assert "Water Bottle" in suggestions5
    assert "Phone" in suggestions5
    # Should not get trip-specific items for Hiking/Jeep/Camping/Fishing
    assert "Hiking Boots" not in suggestions5
    assert "Tent" not in suggestions5
    # Should not get specific temp items for hot/cold/cool
    assert "Warm Hat" not in suggestions5
    assert "Light Jacket" not in suggestions5
    assert "Sun Hat" not in suggestions5
    # Might get sunglasses if temp > 70, but 65 shouldn't trigger it
    assert "Sunglasses" not in suggestions5