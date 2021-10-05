## Code sketch before implementation
draft - kentontroy, August 2017
```
#!/usr/bin/python
from	__future__	import	division
def lambda_reverse_range(start=1, stop=0, step=-0.00001):
 if (stop>=start or step>=0):
 raise Exception("Invalid parameters. Requirements: Start>=Stop and Step<0")
 i = start
 while i > stop:
 i += step
 yield i
```
```
class	Bond:
		def	__init__(self,	F,	T,	C,	M):
				self.F	=	F
				self.T	=	T
				self.C	=	C
				self.M	=	M
		def	__eq__(self,	another):
				if	type(self)!=type(another):
						return	False
				if	(self.F==another.F	and	self.T==another.T	and	self.C==another.C	and	self.M==another.M):
						return	True
				else:
						return	False
		def	getPresentValue(self,	Y):
				N	=	self.M	*	self.T
				faceValueFlow	=	self.F	/	(1	+	(Y/self.M))**N
				couponFlow	=	(self.C	/	Y)	*	(1	- (1/(1	+	(Y/self.M))**N))
				return	faceValueFlow	+	couponFlow
```
```
class	SpotRateCurve:
		def	__init__(self,	spotRates):
				if	not	len(spotRates)	>=1:
						raise	Exception("Number	of	Spot	Rates	must	be	>=	2")
				self.spotRates	=	spotRates
		def	getRates(self):
				return	self.spotRates
		def	calculateForwardRate(self,	j):
				if	len(self.spotRates)==1:
						raise	Exception("Only	one	spot	rate	exists")
				if	j	<=	1	or	j	>	len(self.spotRates):
						raise	Exception("Invalid	j	index	parameter")
				j_	=	j-1
				numerator	=	(1+self.spotRates[j_]/100)**j
				denominator	=	1+self.spotRates[0]/100
				return	100.00	*	((numerator/denominator)**(1/(j-1))	- 1)
		def	estimateNextYear(self):
				if	len(self.spotRates)==1:
						raise	Exception("Only	one	spot	rate	exists")
				spotRates	=	[]
				for	j	in	range(2,	len(self.spotRates)+1):
						spotRates.append(float("{0:.4f}".format(self.calculateForwardRate(j))))
				return	SpotRateCurve(spotRates
```
```
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
		getTermStructureFromSpotRates	=	staticmethod(getTermStructureFromSpotRates
  ```
```
