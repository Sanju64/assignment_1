class Tringles: 
   def tringle(n):
      trow = [1]
      y = [0]
      for x in range(max(n,1)):
          print('' ,trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
      return n>=1
      tringle(10) 

str1 = ["sandsksju", "asjfj","kjbfbas","ajfk","ab"]
res = min(len(ele)for ele in str1 )
for each in str1:
   if len(each)==res:
      print ("length is ",res)
      print("shortest string is : " ,each)
   else:
      pass

 