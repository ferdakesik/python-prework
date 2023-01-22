
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

#Question-3

a_list=[22,33,445,43]
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list(a_list)

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
    
               