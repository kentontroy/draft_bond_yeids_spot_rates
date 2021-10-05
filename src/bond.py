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
