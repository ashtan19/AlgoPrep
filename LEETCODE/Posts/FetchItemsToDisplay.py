"""
Leetcode: Amazon OA Fetch Items to Display

Attempts: 1
Completed: Y
Acheived Ideal: Y
Under 30 Mins: N

Time Complexity: O(nlogn)
Space Complexity: O(n)

Pattern: Sorting 
Technique: Use lambda functions to sort the dictionary based on the sort parameter

Problems Encountered:
Other Solutions: Can be done in two lines (see below)

"""


def fetchItemsToDisplay(items, sortParam, sortOrder, itemsPerPage, pageNum):
    sorted_items = []
    is_descending = False if sortOrder == 0 else True

    # Creating sorted item name list based on sort param
    sorted_items = sorted(
        items.items(), key=lambda x: x[sortParam], reverse=is_descending)
    sorted_items = [x[0] for x in sorted_items]
    print(sorted_items)

    # Determine what which items to show
    start_index = pageNum * itemsPerPage
    end_of_page = start_index + itemsPerPage
    # This is when user is accessing a page where there will be no items
    if start_index >= len(sorted_items):
        return []
    else:
        return sorted_items[start_index: end_of_page] if end_of_page < len(sorted_items) else sorted_items[start_index:]


# If Item value is array, test_items = {"item1": [10, 15], "item2": [3, 4], "item3": [17, 8]}
test_items = {"item1": (10, 15), "item2": (3, 4), "item3": (17, 8)}
print(fetchItemsToDisplay(test_items, 0, 0, 3, 1))

# # Creating sorted item name list based on sort param
# if sortParam == 0:
#     sorted_items = sorted(items.keys(), reverse=is_descending)
# else:
#     sorted_items = sorted(
#         items.items(), key=lambda x: x[1][sortParam-1], reverse=is_descending)
#     sorted_items = [x[0] for x in sorted_items]
# print(sorted_items)


def fetchItemsToDisplay(numOfItems, items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    items = sorted(items, key=lambda x: x[sortParameter], reverse=sortOrder)
    return items[itemsPerPage * pageNumber: itemsPerPage * pageNumber + itemsPerPage]
