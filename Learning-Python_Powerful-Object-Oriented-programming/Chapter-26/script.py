# --- Example: Polymorphism – Employee ---
class Employee:
    def computeSalary(self): ...

class Engineer(Employee):
    def computeSalary(self): ...

huyen = Employee()
ho = Employee()
test = Engineer()


# --- Example: Polymorphism + Composition ---
def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data:
            break
        data = converter(data)
        writer.write(data)
        
class Reader: ...
class FileReader(Reader):
    def read(self): ...

class SocketReader(Reader):
    def read(self): ...

# processor(FileReader(), converter, FileWriter())
# processor(SocketReader(), converter, JsonWriter())



