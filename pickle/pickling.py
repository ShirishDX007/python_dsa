import pickle

data = ["Alex", "Marty", "Gorgia", "Private"]
#Serialze the data to store in byte stream
with open('charecters.pkl', 'wb') as f:
    pickle.dump(data,f)
f.close()

#deserialze data to convert byte to objects 
with open('charecters.pkl', 'rb') as f:
    read_data = pickle.load(f)
    print(read_data)
