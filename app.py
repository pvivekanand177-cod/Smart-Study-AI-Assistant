import streamlit as st

st.set_page_config(page_title="Smart AI Study Assistant", page_icon="📚")
st.title("📚 Smart AI Study & Exam Prep Assistant")
st.write("Built by Vivekanand Pandey | Global AI Hackathon")

tab1, tab2 = st.tabs(["📅 Smart Study Planner", "🧠 Concept Quiz"])

with tab1:
    st.subheader("Create Your Study Schedule")
    subject = st.text_input("Subject Name", "Python Programming")
    days = st.number_input("Days Left for Exam", min_value=1, max_value=90, value=10)
    hours = st.number_input("Daily Study Hours", min_value=1, max_value=16, value=3)

    if st.button("Generate Plan"):
        study_days = max(1, int(days * 0.7))
        revision_days = days - study_days
        st.success(f"**Plan for {subject}:**")
        st.write(f"• **Core Concept Learning:** {study_days} days ({study_days * hours} total hours)")
        st.write(f"• **Mock Tests & Revision:** {revision_days} days ({revision_days * hours} total hours)")

with tab2:
    st.subheader("Quick Concept Check")
    topic = st.selectbox("Choose Topic", ["Python Loops", "Time Complexity", "Machine Learning"])
    
    if topic == "Python Loops":
        st.info("**Concept:** `for` loops iterate over sequences, while `while` loops run until a condition becomes False.")
        ans = st.radio("Which keyword skips the current iteration in a loop?", ["break", "continue", "pass"])
        if st.button("Check Answer"):
            if ans == "continue":
                st.success("Correct! `continue` jumps to the next iteration.")
            else:
                st.error("Incorrect. The right answer is `continue`.")
    elif topic == "Time Complexity":
        st.info("**Concept:** Linear Search checks elements one by one, taking O(n) time in the worst case.")
        ans = st.radio("What is the best-case time complexity of Linear Search?", ["O(1)", "O(n)", "O(log n)"])
        if st.button("Check Answer"):
            if ans == "O(1)":
                st.success("Correct! If the element is at index 0, it takes O(1).")
            else:
                st.error("Incorrect. Best case is O(1).")
    else:
        st.info("**Concept:** Supervised learning trains models on labeled input-output pairs.")
        ans = st.radio("Predicting house prices is an example of:", ["Regression", "Clustering", "Reinforcement"])
        if st.button("Check Answer"):
            if ans == "Regression":
                st.success("Correct! Continuous value prediction is Regression.")
            else:
                st.error("Incorrect. It is Regression.")
