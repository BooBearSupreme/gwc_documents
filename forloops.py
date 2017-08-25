#for- keyword to indicate that we are starting a for loop

#hops (or any other variable name) will be the variable in which the changing
#number is stored in

#in- keyword to indicate expecting number range to loop through

#range- function that loops through indicated ranges
#for apples starts from 1
#for apples goes up from 1 to 5 not include 5
#colon, not smicolon
print("apples")
for apples in range(1,5):
    print(apples)
#parameters
print("hops")
for hops in range (6): #range 0-6 not including 6
    print(hops)
#for hops, since no paramteres, assumes we start at 1
#to print repeat a word
print("i")
for i in range(5):
    print("chocolate")

# put in a string so dont have to do mad work

print(cat_post)
print(dog_post)
print(cheetah_post)
print(melon_post)
print(elephant_post)
print(crazy_people_post)
post_name = ["cat_post","dog_post","cheetah_post","melon_post","elephant_post","crazy_people_post"]
for i in range(1,6):
    print(i+post_name[i])

#round 1, var i=1
#round 2, var i=2
#round 3, var i=3
#round 4, var i=4

#print string aplles 5 times
#print value of your round at each iteration (round)
#write a program that prints following
    # 2 4 6 8 10 12 14 16
#write a for loop that prints following
    #3 4 5 6 7 8
#write a for loop that prints
    # 1.banana              six times
