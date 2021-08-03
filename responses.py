from datetime import datetime

def sample_responses(input_text):
  user_message = str(input_text).lower()

  if user_message in ("hi", "hello", "cc"):
    return "Hello i'm Miss CC how are you ?"

  if user_message in ("who are you ?"):
    return "i am CC bot and you ?"

  if user_message in ("time", "time?"):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")

    return str(date_time)

  return "what the hack is this ?"
