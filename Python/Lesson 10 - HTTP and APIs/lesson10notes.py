# Exercise 1
# import requests

# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# print(response.status_code)
# print(response.reason)

# #Exercise 2
# print(response.headers['Content-Type'])
# print(response.elapsed)

# # Exerise 3
# try:
#     print(response.json()['userId'])
#     print(response.json()['id'])
#     print(response.json()['title'])

# except:
#     pass


# Exercise 2 
import requests

username = 'student'
passwd = 'pass123'
response = requests.get('https://httpbin.org/basic-auth/student/pass123', auth=('student', 'pass123'))

print(response.status_code)

headers = {
    "Authorization": f"Bearer abc123"
    "X-API-Key: demo-key-001"
}
response = requests.get('https://httpbin.org/bearer', headers=headers)

print(response)

response3 = requests.get('https://httpbin.org/get', headers=headers)

print(response3.json())