#!/usr/bin/Rscript

# Generate longitude and latitude scatter plot
c <- read.csv("lonlats.csv")
jpeg('longitude_latitude.jpg')
plot(c$lon, c$lat, xlab="Longitude", ylab="Latitude", cex=0.1)
text(c$lon, c$lat, labels=c$no, cex=0.8)

# Read data
economy <- read.csv("economy.csv")
mydata <- economy[,3:14]

# Determine the number of clusters
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata, centers=i)$withinss)
jpeg('number_of_clusters.jpg')
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")

# Clustering and plotting
fit <- kmeans(mydata, 4)
jpeg('economy_clusters.jpg')
plot(mydata[,8],mydata[,9],col=fit$cluster,cex=0,xlab="IRSD (Min)",ylab="IRSD (Max)")
text(mydata[,8],mydata[,9],col=fit$cluster,cex=0.6,labels=economy[,16])
jpeg('economy_clusters_country.jpg')
plot(mydata[,8],mydata[,9],col=fit$cluster,cex=0,xlab="IRSD (Min)",ylab="IRSD (Max)")
text(mydata[,8],mydata[,9],col=fit$cluster,cex=0.6,labels=economy[,16])
jpeg('economy_clusters_language.jpg')
plot(mydata[,8],mydata[,9],col=fit$cluster,cex=0,xlab="IRSD (Min)",ylab="IRSD (Max)")
text(mydata[,8],mydata[,9],col=fit$cluster,cex=0.6,labels=economy[,17])

