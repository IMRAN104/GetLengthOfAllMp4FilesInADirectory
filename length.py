#Try No. -> for multiple files simultaneously
import os
def list_all_files_in_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                #print(os.path.join(root, file))
                file_list.append(str(os.path.join(root, file)))
    return file_list



def get_length(file_list):
    from mutagen.mp4 import MP4
    total_length = 0
    # f_name = ''
    for filePath in file_list:
        try:
            if filePath.endswith('.mp4'):
                mp4 = MP4(filePath)
                total_length = total_length + mp4.info.length
                # print(length.info.length)
                # print(os.path.getsize(filePath))
                # print(total_length)
                # f_name = filePath
        except:
            # print(f_name)
            continue
    # print(f_name)
    return total_length

current_directory = os.getcwd()
file_list = list_all_files_in_directory(current_directory)

#print(file_list)
total_length_in_seconds = get_length(file_list)
total_length_in_minutes = total_length_in_seconds / 60
total_length_in_hour = int(total_length_in_minutes / 60)
minutes = int(total_length_in_minutes % 60)
total_length_formatted = f'{total_length_in_hour} hr {minutes} min'
print(total_length_formatted)













# #Try No. 3 -> working for single file
# import os
# from mutagen.mp4 import MP4
# filePath = "01. Welcome Aboard-jNPJnAxbOK8.mp4"
# length = MP4(filePath)

# print(length.info.length)
# # print(os.path.getsize(filePath))