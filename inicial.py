import base64
import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import (CredentialsError,
                                               ForgotError,
                                               Hasher,
                                               LoginError,
                                               RegisterError,
                                               ResetError,
                                               UpdateError)

main_bg2 = "IA.jpg"

# def set_bg_hack(main_bg):
#     '''
#     A function to unpack an image from root folder and set as bg.
 
#     Returns
#     -------
#     The background.
#     '''
#     # set bg name
#     main_bg_ext = "png"
        
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )
    
# set_bg_hack(main_bg2)

st.image(main_bg2)

""" 
🎓 **Bem-vindo ao Aplicativo de Aprendizado de Inteligência Artificial! ✨**
"""


# Loading config file
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# authenticator = stauth.Authenticate(
#     '../config.yaml'
# )


# st.divider()
# abas = ['Login', 'Registro', 'Esqueci a Senha', 'Esqueci o Login']

# aba1, aba2, aba3, aba4 = st.tabs(abas)

# with aba1:
    

#     # Creating a login widget
#     try:
#         authenticator.login()
#     except LoginError as e:
#         st.error(e)
#     if st.session_state["authentication_status"] is True:
#         st.session_state.pagina = "paginas/aulas.py"
#         st.write('Escolha uma página para continuar')
#     elif st.session_state["authentication_status"] is False:
#         st.error('Username/password is incorrect')
#     elif st.session_state["authentication_status"] is None:
#         st.warning('Please enter your username and password')

  

# with aba2:


#     # Creating a new user registration widget
#     try:
#         (email_of_registered_user,
#          username_of_registered_user,
#          name_of_registered_user) = authenticator.register_user()
#         if email_of_registered_user:
#             st.success('User registered successfully')
#             # Saving config file
#             with open('config.yaml', 'w', encoding='utf-8') as file:
#                 yaml.dump(config, file, default_flow_style=False)

#     except RegisterError as e:
#         st.error(e)



# with aba3:
   

#     # Creating a forgot password widget
#     try:
#         (username_of_forgotten_password,
#          email_of_forgotten_password,
#          new_random_password) = authenticator.forgot_password()
#         if username_of_forgotten_password:
#             st.success(f"New password **'{new_random_password}'** to be sent to user securely")
#             config['credentials']['usernames'][username_of_forgotten_password]['pp'] = new_random_password
#             with open('config.yaml', 'w', encoding='utf-8') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             # Random password to be transferred to the user securely
#         elif not username_of_forgotten_password:
#             st.error('Username not found')
#     except ForgotError as e:
#         st.error(e)

# with aba4:
    

#     # Creating a forgot username widget
#     try:
#         (username_of_forgotten_username,
#          email_of_forgotten_username) = authenticator.forgot_username()
#         if username_of_forgotten_username:
#             st.success(f"Username **'{username_of_forgotten_username}'** to be sent to user securely")
#             with open('config.yaml', 'w', encoding='utf-8') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             # Username to be transferred to the user securely
#         elif not username_of_forgotten_username:
#             st.error('Email not found')
#     except ForgotError as e:
#         st.error(e)




