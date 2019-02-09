def isOverlapping(l1,l2):
	x1 = min(l1);
	x2 = max(l1);
	x3 = min(l2);
	x4 = max(l2);
	
	if x1 == x3:
		return True;
	elif x1 < x3 and x2 <= x3:
		return False;
	elif x1 < x3 and x2 > x3:
		return True;
	elif x3 < x1 and x4 <= x1:
		return False;
	elif x3 < x1 and x4 > x1:
		return True;
	