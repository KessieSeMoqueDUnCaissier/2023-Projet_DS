setwd("E:/Informatique/Démarche Scientifique/Projet")
analyse=read.table("resultats/borrelia_fg.txt",sep="\t",header=TRUE)
plot(analyse[,2], analyse[,1], ylab="Taux GC (%)", xlab="Position", main = "OriC chez Borrelia Burgodoferi", type="l", lwd=1, xlim = c(0,910000))
dev.new(width=15, height=15)
summary(analyse[,1])
which.max(analyse[,1])
t.test(analyse[,2]<=440000,analyse[analyse[,2]>440000])

# On dresse ici un graphique nous permettant de trouver OriC chez la bactérie