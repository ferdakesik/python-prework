
# #QUESTION-1

def hello_name(user_name):
    return "hello_"+user_name.upper()
print(hello_name("ferda"))

# #QUESTION-2

def first_odds():
     for odd in range(1,100): 
         if odd %2!=0:
             print(odd)
        
first_odds()

def first_odds2():
    for i in range(1,101,2):
        print(i)

#Question-3

a_list=[22,33,445,43]
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list(a_list)


def max_num_in_list(a_list2):
    my_max=0
    for num in a_list2:
        if num>my_max:
            my_max=num
    return my_max
max_num_in_list([100,99,88,34,22])


#QUESTION-4
a_year=400
def is_leap_year(a_year):
    if a_year %4==0 or a_year %100!=0 and a_year %400==0:
        print(bool(a_year))  
is_leap_year(a_year)


#question-5
def cons(num):
    list=[i for i in range(num)]
    return (list)

print(bool(cons(10)))
    
               