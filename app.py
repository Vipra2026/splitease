import streamlit as st
import v 

if "members" not in st.session_state:
    st.session_state.members = []

if "expense_dic" not in st.session_state:
    st.session_state.expense_dic = []

v.members = st.session_state.members
v.expense_dic = st.session_state.expense_dic

st.title("SplitEase")

name = st.text_input("Enter name").lower()
submit = st.button("Add Member")
if submit == True:
    st.session_state.members.append(name)

st.write(", ".join(st.session_state.members))

paid_by = st.text_input("Who paid").lower()
activity = st.text_input("Activity name").lower()
amount = st.number_input("Enter amount", min_value=0, step=1, format="%d")
activity_and_expense = {activity:amount}
involved_members = st.text_input("Involved members (optional)").lower()
if involved_members == (""):
    involved_members = st.session_state.members
else:
    involved_members = involved_members.split(",")
add_details = st.button("Add Expense")

if add_details == True:
    valid = True
    for find_name in involved_members:
        if find_name not in v.members:
            st.error(f"Please add {find_name} as a member first.")
            valid = False
    if valid == True:
        expense_dic = {
            "paid by" : paid_by,
            "expense details" : activity_and_expense,
            "involved members" : involved_members
        }
        st.session_state.expense_dic.append(expense_dic)
for op in st.session_state.expense_dic:
    st.write(f"{op['paid by']} paid {next(iter(op['expense details'].values()))} for {next(iter(op['expense details'].keys()))}.")

calculate = st.button("Calculate")
if calculate == True:
    st.write(f"Total Expense is {v.calculate_total()}.")
    for line in v.calculate_settlements():
        st.write(line)