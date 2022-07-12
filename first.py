import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Alisan Smart Homes - Smart Calculator",
    page_icon="🧊",
    initial_sidebar_state="auto",
    #menu_items={
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "This is an *extremely* cool app!"
    #}
)

st.title('Alisan - Smart Calculator')

st.write("---")
st.subheader('Segment')
option = st.selectbox('Interested in which segment?',
    ('Choose','Retrofit Controllers (Turns ordinary switches to smart switch)', 'Touch Switches (Complete touch panel)'))

#st.write('You selected:', option)

if option == "Touch Switches (Complete touch panel)":
    st.write("---")
    st.subheader('Touch Switches')
    option_bhk = st.selectbox('What’s your home size?',
                          ('1BHK','2BHK','3BHK','4BHK'))
    
    number_swb = st.number_input(
        'How many Switchboards do you have?', min_value=1, max_value=5, step=1)
    st.write('You have ', number_swb, 'Switchboard(s)')
    
    option_plate_size = st.selectbox('Select Plate size or box size for rooms?',
                                     ('Choose', '8X6', '8X3', '5x3'))
    
    option_plate = st.selectbox('Please select suitable models for your master plates in the room?',
                                     ('Choose', '4 switch + 1 Fan', '6 switch + 1 Fan', '4 switch + 1 Fan + 1 socket', '6 switch + 1 Fan + 1 socket', '6 Switch', '8 Switch'))

    option_otherplate = st.selectbox('Please select more Touch switch models in the room?',
                                     ('Choose','2 Switch + 2 Socket', ' 2 Switch + 1 Socket', '4 Switch', '6 Switch', '8 Switch', '2 Switch', '4 switch + 1 Socket'))
                                     
    option_plate_size_l = st.selectbox('Select Plate size or box size for living room?',
                                     ('Choose', '8X6', '8X3', '5x3'))
    
    option_living_plate = st.selectbox('Please select suitable model for master plates in living room?',
                                       ('Choose', '8 Switch + 2 Fan', '12 Switch', '16 Switch', '8 Switch + 2 Fan + 2 Socket', '6 Switch + 1 Fan', '4 Switch + 1 Fan', '4 Switch + 1 Fan + 1 Socket', '8 Switch + 1 Fan'))

    option_living_plate = st.selectbox('Select further Touch Switches you want in your Home?',
                                       ('Choose', '2 switch', '2 switch + 2 socket', '8 Switch + 2 Fan', '12 Switch', '16 Switch', '8 Switch + 2 Fan + 2 Socket', '6 Switch + 1 Fan', '4 Switch + 1 Fan', '4 Switch + 1 Fan + 1 Socket', '8 Switch + 1 Fan'))

if option == "Retrofit Controllers (Turns ordinary switches to smart switch)":
    st.write("---")
    st.subheader('Retrofit Switches')
    
    analysis_dict = {
        "1BHK": 2,
        "2BHK": 3,
        "3BHK": 4,
        "4BHK": 5,
    }
    option_bhk = st.selectbox('What’s your home size?',
                              ('1BHK', '2BHK', '3BHK', '4BHK'))
    d = {}
    for i in range(1, analysis_dict[option_bhk]):
        
        with st.expander("Bedroom "+ str(i)):
            # d["string{}".format(i)] = st.number_input(
            #      'How many Switchboards do you have?', min_value=1, max_value=5, step=1)
            d["bed{}".format(i)] = st.number_input(
                'How many Switchboards do you have in Bedroom '+str(i) + ' ?', min_value=1, max_value=5, step=1)
            #st.write('You have', age, 'Switchboard(s) in Bedroom', i)
            
    option_r_living = st.selectbox('How many switches do you want to get automated in your living room?',
                                   ('Choose', '1 Switch', '2 Switch', '4 switch', '6 switch', "Don't want"))
                                   
    option_r_dining = st.selectbox('How many switches do you want to get automated in your dinning room?',
                                   ('Choose', '1 Switch', '2 Switch', '4 switch', '6 switch', "Don't want"))

    option_r_kitchen = st.selectbox('How many switches do you want to get automated in your Kitchen?',
                                   ('Choose', '1 Switch', '2 Switch', '4 switch', '6 switch', "Don't want"))
    
    option_r_kitchen = st.selectbox('Do you want to be regulated (Speed change) via Mobile App?',
                                    ('Choose', 'Yes', 'No'))
                                    
    ac_number = st.number_input(
        'How many AC’s you want to get automated?', min_value=0, max_value=6, step=1)
        
    geyser_number = st.number_input(
        'How many Geyser’s you want to get automated?', min_value=0, max_value=6, step=1)

    option_r_remote= st.selectbox('Do you want to configure remotes of AC, TV, DTh, Soundbar in your rooms?',
                                    ('Choose', 'Yes', 'No'))
    
    option_r_technician = st.selectbox('Do you want to get installation done with our expert technicians?',
                                   ('Choose', 'Yes', 'No'))
