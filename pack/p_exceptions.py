class P_Exceptions:
    def exce(self, item):
        try:
            file = open("order.txt", "a")
            print("File found")
            for x in item.split(","):
                file.write(x.lstrip() + "\n")
            file.close()
        except FileNotFoundError as errmsg:
            print("File not found: {}".format(errmsg))
            print("Creating the file...")
            file2 = open("order.txt", "w")
            file2.write(item+"\n")
            file2.close()
        finally:
            print('Goodbye')