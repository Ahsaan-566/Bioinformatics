pollutantmean <- function(directory, pollutant, id = 1:332) {
  filenames <- list.files(path = directory, full.names = TRUE)
  df <- data.frame()
  for (i in id) {
    df <- rbind(df,read.csv(filenames[i],header = TRUE))
  }
  round(mean(df[[pollutant]], na.rm = TRUE), digits=3)
  if (pollutant == 'nitrate'){
   mean(df$nitrate, na.rm = TRUE)
  }
  else if (pollutant == 'sulfate') {
   mean(df[[pollutant]], na.rm = TRUE)
  }
  round(ans,digits = 3)
  mean(df$sulfate, na.rm = TRUE)
}
