class Patient:
    def init(self, pid="", name="", disease="", gender="", age=""):
        self.id = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def str(self):
        return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"


class PatientManager:
    def init(self):
        self.patients = []
        self.read_file()

    def read_file(self):
        try:
            with open("patients.txt") as f:
                next(f)
                for line in f:
                    parts = line.strip().split("_")
                    if len(parts) == 5:
                        self.patients.append(Patient(*parts))
        except:
            pass

    def write_file(self):
        with open("patients.txt", "w") as f:
            f.write("id_Name_Disease_Gender_Age\n")
            for p in self.patients:
                f.write(str(p) + "\n")

    def display_list(self):
        print("ID   Name                   Disease         Gender          Age\n")
        for p in self.patients:
            print(f"{p.id:<5} {p.name:<22} {p.disease:<15} {p.gender:<15} {p.age:<5}\n")

    def display_by_id(self):
        pid = input("\nEnter the Patient Id: ")
        found = False
        for p in self.patients:
            if p.id == pid:
                print("\nID   Name\t\t    Disease\t    Gender\t    Age\n")
                print(f"{p.id:<5} {p.name:<22} {p.disease:<15} {p.gender:<15} {p.age:<5}\n")
                found = True
                break
        if not found:
            print("Can't find the Patient with the same id on the system\n")

    def add(self):
        p = Patient(
            input("Enter Patient id: "),
            input("Enter Patient name: "),
            input("Enter Patient disease: "),
            input("Enter Patient gender: "),
            input("Enter Patient age: ")
        )
        self.patients.append(p)
        with open("patients.txt", "a") as f:
            f.write(str(p) + "\n")
        print(f"\nPatient whose ID is {p.id} has been added.\n")

    def edit(self):
        id = input("\nPlease enter the id of the Patient that you want to edit their information: ")
        for p in self.patients:
            if p.id == id:
                p.name = input("Enter new Name: ")
                p.disease = input("Enter new disease: ")
                p.gender = input("Enter new gender: ")
                p.age = input("Enter new age: ")
                self.write_file()
                print(f"\nPatient whose ID is {id} has been edited.\n")
                return
        print("Cannot find the patient .....\n")