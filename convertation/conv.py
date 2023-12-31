from PIL import Image
import numpy as np
import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client['picture_mongo']
j = []
for i in db.get_collection('first').find():
    # print(i['picture'])
    t = str(i['picture'])
    p = ''
    for y in t:
        if y != " ":
            p += y
        elif p[-1] != " ":
            p += " "
    tr = np.array(map(int, p[1:-1:].split()))
    print(tr)
    j.append(j)
# img = Image.open('i.jpg')
j = np.asarray(j)
client.close()
t = Image.fromarray(j)
t.show()
# # 2. Convert image to NumPy array
# arr = np.asarray(img)
# # 3. Convert 3D array to 2D list of lists
# lst = []
# for row in arr:
#     tmp = []
#     for col in row:
#         tmp.append(str(col))
#     lst.append(tmp)
# # 4. Save list of lists to CSV
# c = []
# with open('my_file.csv', 'w') as f:
#     for row in lst:
#         f.write(';'.join(row) + '\n')
#
