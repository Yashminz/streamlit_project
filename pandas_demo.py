import streamlit as st
import pandas as pd
import plotly.express as px


stu_records={
    "name":["kiran","sachin","harry","sachin","pooja"],
    "rollno":[1,2,3,4,5],
    "age":[21,23,18,21,23]
}


df=pd.DataFrame(stu_records)

st.dataframe(df)

px.bar(df,x="name",y="age",color="age",title="Age of Students")

st.plotly_chart(px.bar(df,x="name",y="age",color="age",title="Age of Students",text="age",template="plotly_dark"))