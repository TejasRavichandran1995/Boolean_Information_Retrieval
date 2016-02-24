library(recommenderlab)
data(MovieLense)
d<-MovieLense
es <- evaluationScheme(d, method="cross-validation", goodRating=4,
                       k=4, given=10)



algorithms <- list(
  RANDOM = list(name = "RANDOM", param = NULL),
  POPULAR = list(name = "POPULAR", param = NULL),
  UBCF = list(name = "UBCF", param = list ( method="cosine",nn =50,minRating=3)),
  IBCF = list(name = "IBCF", param = NULL),

  SVD = list(name = "SVD", param = NULL),

)



evlist <- evaluate(es, algorithms)
plot(evlist, legend="topright")

plot(evlist, "prec", legend="topright")
