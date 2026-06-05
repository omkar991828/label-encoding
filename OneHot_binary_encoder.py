

'''OneHot encoder--it is a technique where each category converted into seprate binary column where 1
represent the presence of cotegory and 0 is represence of absent of cotegory and it is work on 2D array'''




from sklearn.preprocessing import OneHotEncoder
fruits=[['grapes']
    ,['banana']
    ,['mango']
    ,['grapes']
    ,['banana']]
oe=OneHotEncoder()
encoded=oe.fit_transform(fruits)
print('original:',fruits)
print('encoded:',encoded)




# this is output above code


# | Fruit  | Banana | Grapes | Mango |
# | ------ | ------ | ------ | ----- |
# | grapes | 0      | 1      | 0     |
# | banana | 1      | 0      | 0     |
# | mango  | 0      | 0      | 1     |
# | grapes | 0      | 1      | 0     |
# | banana | 1      | 0      | 0     |
