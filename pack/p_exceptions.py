class P_Exceptions:
    def exce(self):
        try:
            file = open("order.txt")
            print("File found")
        except FileNotFoundError as errmsg:
            print("File not found: {}".format(errmsg))
            # raise
        finally:
            print('Goodbye')