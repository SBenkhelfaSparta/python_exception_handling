class PExceptions:
    def exce(self, item):
        try: #check if file exists
            file = open("order.txt", "r+") #read and write
            print("File found, the contents are:")
            print(file.read()) #position of writing is now pushed to the end
            for x in item.split(","):
                file.write(x.lstrip() + "\n")
            file.close()
        except FileNotFoundError as errmsg: #create file if it doesn't exist
            print("File not found: {}".format(errmsg))
            print("Creating the file...")
            file2 = open("order.txt", "w")
            for x in item.split(","):
                file2.write(x.lstrip() + "\n")
            file2.close()
        finally:
            print('Goodbye')