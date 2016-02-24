library(recommenderlab)
data(MovieLense)
d<-MovieLense
es <- evaluationScheme(d, method="cross-validation",train=0.9, goodRating=4,
                       k=4, given=10)



algorithms <- list(
  RANDOM = list(name = "RANDOM", param = NULL),
  POPULAR = list(name = "POPULAR", param = NULL),
  UBCF = list(name = "UBCF", param = NULL),
  IBCF = list(name = "IBCF", param = NULL),

  SVD = list(name = "SVD", param = NULL),

)



ev <- evaluate(es, algorithms)
plot(ev, legend="topright")

plot(ev, "prec", legend="topright")
