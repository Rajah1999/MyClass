import pickle

filename = 'data.pkl'

def save_file(data, filename):
    file = open(filename, "wb")
    pickle.dump(data, file)
    file.close()

def read_the_file(filename):
    file = open(filename, "rb")
    data = pickle.load(file)
    file.close()
    return data

employee_name = input("Please enter customer name: ")

print("Menu for cleaning \n 1. Mop \n 2. Dishes \n 3. Dusting")
while True:
    try:
        employee_cleaning = input("Please input number: ")
        if employee_cleaning.isnumeric() and 1 <= int(employee_cleaning) <= 3:
            break
        else:
            print("Invalid input. Please enter a numeric value between 1 and 3.")
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

employee_cleans = [employee_name, employee_cleaning]

save_file(employee_cleans, filename)

print(read_the_file(filename))