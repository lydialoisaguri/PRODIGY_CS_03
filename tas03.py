mport re

def check_password_strength(password):
  length_criteria = 8
  uppercase_criteria = re.compile(r'[A-Z]')
  lowercase_criteria = re.compile(r'[a-z]')
  digit_criteria = re.compile(r'\d')
  special_char_criteria = re.compile(r'[^A-Za-z0-9]')

  strength_score = 0
  feedback_message = ""

  if len(password) >= length_criteria:
    strength_score +=1
  else:
    feedback_message +="Password should contain at least {} characters long.\n".format(length_criteria)

  if uppercase_criteria.search(password):
    strength_score += 1
  else:
    feedback_message += "Password should contain at least one uppercase letter.\n"

  if lowercase_criteria.search(password):
    strength_score += 1
  else:
    feedback_message += "Password should contain at least one lowercase letter.\n"

  if digit_criteria.search(password):
    strength_score += 1
  else:
    feedback_message += "Password should contain at least one digit.\n"

  if special_char_criteria.search(password):
    strength_score += 1
  else:
    feedback_message += "Password should contain at least one special character.\n"

  if strength_score == 5:
    feedback_message += "Strong password!"
  elif strength_score >= 3:
    feedback_message += "Medium strength password."
  else:
    feedback_message += "Weak password. Please improve."

  return feedback_message

def main():
  password = input("Enter your password: ")
  strength_feedback = check_password_strength(password)
  print(strength_feedback)

if __name__ == "__main__":
  main()
