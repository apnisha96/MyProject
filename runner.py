runner_scores=list(input("Enter the scores"))

def runneris(scores):
    score = scores[0]
    for i in range(len(scores)-1): 
        if(score < scores[i+1]):
           runner = score
           score = scores[i+1]
        else:
           score = scores[i] 
    return runner

runner_score = runneris(runner_scores)
print runner_score


        
    
