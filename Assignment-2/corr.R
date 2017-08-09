source("complete.R")

corr = function(directory, threshold = 0){
  completeCases = complete(directory)
  AboveThreshold = completeCases[completeCases$nobs>threshold,1]
  filenames =list.files(path=directory, full.names=TRUE)
  correlations <- rep(NA,length(AboveThreshold))
  
  for (i in AboveThreshold) {
    fileData <- (read.csv(filenames[i]))
    completeCases <- complete.cases(fileData)
    validSulfateData <- fileData[completeCases, 2]
    validNitrateData <- fileData[completeCases, 3]
    correlations[i] <- cor(x = validSulfateData, y = validNitrateData)
  }
  correlations <- correlations[complete.cases(correlations)]
}

cr = corr('specdata',150)
round(head(cr),digits=5)
summary(cr)

