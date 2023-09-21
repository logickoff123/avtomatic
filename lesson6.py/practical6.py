# tree = {
#  1:{
#     1: {
#          1: 'text',
#          2: 'text',
#          3: 'text',
#      }
#  },
#     1:{
#     1: {
#         1: {
#             1: {
#                 1: {
#                     1: 'folder',
#                     1: 'folder',
#                     1: 'target folder',
#                 },
#                 2: [1,2,3]
#             }
#         }
#     } 
#  }   
# }
# def rec_find (tree:dict,name:str):
#     for key, value in tree.items():
#         if isinstance(value,dict):
#             rec_find(value,name)
#             print(f'ключ -{key},значение {value}')
        
# rec_find (tree, 'target_function')

# class Bird:
#      def __init__(
#          self,
#         wings_lenght: float =12.5,
#         legs_lenght: float = 3.5,
#         color: str = 'red'
#     ):
#          self.wings_lenght = wings_lenght
#          self.legs_lenght = legs_lenght
#          self.color = color
#          print ('Bird Initialaxed')
# def fly(self):
#     print('I fly')
        
# def swim(self):
#     print('I swim')
        
# def walk(self):
#     print('I walk')
        
# def make_noise(self):
#     print('Tweet') 
    
# class Toys:
#     def __init__(
#         self,
#         toxic: bool = False,
#         size_cm3: float = 12.6,
#         color: str = 'purple',
#     ):  
#         def bounce (self):
#             print ('plum')
        
#         def make_noize(self):
#             print ('asasasas')
                
#     bird1 = Bird()
    
# toy1 = Toys()

# toy1.make_noi

########### прктика наша ##################


class MixinSpeak:
    def fly(self):
        print("I am batman")
        
class MixinHit:
    def fly(self):
        print("I am hitting")

class Mixinbultercome:
    def fly(self):
        print("Alfred where is my suit")

class MixinStand:
    def walk(self):
        print("I am stand")

class Mixinlook:
    def swim(self):
        print ("I look at you")

class MixinHead:
    def make_noise(self):
        print ("My head is spinning")
        
class Mixinspeakzagadochnic:
    def speak(self):
        print ("I have riddle for you")
        
class Mixinspeakzagadochnic2:
    def speak(self):
        print ("HAVE A NICA DAY BATMAN")
                   

class Characters:
    def __init__(
        self,
        width_cm: float,
        height_cm: float
    ):
        self.width_cm: float = width_cm
        self.height_cm: float = height_cm
        
class Playable(MixinSpeak, MixinHit, Mixinbultercome):
    pass
        
class Toy(MixinStand, Mixinlook, MixinHead):
    pass
        
        
class Camerman (Characters,Playable):
    width_cm: float = 60
    length_cm: float = 200
    eyes: str = 'one'
    
    def __init__(
        self,
        width_cm: float = 60,
        length_cm: float = 200,
        eyes: str = 'one'
    ):
        self.width_cm: float = width_cm
        self.length: float = length_cm
        self.eyes: float = eyes
        print('Camerman watching')
        
class ToyCamera(Characters, Toy):
    eyes: str = 'camera'
    size_cm3: float = 12
    width_cm: float = 8
    
    def __init__( 
        self,
        eyes: str = 'camera',
        size_cm3: float = 12,
        width_cm: float = 8
    ):
        self.eyes: str = 'camera',
        self.size_cm3: float = size_cm3
        self.width_cm: float = width_cm
        print('ToyCamer')            
        
    
class Batman(Characters, Playable):
    width_cm: float = 90
    length_cm: float = 1.91
    iq: float = 195
    
    def __init__(
        self,
        width_cm: float = 90,
        length_cm: float = 1.91,
        iq: float = 195
    ):
        self.width_cm: float = width_cm
        self.length: float = length_cm
        self.iq: float = iq
        print('Batman come')
            
class ToyBatman(Characters, Toy):
    eyes: str = 'black'
    size_cm3: float = 12
    width_cm: float = 8
    
    def __init__( 
        self,
        eyes: str = 'black',
        size_cm3: float = 12,
        width_cm: float = 8
    ):
        self.eyes: str = 'black',
        self.size_cm3: float = size_cm3
        self.width_cm: float = width_cm
        print('Toy')
          
class Zagadochnic(Characters, Playable,Mixinspeakzagadochnic,Mixinspeakzagadochnic2): 
    width_cm: float = 70
    length_cm: float = 1.85
    iq: float = 200
    
    def __init__(
        self,
        width_cm: float = 70,
        length_cm: float = 1.85,
        iq: float = 20
    ):
        self.width_cm: float = width_cm
        self.length: float = length_cm
        self.iq: float = iq
        print('HHHHHHHH')
    
class  ToyZagadochnic (Characters, Toy):
    eyes: str = 'zagadochnic'
    size_cm3: float = 12
    width_cm: float = 8
    
    def __init__( 
        self,
        eyes: str = 'zagadochnic',
        size_cm3: float = 12,
        width_cm: float = 8
    ):
        self.eyes: str = 'zagadochnic',
        self.size_cm3: float = size_cm3
        self.width_cm: float = width_cm
        print('AYCH')      

    def stand(self):
        print('приступники будут наказаны)')
        
    def head_turn(self):
        print('Поломался')

