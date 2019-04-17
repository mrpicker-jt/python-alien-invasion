import os

path = os.getcwd()
print(path)

f = os.listdir(os.getcwd())
for file_name in f:
    if file_name.endswith('m4a'):
        command = 'ffmpeg -i "' + os.path.abspath(file_name) + '" -y  ' + \
                  ''.join(file_name.replace('.m4a', '.mp3').split())
        # command='ffmpeg -i "'+os.path.abspath(file_name)+'" -acodec libmp3lame -y -aq 2  ' + \
        # ''.join(file_name.replace('.m4a','.mp3').split())
        print(command)
        os.system(command)
