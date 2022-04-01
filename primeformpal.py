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

ALL_PRIME_STRINGS = DYADS + TRICHORDS + HEXACHORDS + NONACHORDS + DECACHORDS

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
			print(f"Derivative {prettify_derivative(derivative)}  -- yields sum {sum(derivative[1:])}  <<=== LESS")
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