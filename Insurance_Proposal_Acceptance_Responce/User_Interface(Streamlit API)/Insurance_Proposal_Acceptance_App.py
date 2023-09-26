import pickle
import streamlit as st 


pickle_in = open("a_hack.pkl","rb")
model=pickle.load(pickle_in)

def predict_note_authentication(Proposed_Insurance_Type_joint , Max_Age, Policy_Holding_Duration,Proposed_Health_Insurance_Category):
    prediction=model.predict([[Proposed_Insurance_Type_joint , Max_Age, Policy_Holding_Duration,Proposed_Health_Insurance_Category]])
    print(prediction)
    return prediction

def main():
    st.title("Insurance Proposal Acceptance Response Prediction for a FinTech Company")
    Proposed_Insurance_Type_joint  = st.selectbox("Proposed_Insurance_Type_joint ",[0,1])
    Max_Age = st.number_input("Max_Age",value = 0,step = 1)
    Policy_Holding_Duration = st.slider("Policy_Holding_Duration",0,25,100)
    Proposed_Health_Insurance_Category = st.slider("Proposed_Health_Insurance_Category",0,25,100)
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Proposed_Insurance_Type_joint , Max_Age, Policy_Holding_Duration,Proposed_Health_Insurance_Category)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()