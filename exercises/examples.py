
input_data  = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
numbers = list(map(int, input_data.split()))

print(numbers)


x = [1,2,3]
y = [2,4,6]

plt.plot(x,y)
plt.title('Our first graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,2,3,4])
plt.xticks([0,2,3,4,5,8,10])

plt.show()