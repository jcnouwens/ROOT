# ROOT assignment

1. Validate the bill of materials (BOM) based on the validations described below and append appropriate errors on rows if there are any.
2. What should be the optimal way of storing the BOM? 
3. Match [input materials] with the Ecoinvent database references [Column B, C and D]
4. The Ecoinvent database might not have an exact match on material names, for example, material in the BOM might be an abbreviation or the other way around. How do we want to deal with this situation?

# ToDo
1. Check mass for digits, no letters
2. Check quantity and mass for integer or float
3. Check level for integer
4. Check all for duplicate rows
5. Check for any missing values (level, name, quantity, unit, mass)
6. Check for any missing values at suppliers and their locations. BR: Define supplier at the highest level(o) and if not listed there to the next highest level (1) and if not at (1) then to the next highest level (2) etc.

# Done
1. Check units to be: kg, items, m2
2. Check if level 0 (product) is missing
3. Check for the right level sequence. Number X can only be followed by [number X], [number X + 1] or [Number X - 1, Number X-2, Number X-3 etc] Number X can never be followed by [Number X + >1]  Good → 0, 1, 2, 2, 3, 3, 1, 2, 1, 2, 3, 4, 4, 5, 5, 1. Wrong → 0, 1, 2, 2, 1, 3
4. Only match the following values within the BOM: match [Number X] if the previous [number] is the same or higher. Don’t match [Number X] If the previous number is lower. Example: match all the bold numbers → 0, 1, 2, 2, 3, 3, 1, 2, 1, 2, 3, 4, 4, 5, 5, 1.
5. Check the quantity for digits, no letters