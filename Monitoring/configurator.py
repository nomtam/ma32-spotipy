# CR: bad file naming
import configparser

config_data = configparser.ConfigParser()
# CR: you should put a relative path. If I try to run this from my PC it won't find REFAEL user
config_data.read("C:\\Users\\REFAEL\\Desktop\\spotipy\\config.ini")