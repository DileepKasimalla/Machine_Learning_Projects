import pickle
import streamlit as st 

pickle_in = open("wine_quality.pkl","rb")
model=pickle.load(pickle_in)

def predict_note_authentication(fixedacidity, volatileacidity, citricacid, residualsugar,chlorides, freesulfurdioxide, totalsulfurdioxide,density,pH, sulphates, alcohol
):
    prediction=model.predict([[fixedacidity, volatileacidity, citricacid, residualsugar,chlorides, freesulfurdioxide, totalsulfurdioxide,density,pH, sulphates, alcohol]])
    print(prediction)
    return prediction

def main():
    st.title("WINE QUALITY PREDICTION")
    fixedacidity  = st.number_input("fixedacidity ",value = 0, step = 1)
    volatileacidity = st.number_input("volatileacidity",value = 0,step = 1)
    citricacid = st.number_input("citricacid",value = 0, step = 1)
    residualsugar = st.number_input("residualsugar",value = 0, step = 1)
    chlorides = st.number_input("chlorides",value = 0, step = 1)
    freesulfurdioxide = st.slider("freesulfurdioxide",0,100,25)
    totalsulfurdioxide = st.slider("totalsulfurdioxide",0, 300,100)
    density = st.number_input("density",value = 0, step = 1)
    pH = st.slider("pH",0,14,7)
    sulphates = st.number_input("sulphates",value = 0, step = 1)
    alcohol = st.number_input("alcohol",value = 0, step = 1)
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(fixedacidity, volatileacidity, citricacid, residualsugar,chlorides, freesulfurdioxide, totalsulfurdioxide,density,pH, sulphates, alcohol)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()