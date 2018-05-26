randomNumber <- as.integer(runif(1, 0, 100))
print(paste(randomNumber))
repeat {
  inputNumber <- readline(prompt="Enter number: ")
  inputNumber <- as.integer(inputNumber)
  
  if(inputNumber > randomNumber) {
    print("The randomNumber is smaller")
  } else if (inputNumber < randomNumber) {
    print("The randomNumber is bigger")
  } else {
    print("You find the number. Nice.")
    break
  }
}
