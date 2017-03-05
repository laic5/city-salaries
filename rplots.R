library(ggplot2)

setwd("../../etc/city-salaries")

fnames = c("2009_City.csv","2010_City.csv","2011_City.csv", "2012_City.csv", "2013_City.csv", "2014_City.csv")

dat = read.csv("2015_City.csv", skip = 4)
dat = dat[,c(1,17)]

for(f in fnames) {
  df = read.csv(f, skip = 4, header = T, stringsAsFactors = F)
  ind1 = 1
  ind2 = which(names(df) == "Total.Wages")
  df = df[,c(ind1, ind2)]
  dat = rbind(dat, df)
}

newdat = dat[which(dat$Total.Wages > 13000),]


ggplot(newdat, aes(Total.Wages, fill = as.factor(Year))) + geom_density(alpha = 0.2)
