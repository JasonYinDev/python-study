from users import login

def userRegister(username,password):
  print(f"使用{username},{password}注册")
  login.userLogin(username,password)

userRegister("jason","password")