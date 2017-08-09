complete <- function(directory, id=1:332){
  
  data = data.frame()
  nobs = data.frame()
  completeCases = data.frame()
  
  filenames =list.files(path=directory, full.names = TRUE)
  for(i in id){
    data = read.csv(filenames[i],header = TRUE)
    nobs = sum(complete.cases(data))
    completeCases = rbind(completeCases, data.frame(i,nobs))
  }
  completeCases
}

