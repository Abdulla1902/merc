class Car:
    def __init__(self,title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color
    def start_engine(self):
         print(f'engine on {self.title} {self.model} started')
    def stop_engine(self):
        print(f'engine off {self.title} {self.model} stopped')
    def info(self):
        print(f'All_Info {Mercedes.title} {Mercedes.model} {Mercedes.weight} {Mercedes.hp} {Mercedes.nm} {Mercedes.max_speed} {Mercedes.color} \n')
Mercedes = Car('Mercedes', 'w210',2160,220, 7000, 230, 'black' )
Mercedes.start_engine()
Mercedes.stop_engine()
Mercedes.info()