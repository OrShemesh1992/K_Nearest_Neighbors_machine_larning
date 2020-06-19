from __future__ import print_function
import math
import random
#******Classification function of K Nearest Neighbors*****
def classifyAPoint(base,point,k,p):
    distance=[]
    for group in base:
        for feature in base[group]:
            if p==1 or p==2:
                #  Calculate the distance if p is 1 or 2
                Manhattan_distance =(abs(float(feature[0])-float(point[0]))**float(p) + abs(float(feature[1])-float(point[1]))**float(p))**(1/float(p))
            else:
                #  Calculate the distance if p is inf
                Manhattan_distance =float(max(abs(float(feature[0])-float(point[0])) , abs(float(feature[1])-float(point[1]))))
            # A collection of all the distances calculated
            distance.append((Manhattan_distance,group))
    #Sorting distances from smaller to larger
    #And take the k At the beginning
    distance = sorted(distance)[:k]
    #Count what is more than the other
    over0,over1 = 0,0
    for d in distance:
        if d[1] is 0:
            over0 += 1
        elif d[1] is 1:
            over1 += 1
    return 0 if over0>over1 else 1
#The function takes the data and doing Random
#and divides the array into groups
def randomization(List):
    # random list
    List=random.sample(List,len(List))
    training,testing = List[:len(List)//2],List[len(List)//2:]
    train = {0:[],1:[]}
    # The group for training
    for i in training:
        if i[1] is '1':
            train[0].append((float(i[0]),float(i[2])))
        elif i[1] is '2':
            train[1].append((float(i[0]),float(i[2])))
    test = {0:[],1:[]}
    # The group for testing
    for i in testing:
        if i[1] is '1':
            test[0].append((float(i[0]),float(i[2])))
        elif i[1] is '2':
            test[1].append((float(i[0]),float(i[2])))
    return train,test;

def main():
    f = open("HC_Body_Temperature", "r")
    List = []
    for i in f:
        List.append(i.split())

    P = [1, 2, 'inf']
    EROR_test,EROR_train=0,0
    print("*********k Nearest Neighbors*********")
    # evaluate the k-NN classifier
    for k in range(1, 10, 2): # {1,3,5,7,9}
        print("              k is ",k)
        for p in P:# {1,2,inf}
            EROR_train=0
            EROR_test=0
            for i in range(500):# rounds
                base,test=randomization(List)
                for x in test[0]:
                    # Group 0
                    if classifyAPoint(base,x,k,p) is 1:
                        EROR_test+=1
                for x in test[1]:
                    # Group 1
                    if classifyAPoint(base,x,k,p) is 0:
                        EROR_test+=1
                for x in base[0]:
                    # Group 0
                    if classifyAPoint(base,x,k,p) is 1:
                        EROR_train+=1
                for x in base[1]:
                    # Group 1
                    if classifyAPoint(base,x,k,p) is 0:
                        EROR_train+=1
            print("**********************************************")
            print("Testing eror - p = ",p ," Average: ", float(EROR_test)/65/500)
            print ("Training eror - p = ",p ," Average: ", float(EROR_train)/65/500)
            print("**********************************************")
if __name__ == '__main__':
    main()
