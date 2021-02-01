
"""DSA_Week3

Author: Adio Roheem & Santigie Sankoh

"""

#initializing constructor
class Simple_array:
  def __init__(self, array=[2,4,6,8,1,4]):
    self.array = array
"""
Space complexity is O(1)
Time complexity is O(1)
"""
#this method print the length of our list
  def length(self):
    print(len(self.array))
"""
Space complexity is O(1)
Time complexity is O(1)
"""
#this method print a specific item in our list
  def get_value(self):
    for n, i in enumerate(self.array):
      if i == 1:
        print(self.array[n])
        """
          Space Compexity: In the script above, the function search an item in a list containing integers. It does this by iterating 
          through the list to check for the specific element. 
          The algorithm has to allocate memory for the the new item and items in the list. And does that nth term.
          Therefore, the space complexity of the algorithm becomes O(n)

          Time complexity of the above is O(n) because of the for loop that increments based on the nth array. 
        """

#this method replace an item with a new item
  def replace(self):
    for n, i in enumerate(self.array):
      if i == 4:
        self.array[n] = 3
        return self.array
  """
    Space Compexity: In the script above, the function replace an item in a list containing integers. It does this by iterating 
    through the list to check for the specific element. 
    The algorithm has to allocate memory for the the new item and items in the list. And does that nth term.
    Therefore, the space complexity of the algorithm becomes O(n)
    
    Time complexity of the above is O(n) because of the for loop that increments based on the nth array. 
    
  """

#this subclass is inherit from our simple class     
class Dynamic_array(Simple_array):
  def __init__(self, array=[2,4,6,8,1,4]):
    super().__init__(array=[2,4,6,8,1,4])

  """
  Space complexity is O(1)
  Time complexity is O(1)
  """
#this method add an item to our list
  def Add_list(self):
    self.array.append(5)
    print(self.array)

  """
  Space complexity is O(1)
  Time complexity is O(1)
  """
 #this method delete an item from our list   
  def del_list(self):
    del self.array[3]
    print(self.array)

"""
Space complexity is O(1)
Time complexity is O(1)
"""
length_array = Dynamic_array()

#this will return tour lenght function
#length_array.length()

#this will return our get value function
#length_array.get_value()

#this will return our replace function
#length_array.replace()

#this will return Add_list function
#length_array.Add_list()

#this will return our del_list function
length_array.del_list()





