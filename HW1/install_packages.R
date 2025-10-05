packages <- c("readxl", "dplyr", "ggplot2")

installed <- packages %in% rownames(installed.packages())

if(any(!installed)) {
  install.packages(packages[!installed])
}