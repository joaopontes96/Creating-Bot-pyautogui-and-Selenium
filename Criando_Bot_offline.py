import pyautogui

pyautogui.PAUSE = 2

# Abrir a ferramenta- o sistema- o programa

pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("baclirakspace")
pyautogui.press("enter")

# Preencher o login

pyautogui.click(x=551, y=306)
pyautogui.write('lira')

# Preencher a senha

pyautogui.click(x=636, y=362)
pyautogui.write('senha')

# Clicar em fazer login

pyautogui.click(x=571, y=489)
