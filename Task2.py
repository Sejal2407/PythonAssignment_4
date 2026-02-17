try :
    with open("output.txt","w") as fh:
        main_data = input("Enter text to write to the file: ")
        fh.write(main_data)
        print("Data successfully written to output.txt")
    with open("output.txt","a") as fh:
        additional_data = input("Enter additional text to append: ")
        fh.write("\n"+additional_data)
        print("Data successfully appended")
    with open("output.txt","r") as fh:
        final_data = fh.read()
        print("Final content of output.txt: \n",final_data)
except IOError as error:
    print(error)

# try:
#     with open("output.txt","w+") as fh:
#         main_data = input("Enter text to write to the file: ")
#         fh.write(main_data)
#         print("Data successfully written to output.txt")
#
#         additional_data = input("Enter additional text to append: ")
#         fh.write(additional_data)
#         print("Data successfully appended")
#         fh.seek(0,0)
#         final_data = fh.read()
#         print("Final content of output.txt: \n",final_data)
# except IOError as error:
#     print(error)

