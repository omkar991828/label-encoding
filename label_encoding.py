# from sklearn.preprocessing import LabelEncoder
#
# colors = ['Red', 'Blue', 'Green', 'Red', 'Blue']
#
# le = LabelEncoder()
#
# encoded = le.fit_transform(colors)
#
# print("Original:", colors)
# print("Encoded :", encoded)




from sklearn.preprocessing import LabelEncoder
car=['laborgini','maruti','suzuki','toyota','tavera','rohan','aman','aman','anil','ananya']
le=LabelEncoder()
encoded=le.fit_transform(car)
print('original:',car)
print('encoded',encoded)


