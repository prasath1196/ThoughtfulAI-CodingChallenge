REJECTED = "REJECTED"
SPECIAL = "SPECIAL"
STANDARD = "STANDARD"
INVALID_INPUT = "INVALID_INPUT"
class PackageSorter:
    def __init__(self):
        pass

    def sort(self, width, height, length, mass):
        if not self._is_valid_input(width, height, length, mass):
            return INVALID_INPUT
        if self._is_bulky(width, height, length) and self._is_heavy(mass):
            return REJECTED
        elif self._is_bulky(width, height, length) or self._is_heavy(mass):
            return SPECIAL
        else:
            return STANDARD


    def _calculate_volume(self, width, height, length):
        return width * height * length

    def _has_bulky_dimmensions(self, width, height, length):
        return any(dimension >= 150 for dimension in [width, height, length])
    
    def _is_bulky(self, width, height, length):
        volume = self._calculate_volume(width, height, length) 
        return volume >=1000000 or self._has_bulky_dimmensions(width, height, length) 

    
    def _is_heavy(self, mass):
        return mass >= 20
    

    def _is_valid_input(self,width, height, length, mass): 
        non_number_input = any(not isinstance(input, (int, float)) for input in [width, height, length, mass])
        if non_number_input:
            return False
        negative_input = any(input < 0 for input in [width, height, length, mass])  
        zero_input = any(input == 0 for input in [width, height, length, mass])
        return not (negative_input or zero_input)