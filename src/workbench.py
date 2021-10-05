from	bond	import	Bond
from	utility	import	lambda_reverse_range

class	WorkBench:
		def	findUpperBoundForYield(bond,	boundForPrice):
				for	v	in	lambda_reverse_range():
						presentValue	=	bond.getPresentValue(v)
						if	(presentValue	>	boundForPrice):
								print	"Bond	Price:	%f"	%	presentValue
								print	"Yield:	%f"	%	v
								break
		findUpperBoundForYield	=	staticmethod(findUpperBoundForYield)
    
		def	getTermStructureFromSpotRates(spotRateCurve):
				print	spotRateCurve.getRates()
				estimate	=	spotRateCurve
				try:
						while(1):
								estimate	=	estimate.estimateNextYear()
								print	estimate.getRates()
				except:
						pass
		getTermStructureFromSpotRates	=	staticmethod(getTermStructureFromSpotRate
