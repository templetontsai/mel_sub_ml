library(cluster)

population2012 <- read.csv("2012_population.csv")
ppltn12 <- population2012[,3:27]
ppltn12.dist <- dist(ppltn12)
fit <- cmdscale(ppltn12.dist,eig=TRUE,k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x,y,xlab="x", ylab="y", main="population 2012", type="n")
text(x, y, labels = row.names(ppltn12), cex=.7)

diversity <- read.csv("diversity_modified.csv")
dvrsty <- diversity[,c(3,4,5,6,7,8,9,10,11,12,13,14,28,29)]
wts <- c(1,1,1,1,1,1,1,1,1,1,3,1,3,1)
dvrsty.gower <- as.matrix(daisy(dvrsty,metric="gower",weights=wts))
fit <- cmdscale(dvrsty.gower,eig=TRUE,k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x,y,xlab="x", ylab="y", main="diversity", type="n")
text(x, y, labels = row.names(dvrsty), cex=.7)

landuse <- read.csv("land_use.csv")
land <- landuse[,2:12]
land.dist <- dist(land)
fit <- cmdscale(land.dist,eig=TRUE,k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x,y,xlab="x", ylab="y", main="land_use", type="n")
text(x, y, labels = row.names(land), cex=.7)

hospital <- read.csv("hospital_modified.csv")
hsptl <- hospital[,3:19]
wts=c(1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1)
hsptl.gower <- as.matrix(daisy(hsptl,metric="gower",weights=wts))
fit <- cmdscale(hsptl.gower,eig=TRUE,k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x,y,xlab="x", ylab="y", main="hospital", type="n")
text(x, y, labels = row.names(hsptl), cex=.7)

demography <- read.csv("demographic_modified.csv")
demo <- demography[,c(3,4,14,15,16,17,27,28,29,30,31,32,33,34,35,36,41,42,47,48)]
wts <- c(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1)
demo.gower <- as.matrix(daisy(demo,metric="gower",weights=wts))
fit <- cmdscale(demo.gower,eig=TRUE,k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x,y,xlab="x", ylab="y", main="demography", type="n")
text(x, y, labels = row.names(demo), cex=.7)

services <- read.csv("services.csv")
srvcs <- services[,3:26]
srvcs.dist <- dist(srvcs)
fit <- cmdscale(srvcs.dist,eig=TRUE,k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x,y,xlab="x", ylab="y", main="services", type="n")
text(x, y, labels = row.names(srvcs), cex=.7)





