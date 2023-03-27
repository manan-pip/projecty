  import streamlit as st
from streamlit_option_menu import option_menu

# Third change in april
 
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
into=st.container()
def show_main_page():
  with mainSection:
    with st.sidebar:
         
     selected = option_menu('CardioVascular Disease Prediction System',
                               
                               ['Predict Disease',
                                'My Records',
                                 'More Informatio'],
                                icons=['activity','record','person']
                               )
         
    if selected == "Predict Disease":
        with st.form("my_form"):
           
           c1,c2,c3=st.columns([4,3,2])
           with c2:
               st.markdown(":green[Prediction Form]",unsafe_allow_html=True)
        
           col1,col3,col2=st.columns([3,1,3])
        
           with col1:
               st.number_input(":green[Age (In Days)]",min_value=1,key="age",step=1)
               st.number_input(":green[Height (In cm)]",min_value=1,key="height")
               st.number_input(":green[Weight (In kg)]",min_value=1,key="weight")
               st.number_input(":green[Systolic Blood Pressure]",min_value=1,key="SBP")
               st.number_input(":green[Diastolic Blood Pressure] ",min_value=1,key="Dbp")
        
           with col2:
               
               st.radio(":green[Your Gender] ",("Women","Men"),key="gender",horizontal=True)   
               st.radio(":green[Cholesterol] ",("normal","High","Too High"),key="cholesterol",horizontal=True)
               st.radio(":green[Gluecose] ",("normal","High","Too High"),key="gluc",horizontal=True)
               st.radio(":green[Do You Excesie]",("Yes","No"),key="excerise",horizontal=True)           
               st.radio(":green[Do You Smoke]",("Yes","No"),key="smoke",horizontal=True)    
               st.radio(":green[Do You Drink Alcohol]",("Yes","No"),key="alco",horizontal=True)    
                    
           
           col11, col22, col3 , col4, col5 = st.columns(5)
           
           with col11:
               pass
           with col22:
               pass
           with col4:
               pass
           with col5:
               pass
           with col3 :
               
               submitted = st.form_submit_button("Submit")
           if submitted:
                 st.success("submitted")
        
        st.write("Outside the form")
        
        lst=st.session_state
        
        st.write(lst)
    
    if selected=="My Records":
        st.markdown(":red[You Don't Have Any Previous recordds Now]")
    if selected=="More Informatio":
        st.markdown(":grenn[We are working on that]")
    #age;gender;height;weight;ap_hi;ap_lo;cholesterol;gluc;smoke;alco;active;cardio
        
        
        #age=days
        #gender = 1women, 2men 
        #heght =cm 
        #weight = kg 
        #ap_low systolic 
        #
        #ap_hi diastolic
        #
        #cholestorel 
        #gluc
        #physical activa 1 , 0 
        #alco 1 , 0
        #smoke 1,0
        #smoke 1,0
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(userName, password):
    if userName=="manan" and password=="abc":
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False;
        st.error("Invalid user name or password")
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label=":green[Name] ", value="", placeholder="Enter your user name")
            password = st.text_input (label=":green[Password]", value="",placeholder="Enter password", type="password")
            col1,col2=st.columns([2,3])
            with col2:
              st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))


with headerSection:
    c1,c2=st.columns([1,2])
    with c2:
      st.title(":red[CVD Prediction]")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()  
        else:
            show_login_page()

    
