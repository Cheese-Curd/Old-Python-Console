from TEXT import *

def text(text, clr=COLOR.WHITE, bg=False, bgClr=BG.BLACK, bold=False, italic=False, end="\n"):
	print(f"{OTHER.B if bold else ''}{OTHER.I if italic else ''}{bg if bg else ''}{clr}{text}{OTHER.RESET}", end=end, flush=True)
	
def blank(amount):
	amount -= 1
	print("\n"*amount)