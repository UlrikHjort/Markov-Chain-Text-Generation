Program to generate text sequences from Markov chains by the prediction of a future state based on the characteristics of a present state.
A text file is given as input and a Markov chain dictionary is generated. Each word is saved as key with a list of subsequent 
found in the learning text. The same word can exist several times in the list which  will works as the probability 
of the occurrence of the actual word.

Usage: Give a text file as argument:
       python MarkovChainTextGen.py <text file> <sentence length>

Example:
	python MarkovChainTextGen.py text.txt 10