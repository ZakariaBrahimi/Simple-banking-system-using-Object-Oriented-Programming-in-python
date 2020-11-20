- Everything in Python actually is Objects
- when we create something in python we really create an object which is an instance of specific class and that class define the way that object interact with other things in programme

- creating new instance ===>> f = dog() ===>> new instance(object)
- Attribute ===>> self.aaaaa = name

----- Object Oriented three pillars:
                                    - Encapsulation = التغليق ===>> using "self" argument
                                    - Inheritance   = الوراثة
                                    - Polymorphisme (many shapes) = leng("zaki), len([0,1,2])


- Constructor :
                - A special type of method
                - It is automatically called when the instance is constructed

- Class Attribute VS Instance Attribute

- An inheriting class :
                        - Child class
                        - Subclass

- An inherited class :
                        - Parent class
                        - Base class
                        - Super class
- Constructor Inheritance(super):
    - Used to relate the class with it's parent class
    - if the class does not have __init__ constructor, python will check its parent class
    - We use super() function to call methods in the parent class

- Multiple Inheritance : ===>> mro() = method resolution order