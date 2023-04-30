setwd("E:/Informatique/Démarche Scientifique/Projet")
analyse=read.table("resultats/Gallus.txt",sep="\t",header=FALSE)
plot(analyse[,1], analyse[,2], ylab="Taux GC (%)", xlab="Taille des chromosomes", main = "Taux GC en fonction de la taille des chromosomes")
dev.new(width=10, height=10)
resreg<-lm(analyse[,2]~analyse[,1],data=analyse)
summary(resreg)
summary(analyse[,1])
abline(resreg, col = "red", lwd=2)

# On crée un graphe et on en fait une régression linéaire afin de rechercher la relation entre le taux de GC et la taille des chromosomes
# analyse[,1] correspond à la taille des chromosomes
# analyse[,2] correspond au %GC