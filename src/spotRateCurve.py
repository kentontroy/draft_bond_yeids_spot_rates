class SpotRateCurve:
  def __init__(self, spotRates):
    if not len(spotRates) >=1:
      raise Exception("Number of Spot Rates must be >= 2")
    self.spotRates = spotRates

  def getRates(self):
    return self.spotRates

  def calculateForwardRate(self, j):
    if len(self.spotRates)==1:
      raise Exception("Only one	spot rate exists")
    if j <= 1 or j > len(self.spotRates):
      raise Exception("Invalid	j index	parameter")
    j_ = j-1
    numerator =	(1+self.spotRates[j_]/100)**j
    denominator	= 1+self.spotRates[0]/100
    return 100.00 * ((numerator/denominator)**(1/(j-1))	- 1)
		
   def estimateNextYear(self):
     if len(self.spotRates)==1:
       raise Exception("Only one spot rate exists")
     spotRates	= []
     for j in range(2, len(self.spotRates)+1):
	spotRates.append(float("{0:.4f}".format(self.calculateForwardRate(j))))
     return SpotRateCurve(spotRates)
