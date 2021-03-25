###
# Utility functions
##

# Always set a seed for repeatable randomness... wait what
set.seed(42)

# Use nick colors if RColorBrewer is loaded
if("RColorBrewer" %in% installed.packages()) {
  library(RColorBrewer)
  brewer   <- brewer.pal(9, "Set1")
  red      <- brewer[1]
  blue     <- brewer[2]
  green    <- brewer[3]
  purple   <- brewer[4]
  orange   <- brewer[5]
  nicegray <- "gray45"
}

# Number formatting
f <- function(x) {formatC(x, format="d", big.mark=',')}
ff <- function(x) {formatC(x, format="f", digits=2, big.mark=',')}
fff <- function(x) {formatC(x, format="f", digits=3, big.mark=',')}
ffff <- function(x) {formatC(x, format="f", digits=4, big.mark=',')}
fz <- function(x) {formatC(x, format="d", big.mark=',', flag=" ")}
ffz <- function(x) {formatC(x, format="f", digits=2, big.mark=',', flag=" ")}
format.pvalue <- function(x, digits=3) {
  threshold <- 1*10^(-1*digits)
  x <- round(x, digits)
  if(x < threshold) {return(paste("p<", threshold, sep=""))}
  else {return(paste("p=", x, sep=""))}
}

# DateTime formatting
format.day.ordinal <- function(x) {
  day <- format(x, format="%d")
  daylast <- substr(day, nchar(day), nchar(day))
  dayfirst <- substr(day, 1, 1)
  if(dayfirst == '0') {day = daylast}
  if(daylast == "1") {day <- paste0(day, "st")}
  else if(daylast == "2") {day <- paste0(day, "nd")}
  else if(daylast == "3") {day <- paste0(day, "rd")}
  else {day <- paste0(day, "th")}
  return(day)
}
format.month <- function(x) {format(x, format='%B %Y')}
format.date <- function(x) {paste(format(x, format='%B'), format.day.ordinal(x), format(x, format='%Y'), sep=' ')}

# Log-odds to Probability, https://sebastiansauer.github.io/convert_logit2prob/
## not always utilized, but just in case...
logit2prob <- function(logit) {
  odds <- exp(logit)
  prob <- odds / (1 + odds)
  return(prob)
}

# LaTeX helpers
bold <- function(x) {paste('{\\textbf{',x,'}}', sep ='')}
gray <- function(x) {paste('{\\textcolor{gray}{', x,'}}', sep ='')}
wrapify <- function(x) {paste("{", x, "}", sep="")}
