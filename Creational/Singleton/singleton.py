class Logger:
    __instance = None
    def __new__(cls,file):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.file_name = file
            cls.__instance.log_count = 0
        return cls.__instance

    def log(self, message):
        print(f"Logging in {self.file_name} this message:{message}")
        self.log_count += 1
    def get_log_count(self):
        return self.log_count   
l1=Logger("app.log")
l1.log("Hey")
l2=Logger("app.log")
l2.log("Bye")
l3=Logger("app.log")
l3.log("Good")
print(l1.get_log_count())
print(l2.get_log_count())
print(l3.get_log_count())   