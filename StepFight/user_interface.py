#user_interface
import httplib2 

#student_id = "42584672" 
#timeInterval = "10" 


#print(resp) # reps is a httplib2 response dictionary
#print(content, '\n')

def prompt_for_ID()->'user_data':
    
    while True:
        ok_to_return = True
        student_id = str(input("Please enter you 8 digit Student ID Number: ")).strip()
        if len(student_id) == 8:
            for s in student_id:
                if s.isdigit() == False: #if every char is a digit, it's ok to return student_id
                    ok_to_return = False
            if ok_to_return == True:
                return student_id
        else:
            print("I'm sorry please try again")

def request_data(student_id, time_interval) ->'content':
    try:
        h = httplib2.Http(".cache")
        requestAdd = "http://128.195.54.59:8004/DataWarehouse/requestData?id=" + student_id + "&timeInterval=" + time_interval
        resp, content = h.request(requestAdd, "GET")
        print(resp)
        
        
        return content
    
    except:
        print('Did not connect, please try again')
        prompt_for_ID()
        

def starting_gold(content):
    starting_gold = 0
    content_len = len(content)
    print(content_len)

    for value in content:
        if value <= 50:
            starting_gold += 15
        elif 50 <= value <= 100:
            starting_gold += 25
        else:
            starting_gold += 50

    if starting_gold <= 10000:
        return (starting_gold, "Low")
    elif 10000 < starting_gold < 20000:
        return (starting_gold, "Medium")
    elif starting_gold >= 20000:
        return (starting_gold, "High")
    


def run():
    
    student_id = prompt_for_ID()
    content = request_data(student_id, "10")
    player_gold_and_description = starting_gold(content)
    print('You can play now!')
    return player_gold_and_description



    
