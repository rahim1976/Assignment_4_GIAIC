name = input("Write FullName?: ")
years = input("How Long Have You Been Into Tech? Write Number In Words: ")
processor = input("What Processor you currently Rocking?: ")
gpu = input("With GPU?: ")
rams = input("Rams? Write with Model(i.e: DDR4/DDR5): ")
ssd = input("Storage? Write With Form Factor (i.e: HDD/SSD/Nvme): ")
mobo = input("Motherboard? Write Full Name: ")
cooler = input("How You Cool Up Your Hot CPU?: ")
psu = input("Juiced Up By Which PowerSupply?: ")
casing = input("Thats Awesome So In Which Casing These All Items Are Packed In: ")

#Output Text
madlibs = f"Hi there! My name is {name}, and I’ve been a tech enthusiast for the past {years} years. I have a huge interest in gaming and high-performance gaming PCs. Owning a powerful gaming rig is an amazing experience, and mine is packed with some incredible specs.My PC features a {processor} processor paired with an {gpu} GPU. For memory, I have {rams} RAM and a {ssd} SSD. All of this is built on an {mobo} motherboard. To keep things cool, I use a {cooler} cooler. To power everything, I use an {psu} PSU, and it's all housed in the {casing} case."

#Printing Output Text
print(madlibs)