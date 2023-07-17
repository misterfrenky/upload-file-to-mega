import sys, getopt
from mega import Mega

def login(email, password):
  mega = Mega()
  try: 
    return mega.login(email, password)
  except:
    print("Authecation Failed!")
    return False

def upload_to_mega(auth, filename, remote_path):
  link = ''
  try:
    if(remote_path == None or remote_path == ''):
      file = auth.upload(filename)
      link = auth.get_upload_link(file)
    else:
      try:
        folder = auth.find(remote_path)
        if(len(folder)):
          file = auth.upload(filename, folder[0])
          link = auth.get_upload_link(file)
      except:
        print("Folder not found!")
  except:
    print('Something went wrong!')
  print("Uploadeded with Link: %s" % link)

def main(argv):
  remote_path = ''
  filename = ''
  email = ''
  password = ''
  opts, args = getopt.getopt(argv,"hi:e:p:d:f:",["ifile=","ofile="])
  for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-e", "--Email"):
         email = arg
      elif opt in ("-p", "--Password"):
         password = arg
      elif opt in ("-d", "--Directory"):
         remote_path = arg
      elif opt in ("-f", "--Filename"):
         filename = arg
  auth = login(email, password)
  if(auth is not False): 
    upload_to_mega(auth, filename, remote_path)

if __name__ == "__main__":
  main(sys.argv[1:])
