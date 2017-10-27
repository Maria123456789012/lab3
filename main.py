import User_Class as usr
import Friends_Class as fr
import matplotlib.pyplot as plt

#params = {'uid': '290864283',
#          'fields': ('first_name', 'last_name')}
#req = requests.get('https://api.vk.com/method/friends.get', params)
# req = requests.get('https://api.vk.com/method/friends.get', params)

params = {'user_ids': 'academeg'}
user = usr.User()
user.set_params(params)
print(user.execute())
print(user.uid)
friends = fr.Friends()
params = {'uid': user.uid,
          'fields': ('bdate')}
friends.set_params(params=params)
print(friends.execute())

arr = [0 for i in range(0, 200)]
for friend in friends.friends_list:
    arr[friend['age']] += 1
print(arr)
plt.hist(arr)
plt.show()
#data = dict(resp.json())
# print(resp.headers)
# print(data)
