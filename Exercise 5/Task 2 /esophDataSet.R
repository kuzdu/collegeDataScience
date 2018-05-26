summary(esoph) # get summary
str(esoph) #get structure

#some graphics
attach(esoph) #get access for plotting
plot(agegp, ncases, main="Cor. between age and cases", 
     xlab="Age", ylab="Cases", pch=19)
plot(alcgp, ncases, main="Cor. between alcohol and cases", 
     xlab="Alcohol", ylab="Cases", pch=19)
plot(tobgp, ncases, main="Cor. between tabaco and cases", 
     xlab="Tabaco", ylab="Cases", pch=19)
plot(aggregate(ncases, by=list(agegp), FUN=sum)) #age
plot(aggregate(ncases, by=list(tobgp), FUN=sum)) #tabac
plot(aggregate(ncases, by=list(alcgp), FUN=sum)) #alc

#aggregate of numbers
aggregate(ncases, by=list(agegp,tobgp,alcgp), FUN=sum)
aggregate(ncases, by=list(agegp), FUN=sum) #age
aggregate(ncases, by=list(tobgp), FUN=sum) #tabac
aggregate(ncases, by=list(alcgp), FUN=sum) #alc
aggregate(ncontrols, by=list(ncases), FUN=sum)
aggregate(ncases, by=list(alcgp), FUN=sum)
aggregate(ncases, by=list(tobgp), FUN=sum)
aggregate(ncases, by=list(agegp), FUN=sum)