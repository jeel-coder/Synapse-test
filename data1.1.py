
Kevin=["Halsey","Taylor Swift","Mitski","Joji",
       "Shawn Mendes","Sabrina Carpenter","Nicky Minaj",
       "Conan Gray","One Direction","Justin Bieber"]

Stuart=["Kendrick Lamar","Steve Lacy","Tyler the Creator",
        "Joji","TheWeekend","ColdpLay","Kanye West",
        "Travis Scott","Franck Ocean","Brent Faiyaz"]

Bob=["Conan Gray","Joji","Dove Cameron","Mitski",
     "Arctic Monkeys","Steve Lacy","Kendrick Lamar",
     "Isabel LaRosa","Shawn Mendes","Coldplay","Lauv"]

Edith=["Metallica","Billie Eilish","TheWeekend","Mitski",
       "NF","Conan Gray","Kendrick Lamar","Nicky Minaj",
       "Kanye West","Coldplay"]

l1=len(Kevin)#10
l2=len(Stuart)#10
l3=len(Bob)#11
l4=len(Edith)#10

counter=[]
arr_names=[Kevin,Stuart,Bob,Edith]
arr=["Kevin","Stuart","Bob","Edith"]

for i in range(len(arr_names)):
    for j in range(i + 1, len(arr_names)):
        count = 0
        for artist in arr_names[i]:
            if artist in arr_names[j]:
                count += 1
        counter.append(count)
        print(f"{arr[i]} & {arr[j]} = {count}")

print(counter)#[1, 4, 3, 3, 3, 4]
arr_length=[l1,l2,l3,l4]

sorted_array=[]
index=0
for i in range(len(arr_length)):
    for j in range(i+1,len(arr_length)):
      p=(counter[index]+counter[index])*100/(arr_length[i]+arr_length[j])
      
      sorted_array.append((f"{arr[i]} & {arr[j]} ",p))
      index +=1
 
sorted_array.sort(key=lambda x: x[1], reverse=True)
print(sorted_array)
  
    
    






 
