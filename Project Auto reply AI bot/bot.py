import pyautogui
import pyperclip
import time
from google import genai

client = genai.Client(api_key="Gemini api key")

# Give user some time to switch to the target window
time.sleep(2)

# Step 1: Click on the icon at (1295, 1051)
pyautogui.click(1265, 1051)
time.sleep(1)  # Wait for the application to open

def last_message_from_sender(chat_log, sender_name):
    messages = chat_log.strip().split("/2024] ")[0]
    if sender_name in messages:
        return True
    return False

while True:
    time.sleep(15)
# Step 2: Click and drag to select text from (490, 158) to (1860, 930)
    pyautogui.moveTo(705, 230)  # Move to start position
    pyautogui.mouseDown()  # Press mouse button
    pyautogui.moveTo(734, 928, duration=1)  # Drag to end position
    pyautogui.mouseUp()  # Release mouse button
    time.sleep(0.5)  # Give some time for selection

    # Step 3: Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')  # Press Ctrl+C
    pyautogui.click(734, 890)
    time.sleep(0.5)  # Wait for copying process

    # Step 4: Retrieve text from clipboard
    chat_history = pyperclip.paste()

    # Step 5: Print the copied text
    # print("Copied Text:", chat_history)

    if last_message_from_sender(chat_history, "Ashwin"):
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents= f"You are a person named shreyans who speaks both hindi and english, lives in india and is a 21 year old boy. You will be given chat history your work will be to short reply to the chats accordingly after analysing them.You are an autoreply chatbot so just analyse their last texts and just generate a good reply to it nothing else. Reply every text like a human named shreyans would reply and nothing else. fully pretend that you are a human named shreyans and talking to another person in the chatbox. Do not use that Reply word.  Your chat history is {chat_history}"
        )

        pyperclip.copy(response.text) # Copying the response text to the clipboard

        # Step 6: Click at reply box 
        pyautogui.click(1100, 955)
        time.sleep(1)

        # Step 7: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Step 8: Press Enter
        pyautogui.press('enter')

