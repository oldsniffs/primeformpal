"""
Prime forms in static variables
Derives alternate forms and displays these with their sums for comparison to the prime form's sum
Gives user ability to view info for all primes or to omit all with a sum greater than the prime. Alternatively, the user can input a single prime.

-- Would all derivates that use an 11 yield a higher sum than prime? No primes have an 11
"""

DYADS = [
	"01",
	"02",
	"03",
	"04",
	"05",
	"06"
]

TRICHORDS = [
	"012",
	"013",
	"014",
	"015",
	"016",
	"024",
	"025",
	"026",
	"027",
	"036",
	"037",
	"048",
]

TETRACHORDS = [
	"0123",
	"0124",
	"0125",
	"0126",
	"0127",
	"0134",
	"0135",
	"0136",

	"0137",
	"0145",
	"0146",
	"0147",
	"0148",
	"0156",
	"0157",
	"0158",

	"0167",
	"0235",
	"0236",
	"0237",
	"0246",
	"0247",
	"0248",
	"0257",

	"0258",
	"0268",
	"0347",
	"0358",
	"0369"
]

PENTACHORDS = [
	"01234",
	"01235",
	"01236",
	"01237",
	"01245",
	"01246",
	"01247",
	"01248",

	"01256",
	"01257",
	"01258",
	"01267",
	"01268",
	"01246",
	"01247",
	"01248",

	"01356",
	"01357",
	"01358",
	"01367",
	"01368",
	"01369",
	"01457",
	"01458",

	"01468",
	"01469",
	"01478",
	"01568",

	"02346",
	"02347",
	"02357",
	"02358",

	"02368",
	"02458",
	"02468",
	"02469",
	"02479",
	"03458"
]

HEXACHORDS = [
	"012345",
	"012346",
	"012347",
	"012348",
	"012357",
	"012358",
	"012367",
	"012368",
	"012369",
	"012378",
	"012458",
	"012468",
	"012469",

	"012478",
	"012479",
	"012569",
	"012578",
	"012579",

	"012678",
	"013457",
	"013458",
	"013469",
	"013479",

	"013579",

	"013679",
	"014568",
	"014579",

	"014589",
	"014679",

	"023457",
	"023468",
	"023469",
	"023579",

	"024579",
	"02468T",
]

SEPTACHORDS = [
	"0123456",
	"0123457",
	"0123467",
	"0123567",
	"0123458",
	"0123468",
	"0123568",
	"0124568",

	"0123478",
	"0123578",
	"0124578",
	"0123678",
	"0124678",
	"0123469",
	"0123569",
	"0124569",

	"0123479",
	"0123579",
	"0124579",
	"0123679",
	"0124679",
	"0134679",
	"0145679",
	"0124589",

	"0124689",
	"0134689",
	"0125689",
	"0125679",
	"0234568",
	"0134568",
	"0234579",
	"0234679",

	"0135679",
	"0134579",
	"012468T",
	"013468T",
	"013568T",
	"0134578"
]

OCTACHORDS = [
	"01234567",
	"01234568",
	"01234578",
	"01234678",
	"01235678",
	"01234569",
	"01234579",
	"01234679",

	"01235679",
	"01234589",
	"01234689",
	"01235689",
	"01245689",
	"01234789",
	"01235789",
	"01245789",

	"01236789",
	"02345679",
	"01345679",
	"01245679",
	"0123468T",
	"0123568T",
	"0124568T",
	"0123578T",

	"0124578T",
	"0124678T",
	"01345689",
	"0134578T",
	"0134679T",
]

NONACHORDS = [
	"012345678",
	"012345679",
	"012345689",
	"012345789",
	"012346789",
	"01234568T",
	"01234578T",
	"01234678T",
	"01235678T",
	"01234679T",
	"01235679T",
	"01245689T",
]

DECACHORDS = [
	"0123456789",
	"012345678T",
	"012345679T",
	"012345689T",
	"012345789T",
	"012346789T",
]

ALL_PRIME_STRINGS = DYADS + TRICHORDS + TETRACHORDS + PENTACHORDS + HEXACHORDS + SEPTACHORDS + OCTACHORDS + NONACHORDS + DECACHORDS

# Convert raw prime form strings from textbook to integer list
def _t_check(t):
	if t.upper() == "T":
		return 10
	elif t.upper() == "E":
		return 11
	else:
		try:
			return int(t)
		except ValueError:
			return t

ALL_PRIMES = [[_t_check(t) for t in ps] for ps in ALL_PRIME_STRINGS]


def blank_scale():
	return [False for i in range(12)]

def get_prime_scalemap(prime_form):
	scalemap = blank_scale()
	index = 0
	for step in range(12):
		try:
			if step == prime_form[index]:
				scalemap[step] = True
				index += 1
		except IndexError:
			break
	return scalemap


# Main task functions

def get_derivatives(prime_form):
	# get prime_map
	scalemap = get_prime_scalemap(prime_form)
	derivatives = []

	# collect all derivatives in a list
	# A derivative is: [(starting index of prime list, direction), list of steps]
	for position in prime_form:

		# Clockwise
		# iterate down through 
		# start at position on scalemap. move through scalemap. if true, the distance is added to new sequence		
		derived_sequence = []
		steps = 0
		position_holder = position
		while steps < 12:
			try:
				# print(f"inspecting {scalemap}\nposition {position} + {steps}")
				if scalemap[position_holder+steps] == True:
					derived_sequence.append(steps)
				steps +=1
			except IndexError:
				position_holder -= 12

		
		derivatives.append([(position, "clockwise")]+derived_sequence)

		# Counter
		derived_sequence = []
		steps = 0
		position_holder = position
		while steps < 12:
			try:
				# print(f"inspecting {scalemap}\nposition {position} + {steps}")
				if scalemap[position_holder-steps] == True:
					derived_sequence.append(steps)
				steps +=1
			except IndexError:
				position_holder -= 12

		
		derivatives.append([(position, "countercw")]+derived_sequence)
	return derivatives


def prettify_sequence(sequence):
	# prepares string for display
	pretty_sequence = "("
	for s in sequence:
		if s == 10:
			pretty_sequence += "T"
		elif s == 11:
			pretty_sequence += "E"
		else:
			pretty_sequence += str(s)
	return pretty_sequence + ")"

def prettify_derivative(derivative):
	return (f"from position {derivative[0][0]} going {derivative[0][1]}: {prettify_sequence(derivative[1:])}")

def display_prime(prime_form, less_only):
	# iterate through derivatives, creating a single line display string for each, including its sum and a flag if it is less than the prime's

	print(f"======> Prime Form: {prettify_sequence(prime_form)} {'---> '+str(sum(prime_form))}")   # Aligh "SUMS" at right, sums underneath
	lesser_derivative_found = False
	equal_derivative_found = False
	for derivative in get_derivatives(prime_form):
		if less_only and sum(derivative[1:]) > sum(prime_form):
			continue
		elif sum(derivative[1:]) == sum(prime_form):
			print(f"Derivative {prettify_derivative(derivative)}  -- yields sum {sum(derivative[1:])}  <<=== EQUAL")
			equal_derivative_found = True
		elif sum(derivative[1:]) < sum(prime_form):
			print(f"Derivative {prettify_derivative(derivative)}  -- yields sum {sum(derivative[1:])}  <<=== LESS ==== DING DING LESS")
			lesser_derivative_found = True
		else:
			print(f"Derivative {prettify_derivative(derivative)}  -- yields sum {sum(derivative[1:])}")
	print('\n')


def display_sums(less_only=False):
	print(f"Displaying all primes, sums")
	for prime_form in ALL_PRIMES:
		display_prime(prime_form, less_only)


def start():
	print("Welcome to Prime Form Pal v0.1")
	print("You know why you're here.\n")
	
	while True:
		choice = input('PRESS ENTER to view all prime forms, their derivative sequences, and all of their sums\n-OR- Enter "less" to limit derived sequences displayed to those with sums lesser or equal to their prime\n-OR- Enter a single form to display its derivatives (no spaces, accepts 1-9, T and E) EXAMPLE: 01568\n-OR- Enter "q" to end program\n>')

		# Show everything
		if choice == "":
			display_sums()

		# Show only derivatives with less-than-prime sums
		elif choice == "less":
			display_sums(less_only=True)

		# Show derivatives of a single, user provided prime form
		elif all(type(i) == int and i < 12 for i in [_t_check(t) for t in choice]):
			display_prime([_t_check(t) for t in choice], less_only=False)

		elif choice == "q":
			quit()

if __name__ == "__main__":
	# for p in ALL_PRIMES:
	# 	print(p)
	# 	print(get_prime_scalemap(p))
	start()