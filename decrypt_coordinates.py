from termcolor import colored
import random
import sys
import math
import M2Crypto
import time


def decrypt(cipher, n, lam, mu):
  #cipher = 8937101318711593120665747361417974288869879739925322008878527810362757708703201677672686726357877499115564589590034949070677745105266155846793428921354823974054459098710178715620849504861491396956480005820744323006277523727790633751289839083118717936486232072949172867771360181200650846039420830140735758338612370602522808224247817954803368428450042808681250611031934190585679979528751153394315758501118756122590716474314192933342359324489998699574235270956684927279160430325827706632752264109946893595720733433498302698531527082083720981109272112366349263971295187099472219156842763074535462824018916002251819166304
  #lam = 157279115436635979042070060588192546046948966660939702848613668463619972851468295101239499771817334475867725902563092035631024486264639035755432395274774306675294126013034986925250889677504673416109870954718090617676738788527302195667019740296309463732727547814923630935423741517715360150847945150686927974000
  #n = 157279115436635979042070060588192546046948966660939702848613668463619972851468295101239499771817334475867725902563092035631024486264639035755432395274774331770944459521265243913036286343065126000380525186451802903618644674932730104077860719548768985648109062384773468589445569094536837159082602920749952547249
  #mu = 254673683386912418221737625200689568044266862680948896670818471207134809316035936254756704939611660538664251583768229825382154309352108458700904554951513406281148027137192650781238761087018940391449290451534381800276984237927516416533571846607174186798690373086709688718543985686321233297139966446093674610
  n_sq = n * n
  x = pow(cipher, lam, n_sq) - 1
  # print "x = ", x
  # print "pow_cl_modn_sq = ", pow(cipher, lam, n_sq)
  # print "pow_cl_modn_sq-1 = ", pow(cipher, lam, n_sq) - 1
  plain = ((x // n) * mu) % n
  # print "x//n = ", x // n
  return plain


def read_server1_pk():
  for line in open('creator_pk.txt', "r+"):
    # print line
    n = line
    return n

sklist = []


def read_server1_sk():
  for line in open('creator_sk.txt', "r+"):
    sklist.append(line)


def readCipher1():
  for line in open('cipher1.txt', "r+"):
    return line


def writePlaintext(plain):
  f = open('plain.txt', "w+")
  f.write(plain)

n = read_server1_pk()
read_server1_sk()
# print "n :", n
cipher1 = readCipher1()
# print "cipher1 :", cipher1
lam = sklist[0]
mu = sklist[1]
# print "lam :", lam
# print "mu :", mu

plain = decrypt(int(cipher1), int(n), int(lam), int(mu))
print "plain :", plain
writePlaintext(str(plain) + '\n')
