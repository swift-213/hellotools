def hello_world():
  """Print a greeting to the whole world."""
  print("Hello, world take 2!")
  return "Hello, world take 2!"

#you don't need main if you only have functions. Main would be for the scipt info like argparse or just main python code!
def main():
  hello_world()

if __name__ == "__main__":
  main()