class COLOR: # Text Color
	BLACK  = "\033[30m"
	RED    = "\033[31m"
	GREEN  = "\033[32m"
	YELLOW = "\033[33m"
	BLUE   = "\033[34m"
	PURPLE = "\033[35m"
	CYAN   = "\033[36m"
	WHITE  = "\033[37m"

class BG: # BG Color
	BLACK  = "\033[40m"
	RED    = "\033[41m"
	GREEN  = "\033[42m"
	YELLOW = "\033[43m"
	BLUE   = "\033[44m"
	PURPLE = "\033[45m"
	CYAN   = "\033[46m"
	WHITE  = "\033[47m"

class OTHER:
	# Bold
	B    = "\033[1m"
	BOFF = "\033[22m"
	# Italic
	I = "\033[3m"
	IOFF = "\033[23m"
	# Underline
	U = "\033[4m"
	UOFF = "\033[24m"
	# Reset
	RESET  = "\033[0m"