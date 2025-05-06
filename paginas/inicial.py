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

main_bg2 = "IA.png"

st.image(main_bg2)

""" 
**Bem-vindo ao Aplicativo de Aprendizado de Inteligência Artificial! ✨**

"""
