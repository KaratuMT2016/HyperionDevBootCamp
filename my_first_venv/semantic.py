"""
● Start
● Create a file called semantic.py
● Write all the code below:
    ● Import spacy
    ● load the preferred langauge model
    ● Parse the tokens or strings to train
    ● Create a nested for loop that will traverse tokens
    ● Print the tokens to compare the text and print the similarity score for each comparison
● End
● Write a note on what is noticed to be different from the two langauge models (en_core_web_sm and en_core_web_md)
"""

import spacy

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana game console mario minecraft roblox')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))



"""
en_core_web_sm                                                                                                                    | en_core_web_md
----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------
● It was uanble to compare cat and cat                                                                                            | ● It was able to compare cat and cat
● It seems this has less trained dataset                                                                                          | ● While this has a larger trained dataset
● The similarity score between monkey and banana is 0.36                                                                          | ● The similarity score between monkey and banana is 0.40. This suggest that with a bigger training set, the accuracy of the similarity is higher.
● The similarity score between cat and apple is strangely high (0.70), which is kind of inaccurate                                | ● However, the similarity is very low (0.20), which shows that with medium a more meaningful and accurate similarity score is achieved.
● The similarity score between minecraft and roblox is 0.34                                                                       | ● Here we have an amazing similarity score of 1.0. This is remarkable as both mincraft and roblox are games.
● The similarity score between cat and mario has a good score of 0.61 which is misleading. This is true for apple and mario (0.76)| ● This language model has a similarity score of -0.06, which goes to say there is no similarity at all between mario and cat, and apple and mario (-0.13).


● In summary the "en_core_web_sm" language model is less accurate when compared with "en_core_web_md" langauge model, but the "en_core_web_sm" language model is faster.
● The choice of which language model to use depends on what the priorities are.
"""