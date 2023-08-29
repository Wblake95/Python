library("random")

rank1 <- list()
rank2 <- list()
rank3 <- list()
rank4 <- list()
rank5 <- list()

vector1 <- list(randomNumbers(n=10,col=1))
increment <- max(unlist(vector1))/5

for (i in 1:length(vector1)) {
	     if (vector1[i] < increment) {
		     rank1 <- append(rank1, vector1[i])
	     }
	     else if (increment < vector1[i] & vector1[i] < increment*2) {
		     rank2 <- append(rank2, vector1[i])
	     }
	     else if (increment*2 < vector1[i] & vector1[i] < increment*3) {
		     rank3 <- append(rank3, vector1[i])
	     }
	     else if (increment*3 < vector1[i] & vector1[i] < increment*4) {
		     rank4 <- append(rank4, vector1[i])
	     }
	     else {
		     rank5 <- append(rank5, vector1[i])
	     }
}

print(vector1)
print(rank1)
print(rank2)
print(rank3)
print(rank4)
print(rank5)
