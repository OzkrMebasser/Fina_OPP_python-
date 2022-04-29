# Algunos intentos fallidos jajajaja
# import csv
# # import glob
# # import os

# # path = r'.\_C:\Users\amendozad\Desktop\oScAr\Estudios\Python\academlo_python\Final_OPP_python\final_OPP_venv\Final_OPP\quizes'  # Path of directory containing data files.
# # extension = 'csv'

# # fieldnames = 'Rank', 'First Name', 'Last Name', 'Attempt #', 'Accuracy', 'Score'
# # output_filename = 'quiz_1.csv'  # Output filename.

# # output_filepath = os.path.join(path, output_filename)  # Output in same directory.

# # csvlist = [filename for filename in glob.glob(os.path.join(path, f'*.{extension}'))
# #             if filename != output_filepath]  # Avoid reading any existing output file.
# # print(csvlist) # Print out the list of csv file names.

# # with open(output_filepath, 'w', newline='') as sortfile:
# #     csv_writer = csv.DictWriter(sortfile, fieldnames=fieldnames, delimiter=',',
# #                                 extrasaction='ignore')
# #     csv_writer.writeheader()
# #     for file in csvlist:
# #         with open(file, 'r', newline='') as csvfile:
# #             csv_writer.writerows(csv.DictReader(csvfile))

# # print('quiz_1.csv')
# # import csv

# class Quiz():
#   def __init__(self, filename):
    
#     self.filename= filename

#   @classmethod
#   def generate_list(self, Rank, First_Name, Last_Name, Attempt, Accuracy, Score):
#     self.Rank = Rank
#     self.First_Name = First_Name
#     self.Last_Name = Last_Name
#     self.Attempt = Attempt
#     self.Accuracy = Accuracy
#     self.Score = Score

#     with open(self.filename, "r") as filename:
#         reader = csv.reader(filename)
#         for row in reader:
#            print(row)
#     print( """
#                 Rank: {0}, 
#                 First_Name: {1}, 
#                 Last_Name: {2}, 
#                 Attempt: {3}, 
#                 Accuracy: {4}, 
#                 Score: {5}""".format(row[0], row[1], row[2], row[3], row[4], row[5])
                                                                                        
#                 ) 

# quiz_1 = Quiz("quiz_1.csv").generate_list

# print(quiz_1)




# with open('quiz_1.csv') as f:
#   reader = csv.reader(f)
#   for row in reader:
#     print('Rank: {0}, First Name: {1}, Last Name: {2}, Attempt: {3}, Accuracy: {4}, Score: {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))