library(recommenderlab)
library(reshape2)
data(MovieLense)
d <- MovieLense
evaluateModels <- function(movieRatingMat)
{
  
  
  recommenderRegistry$get_entries(dataType = "realRatingMatrix")
  
  scheme <- evaluationScheme(movieRatingMat, method = "split", train = .9,
                             k = 1, given = 10, goodRating = 4)
  
  algorithms <- list(
    RANDOM = list(name="RANDOM", param=NULL),
    POPULAR = list(name="POPULAR", param=NULL),
    UBCF = list(name="UBCF", param= list ( method="cosine" , nn=50)),
    SVD = list(name="SVD",param=list(treat_na="0")),
   # PCA= list(name="PCA",param=NULL),
    IBCF = list(name="IBCF",param=NULL)
  )
  
  
  results <- evaluate(scheme, algorithms, n=c(1, 3, 5, 10, 15, 20))
  
  
  
  return (results)
}


visualise <- function(results)
{
  
  plot(results, annotate = 1:3, legend="topright")
  
  
  plot(results, "prec/rec", annotate=3, legend="topright", xlim=c(0,.22))
}


createModel <-function (movieRatingMat,method){
  
  model <- Recommender(movieRatingMat, method = method)
  names(getModel(model))
  getModel(model)$method
  
  getModel(model)$nn
  
  return (model)
}


recommendations <- function(movieRatingMat, model, userID, n)
{
  
  
  topN_recommendList <-predict(model,movieRatingMat[userID],n)
  as(topN_recommendList,"list")
}

evalList <- evaluateModels(d)



visualise(evalList)


rec_model <- createModel(d, "UBCF")
userID <- 1
topN <- 20
recommendations(d, rec_model, userID, topN)

