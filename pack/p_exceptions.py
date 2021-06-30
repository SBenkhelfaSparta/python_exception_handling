class P_Exceptions:
    def exce(self):
        try:
            file = open("order.txt")
            print("File found")
        except FileNotFoundError as errmsg:
            print("File not found: {}".format(errmsg))
            file2 = open("order.txt", "w")
            file2.write("one of everything")
            file2.close()
        finally:
            print('Goodbye')