# def climb_stairs(n):
#     if n <= 1:
#         return 1
#     else:
#         return climb_stairs(n-1) + climb_stairs(n-2)

# steps = int(input("Enter Step: "))
# print(f"Number of ways to climb {steps} steps: {climb_stairs(steps)}")



#Best And Fastest Way

def findNumberOfWayToClimbStairs(n,db):
      if db[n] !=0:
           return db[n]
      if n<=3:
            return n
      ans1=findNumberOfWayToClimbStairs(n-1,db)
      db[n-1]=ans1
      ans2=findNumberOfWayToClimbStairs(n-2,db)
      db[n-2]=ans2
      return ans1+ans2

def main():
      n=int(input("Enter Steps: "))
      db=[0 for i in range(n+1)]
      ans = findNumberOfWayToClimbStairs(n,db)
      print("Number of way to climb steps= ",ans)
main()


