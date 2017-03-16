# coding=utf-8
import ConfigParser

# path = "F:\\python\\autosjg"
# list_name = "config.conf"

# def get_conf(path,list_name):
#     conf_information = {}
#     conf = ConfigParser.ConfigParser()

config = ConfigParser.ConfigParser()
config.readfp(open(raw_input("input file name:"),"rb"))
print config.get("global","ip","port")
print config.get("global1","port")