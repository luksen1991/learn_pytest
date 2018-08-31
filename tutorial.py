#int
lessun_number=1;

print(lessun_number,type(lessun_number))

#Sting

lesson_name="tutorial"

print(lesson_name,type(lesson_name))

lesson_name2="tutorial2"

print(lesson_name2,type(lesson_name2))

#list

tweet_lengths=[140,80,20,10,'test',"witaj",[1,2,3]]
print (tweet_lengths,type(tweet_lengths))
print (tweet_lengths[2])
tweet_lengths[2]=33
print (tweet_lengths[2])

#tuple
tweet_lengths_immutable=(140,80,20,10,'test',"witaj",[1,2,3])
print (tweet_lengths_immutable,type(tweet_lengths_immutable))
# tweet_lengths_immutable[2]=66
# print (tweet_lengths_immutable[2])

#dictionary

tweets_by_user ={
    'Jack': [1,15],
    'Mary': [2,5]
}

print (tweets_by_user,type(tweets_by_user))
print(tweets_by_user['Jack'])

#if constructions

if False:
    print("Yes")
else:
    print ("NOOOOOO")

#for instructions

for tweet in tweets_by_user:
    print (tweet)

def print_line():
    print("============")

print_line()

def type_print(var):
    print(var,type(var))

type_print(lesson_name)

def custom_print(var,list_var=None,*args,**kwargs):
    print ("START")
    print (var)
    if list_var:
        for element in list_var:
            print (element)
    print ("END")
    print ("args",args)
    print ("kwargs", kwargs)

custom_print(lesson_name,tweet_lengths)
custom_print(1)
custom_print(1,[1,2,3])
custom_print(1,[1,2,3],'arg3','arg4','arg5',args=1,arg6={'luk':'bla'})