

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        bulky_dimension = 10_000
        bulky_volume = 1000000000
        is_bulky_dimension = any([i >= bulky_dimension for i in [length, width, height]])
        is_bulky_volume = (length * width * height) >= bulky_volume

        is_bulky = is_bulky_dimension or is_bulky_volume
        is_heavy = mass >= 100

        if is_bulky and is_heavy:
            return "Both"
        if is_bulky:
            return "Bulky"
        if is_heavy:
            return "Heavy"
        return "Neither"